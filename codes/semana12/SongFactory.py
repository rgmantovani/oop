from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass


# ── Produto base ──────────────────────────────────────────
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


# ── Simple Factory ────────────────────────────────────────
class SongFactory:
    # Registry: mapeamento genre -> classe
    # Adicionar novo gênero = uma linha aqui
    _registry: dict[str, type[Song]] = {
        "rock":    RockSong,
        "pop":     PopSong,
        "jazz":    JazzSong,
        "electro": ElectroSong,
    }

    @classmethod
    def create(
        cls,
        genre: str,
        title: str,
        artist: str,
        bpm: int,
    ) -> Song:
        if genre not in cls._registry:
            raise ValueError(f"Gênero desconhecido: {genre!r}")
        return cls._registry[genre](
            title=title, artist=artist, bpm=bpm)

    @classmethod
    def register(cls, genre: str, klass: type[Song]) -> None:
        """Extensão sem alterar código existente (OCP)."""
        cls._registry[genre] = klass


# ── Uso ───────────────────────────────────────────────────
if __name__ == "__main__":
    songs = [
        SongFactory.create("rock",    "Back in Black",
                           "AC/DC",      200),
        SongFactory.create("pop",     "Blinding Lights",
                           "The Weeknd", 171),
        SongFactory.create("jazz",    "So What",
                           "Miles Davis", 136),
        SongFactory.create("electro", "Strobe",
                           "deadmau5",   128),
    ]

    print("=== Tocando playlist ===")
    for s in songs:
        s.play()

    # Extensão dinâmica — sem alterar nada acima
    class SambaSong(Song):
        def play(self) -> None:
            print(f"[SAMBA] {self.info()}")

    SongFactory.register("samba", SambaSong)
    SongFactory.create(
        "samba", "Aquarela do Brasil",
        "Ary Barroso", 95).play()