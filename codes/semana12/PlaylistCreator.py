from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass


# ── Produto base (mesmo que o Simple Factory) ─────────────
@dataclass
class Song(ABC):
    title:  str
    artist: str
    bpm:    int

    @abstractmethod
    def play(self) -> None: ...

    def info(self) -> str:
        return f"{self.title} — {self.artist} ({self.bpm} BPM)"


# ── Produtos concretos ────────────────────────────────────
class RockSong(Song):
    def play(self) -> None:
        print(f"[ROCK]  {self.info()}")

class PopSong(Song):
    def play(self) -> None:
        print(f"[POP]   {self.info()}")

class JazzSong(Song):
    def play(self) -> None:
        print(f"[JAZZ]  {self.info()}")

class ElectroSong(Song):
    def play(self) -> None:
        print(f"[EDM]   {self.info()}")


# ── Creator abstrato ──────────────────────────────────────
class PlaylistCreator(ABC):

    # Factory Method — subclasse decide qual Song criar
    @abstractmethod
    def create_song(self, title: str, artist: str) -> Song: ...

    # Template Method — lógica igual para qualquer creator
    def generate_playlist(
        self, tracks: list[tuple[str, str, int]]
    ) -> list[Song]:
        """
        tracks: lista de (title, artist, bpm)
        Cada creator instancia o tipo de Song correto.
        """
        playlist = []
        for title, artist, bpm in tracks:
            # bpm é injetado depois para manter
            # a assinatura de create_song() simples
            song = self.create_song(title, artist)
            song.bpm = bpm
            playlist.append(song)
        return playlist

    def play_all(
        self, tracks: list[tuple[str, str, int]]
    ) -> None:
        print(f"=== {type(self).__name__} ===")
        for song in self.generate_playlist(tracks):
            song.play()
        print()


# ── Creators concretos ────────────────────────────────────
class RockPlaylist(PlaylistCreator):
    def create_song(self, title: str, artist: str) -> Song:
        return RockSong(title=title, artist=artist, bpm=0)

class PopPlaylist(PlaylistCreator):
    def create_song(self, title: str, artist: str) -> Song:
        return PopSong(title=title, artist=artist, bpm=0)

class JazzPlaylist(PlaylistCreator):
    def create_song(self, title: str, artist: str) -> Song:
        return JazzSong(title=title, artist=artist, bpm=0)

class ElectroPlaylist(PlaylistCreator):
    def create_song(self, title: str, artist: str) -> Song:
        return ElectroSong(title=title, artist=artist, bpm=0)


# ── Uso ───────────────────────────────────────────────────
if __name__ == "__main__":
    rock_tracks = [
        ("Back in Black",  "AC/DC",          200),
        ("Bohemian Rhapsody", "Queen",        144),
    ]
    pop_tracks = [
        ("Blinding Lights", "The Weeknd",    171),
        ("Shape of You",    "Ed Sheeran",    96),
    ]
    jazz_tracks = [
        ("So What",        "Miles Davis",    136),
        ("Autumn Leaves",  "Chet Baker",     92),
    ]

    creators: list[PlaylistCreator] = [
        RockPlaylist(),
        PopPlaylist(),
        JazzPlaylist(),
    ]
    tracks_map = [rock_tracks, pop_tracks, jazz_tracks]

    for creator, tracks in zip(creators, tracks_map):
        creator.play_all(tracks)

    # Extensão: nova playlist sem alterar nada acima
    class SambaSong(Song):
        def play(self) -> None:
            print(f"[SAMBA] {self.info()}")

    class SambaPlaylist(PlaylistCreator):
        def create_song(self, title: str, artist: str) -> Song:
            return SambaSong(title=title, artist=artist, bpm=0)

    SambaPlaylist().play_all([
        ("Aquarela do Brasil", "Ary Barroso", 95),
    ])