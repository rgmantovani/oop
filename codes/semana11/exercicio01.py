from __future__ import annotations

# ── Singleton ────────────────────────────────────────────
class Logger:
    _instancia: Logger | None = None

    def __new__(cls) -> Logger:
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia._inicializado = False
        return cls._instancia

    def __init__(self):
        if self._inicializado:
            return
        self._mensagens: list[str] = []
        self._inicializado = True

    @classmethod
    def instancia(cls) -> Logger:
        return cls()

    def registrar(self, msg: str) -> None:
        self._mensagens.append(msg)
        print(f"[LOG #{len(self._mensagens)}] {msg}")

    def exibir_todos(self) -> None:
        print(f"\nTotal de eventos: {len(self._mensagens)}")

# ── Classes consumidoras ─────────────────────────────────
class Heroi:
    def __init__(self, nome: str):
        self.nome = nome

    def atacar(self, alvo: str, arma: str) -> None:
        Logger.instancia().registrar(
            f"{self.nome} atacou {alvo} com {arma}")

    def usar_magia(self, magia: str, alvo: str) -> None:
        Logger.instancia().registrar(
            f"{self.nome} usou {magia} em {alvo}")

class Inimigo:
    def __init__(self, nome: str):
        self.nome = nome

    def receber_dano(self, qtd: int) -> None:
        Logger.instancia().registrar(
            f"{self.nome} recebeu {qtd} de dano")

# ── Uso ──────────────────────────────────────────────────
heroi  = Heroi("Herói")
dragao = Inimigo("Dragão")

heroi.atacar("Dragão", "espada")
dragao.receber_dano(40)
heroi.usar_magia("Bola de Fogo", "Dragão")
dragao.receber_dano(80)

Logger.instancia().exibir_todos()

# Prova: mesmo objeto
a = Logger()
b = Logger()
print(f"Mesma instância? {a is b} ✓")