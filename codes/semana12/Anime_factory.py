from __future__ import annotations
from abc import ABC, abstractmethod


# ── Produto: Player de Episodio ───────────────────────────
class EpisodePlayer(ABC):
    @abstractmethod
    def load(self, anime: str, ep: int) -> None: ...

    @abstractmethod
    def show_ads(self) -> None: ...

    @abstractmethod
    def play(self) -> None: ...


# ── Produtos concretos ────────────────────────────────────
class CrunchyrollPlayer(EpisodePlayer):
    def load(self, anime: str, ep: int) -> None:
        print(f"  [CR] Carregando '{anime}' Ep.{ep} em 1080p...")

    def show_ads(self) -> None:
        print("  [CR] Ad: Crunchyroll Premium — assine! (30s)")

    def play(self) -> None:
        print("  [CR] Reproduzindo com legendas PT-BR")


class NetflixPlayer(EpisodePlayer):
    def load(self, anime: str, ep: int) -> None:
        print(f"  [NF] Preparando '{anime}' Ep.{ep} em 4K HDR...")

    def show_ads(self) -> None:
        pass  # plano pago, sem anuncios

    def play(self) -> None:
        print("  [NF] Reproduzindo com dublagem PT-BR")


class PiracyPlayer(EpisodePlayer):
    def load(self, anime: str, ep: int) -> None:
        print(f"  [??] Buscando torrent de '{anime}' Ep.{ep}...")

    def show_ads(self) -> None:
        print("  [??] Pop-up suspeito #1  |  Pop-up suspeito #2")

    def play(self) -> None:
        print("  [??] Reproduzindo em 480p — legenda mal-sincronizada")


# ── Creator abstrato ──────────────────────────────────────
class StreamingPlatform(ABC):

    # Factory Method — subclasse decide qual player criar
    @abstractmethod
    def create_player(self) -> EpisodePlayer: ...

    # Template Method — mesma sequencia para toda plataforma
    def watch(self, anime: str, ep: int) -> None:
        player = self.create_player()  # polimorfismo!
        player.load(anime, ep)
        player.show_ads()
        player.play()
        print()


# ── Creators concretos ────────────────────────────────────
class Crunchyroll(StreamingPlatform):
    def create_player(self) -> EpisodePlayer:
        return CrunchyrollPlayer()


class Netflix(StreamingPlatform):
    def create_player(self) -> EpisodePlayer:
        return NetflixPlayer()


class PirateSite(StreamingPlatform):
    def create_player(self) -> EpisodePlayer:
        return PiracyPlayer()


# ── Uso ───────────────────────────────────────────────────
if __name__ == "__main__":
    watchlist: list[tuple[StreamingPlatform, str, int]] = [
        (Crunchyroll(), "Demon Slayer",        12),
        (Netflix(),     "Neon Genesis Eva",     1),
        (PirateSite(),  "One Piece",         1100),
    ]

    print("=== Sessao de Anime ===")
    for platform, anime, ep in watchlist:
        print(f"--- {type(platform).__name__} ---")
        platform.watch(anime, ep)

    # Extensao: nova plataforma sem alterar nada acima
    class HiDivePlayer(EpisodePlayer):
        def load(self, anime: str, ep: int) -> None:
            print(f"  [HD] Streaming '{anime}' Ep.{ep} em 720p")
        def show_ads(self) -> None:
            print("  [HD] Ad: HiDive — simulcast exclusivo!")
        def play(self) -> None:
            print("  [HD] Reproduzindo com legenda PT-BR")

    class HiDive(StreamingPlatform):
        def create_player(self) -> EpisodePlayer:
            return HiDivePlayer()

    print("--- Nova plataforma ---")
    HiDive().watch("Frieren", 1)