from __future__ import annotations
from abc import ABC, abstractmethod
from dataclasses import dataclass
from collections import Counter
import random


# ── Track ────────────────────────────────────────────────
@dataclass(frozen=True)
class Track:
    name:   str
    artist: str
    genre:  str


# ── Strategy: RecommendationEngine ───────────────────────
class RecommendationEngine(ABC):
    @abstractmethod
    def recommend(self, history: list[Track]) -> list[Track]: ...


class SpotifyEngine(RecommendationEngine):
    """Recomenda faixas do gênero mais ouvido."""
    def recommend(self, history: list[Track]) -> list[Track]:
        top_genre = Counter(t.genre for t in history).most_common(1)[0][0]
        return [t for t in history if t.genre == top_genre]


class AppleMusicEngine(RecommendationEngine):
    """Recomenda faixas do artista mais ouvido."""
    def recommend(self, history: list[Track]) -> list[Track]:
        top_artist = Counter(t.artist for t in history).most_common(1)[0][0]
        return [t for t in history if t.artist == top_artist]


class DeezerEngine(RecommendationEngine):
    """Embaralha o histórico e retorna os 3 primeiros."""
    def recommend(self, history: list[Track]) -> list[Track]:
        shuffled = list(history)
        random.shuffle(shuffled)
        return shuffled[:3]


# ── Creator abstrato: MusicPlatform ──────────────────────
class MusicPlatform(ABC):

    def __init__(self) -> None:
        self._cache_key: frozenset | None = None
        self._cache: list[Track] = []

    # Factory Method — subclasse decide qual engine criar
    @abstractmethod
    def create_engine(self) -> RecommendationEngine: ...

    @property
    @abstractmethod
    def platform_name(self) -> str: ...

    def get_playlist(self, history: list[Track]) -> None:
        # Bônus: cache por identidade do histórico
        key = frozenset((t.name, t.artist) for t in history)
        if key == self._cache_key:
            print(f"[cache hit] ", end="")
        else:
            self._cache_key = key
            self._cache = self.create_engine().recommend(history)

        print(f"=== {self.platform_name} — Playlist ===")
        for t in self._cache:
            print(f"  {t.name}  —  {t.artist}")
        print()


# ── Creators concretos ───────────────────────────────────
class SpotifyPlatform(MusicPlatform):
    platform_name = "Spotify"
    def create_engine(self) -> RecommendationEngine:
        return SpotifyEngine()

class AppleMusicPlatform(MusicPlatform):
    platform_name = "Apple Music"
    def create_engine(self) -> RecommendationEngine:
        return AppleMusicEngine()

class DeezerPlatform(MusicPlatform):
    platform_name = "Deezer"
    def create_engine(self) -> RecommendationEngine:
        return DeezerEngine()


# ── Uso ──────────────────────────────────────────────────
if __name__ == "__main__":
    history = [
        Track("Blinding Lights",   "The Weeknd",   "Pop"),
        Track("Starboy",           "The Weeknd",   "Pop"),
        Track("Save Your Tears",   "The Weeknd",   "Pop"),
        Track("Bohemian Rhapsody", "Queen",        "Rock"),
        Track("Back in Black",     "AC/DC",        "Rock"),
        Track("Hotel California",  "Eagles",       "Rock"),
        Track("Shape of You",      "Ed Sheeran",   "Pop"),
        Track("Bad Guy",           "Billie Eilish","Pop"),
    ]

    platforms: list[MusicPlatform] = [
        SpotifyPlatform(),
        AppleMusicPlatform(),
        DeezerPlatform(),
    ]

    for p in platforms:
        p.get_playlist(history)
        # Segunda chamada com mesmo histórico → cache
        p.get_playlist(history)