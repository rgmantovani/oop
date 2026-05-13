from __future__ import annotations

# ── Singleton ────────────────────────────────────────────
class Configuracao:
    _instancia: Configuracao | None = None

    def __new__(cls) -> Configuracao:
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._inicializado = False
        return cls._instancia

    def __init__(self):
        if self._inicializado:
            return
        self._dados: dict[str, str] = {
            "dificuldade": "normal",
            "volume":      "80",
            "idioma":      "pt-BR",
        }
        self._inicializado = True

    @classmethod
    def instancia(cls) -> Configuracao:
        return cls()

    def alterar(self, chave: str, valor: str) -> None:
        self._dados[chave] = valor

    def obter(self, chave: str) -> str:
        return self._dados[chave]

    def exibir(self) -> None:
        for chave, valor in self._dados.items():
            print(f"  [Config] {chave:<12} = {valor}")

# ── Classes consumidoras ─────────────────────────────────
class MenuPrincipal:
    def aplicar_configuracoes(self) -> None:
        cfg = Configuracao.instancia()
        cfg.alterar("dificuldade", "dificil")
        cfg.alterar("volume",      "60")
        print("[Menu] Configurações alteradas pelo jogador")
        cfg.exibir()

class Masmorra:
    def iniciar(self) -> None:
        print("\n[Masmorra] Lendo configurações do jogo...")
        Configuracao.instancia().exibir()  # ✅ vê "dificil"

# ── Uso ──────────────────────────────────────────────────
menu     = MenuPrincipal()
masmorra = Masmorra()

menu.aplicar_configuracoes()
masmorra.iniciar()

# Prova: mesmo objeto
a = Configuracao()
b = Configuracao()
print(f"\nMesma instância? {a is b} ✓")