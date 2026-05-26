# ✅ Padrão Singleton — uma única instância compartilhada
from __future__ import annotations

class GerenciadorDeJogo:

    # ou é uma instancia de Gerenciador de Jogo ou None, mas por default é None
    _instancia: GerenciadorDeJogo | None = None

    # método especial que cria o objeto antes do __init__
    # __new__ cria o objeto
    # __init__ inicializa o objeto
    def __new__(cls) -> GerenciadorDeJogo:
        if cls._instancia is None:

            # chama o __new__ da classe pai (object)
            # equivale a : object.__new__(cls)
            cls._instancia = super().__new__(cls)
            cls._instancia._inicializado = False
        return cls._instancia

    def __init__(self):
        if self._inicializado:  # evita resetar o estado a cada chamada
            return
        self.nivel  = 1
        self.ouro   = 0
        self.pontos = 0
        self._inicializado = True

    @classmethod
    def instancia(cls) -> GerenciadorDeJogo:
        """Ponto de acesso explícito — equivalente ao ::instancia() do C++."""
        return cls()

    def adicionar_ouro(self, qtd: int):   
        self.ouro   += qtd
    
    def adicionar_pontos(self, pts: int): 
        self.pontos += pts
    
    def subir_nivel(self):                
        self.nivel  += 1

    def exibir(self):
        print(f"[Gerenciador] "
              f"nivel={self.nivel}  ouro={self.ouro}  pontos={self.pontos}")


class Masmorra:
    def derrotar_chefe(self):
        mgr = GerenciadorDeJogo()  # sempre o mesmo objeto
        mgr.adicionar_pontos(500)
        mgr.subir_nivel()
        print("[Masmorra] Chefe derrotado!")
        mgr.exibir()


class Loja:
    def vender_espolio(self):
        mgr = GerenciadorDeJogo()
        mgr.adicionar_ouro(120)
        print("[Loja] Espólio vendido!")
        mgr.exibir()  # ✅ nivel=2 — mesmo objeto da Masmorra


class QuadroMissoes:
    def completar_missao(self, nome: str):
        mgr = GerenciadorDeJogo()
        mgr.adicionar_pontos(200)
        mgr.adicionar_ouro(50)
        print(f"[Missão] '{nome}' concluída!")
        mgr.exibir()


if __name__ == "__main__":

    masmorra = Masmorra()
    loja     = Loja()
    quadro   = QuadroMissoes()

    masmorra.derrotar_chefe()                      # nivel=2 pontos=500 ouro=0
    loja.vender_espolio()                          # nivel=2 pontos=500 ouro=120
    quadro.completar_missao("A Mina Maldita")      # nivel=2 pontos=700 ouro=170
    masmorra.derrotar_chefe()                      # nivel=3 pontos=1200 ouro=170
    quadro.completar_missao("O Retorno do Herói")   # nivel=3 pontos=1400 ouro=220
    loja.vender_espolio()                          # nivel=3 pontos=1400 ouro=340
    quadro.completar_missao("A Busca do Tesouro")   # nivel=3 pontos=1600 ouro=390

    # Prova: mesmo objeto em memória
    a = GerenciadorDeJogo()
    b = GerenciadorDeJogo()
    assert a is b, "Singleton falhou!"
    print("\nMesma instância?", a is b, "✓")