"""
Semana 9: Interfaces - Itens Equipáveis
"""

from abc import ABC, abstractmethod

class Equipavel(ABC):
    @abstractmethod
    def equipar(self, jogador):
        pass
    
    @abstractmethod
    def desequipar(self, jogador):
        pass

class Arma(Equipavel):
    def __init__(self, nome, dano):
        self.nome = nome
        self.dano = dano
    
    def equipar(self, jogador):
        jogador.arma_equipada = self
        jogador.dano_total += self.dano
        print(f"⚔️ {self.nome} equipada! Dano +{self.dano}")
    
    def desequipar(self, jogador):
        jogador.dano_total -= self.dano
        jogador.arma_equipada = None
        print(f"Dano -{self.dano}")

class Armadura(Equipavel):
    def __init__(self, nome, defesa):
        self.nome = nome
        self.defesa = defesa
    
    def equipar(self, jogador):
        jogador.armadura_equipada = self
        jogador.defesa_total += self.defesa
        print(f"🛡️ {self.nome} equipada! Defesa +{self.defesa}")
    
    def desequipar(self, jogador):
        jogador.defesa_total -= self.defesa
        jogador.armadura_equipada = None

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.dano_total = 10
        self.defesa_total = 5
        self.arma_equipada = None
        self.armadura_equipada = None

if __name__ == "__main__":
    j = Jogador("Geralt")
    espada = Arma("Espada de Prata", 25)
    armadura = Armadura("Armadura de Lobo", 15)
    
    espada.equipar(j)
    armadura.equipar(j)
    print(f"\nStatus: Dano={j.dano_total}, Defesa={j.defesa_total}")
