# ❌ Cada sistema cria seu próprio GerenciadorDeJogo

class GerenciadorDeJogo:
    def __init__(self):
        self.nivel  = 1
        self.ouro   = 0
        self.pontos = 0

    def adicionar_ouro(self, qtd: int):   
        self.ouro   += qtd
    
    def adicionar_pontos(self, pts: int): 
        self.pontos += pts
    
    def subir_nivel(self):                
        self.nivel  += 1

    def exibir(self):
        print(f"[Gerenciador id={id(self)}] "
              f"nivel={self.nivel}  ouro={self.ouro}  pontos={self.pontos}")


class Masmorra:
    def __init__(self):
        self.mgr = GerenciadorDeJogo()  # cópia isolada

    def derrotar_chefe(self):
        self.mgr.adicionar_pontos(500)
        self.mgr.subir_nivel()
        print("[Masmorra] Chefe derrotado!")
        self.mgr.exibir()


class Loja:
    def __init__(self):
        self.mgr = GerenciadorDeJogo()  # outra cópia — não vê o level-up

    def vender_espolio(self):
        self.mgr.adicionar_ouro(120)
        print("[Loja] Espólio vendido!")
        self.mgr.exibir()  # BUG: nivel=1, pontos=0


if __name__ == "__main__":
    masmorra = Masmorra()
    loja     = Loja()

    masmorra.derrotar_chefe()
    loja.vender_espolio()   # estado divergente!