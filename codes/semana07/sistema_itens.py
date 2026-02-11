"""
Semana 7: Sistema de Itens - Hierarquia
"""

class Item:
    def __init__(self, nome, peso, valor):
        self.nome = nome
        self.peso = peso
        self.valor = valor
    
    def __str__(self):
        return f"{self.nome} (Peso: {self.peso}kg, Valor: {self.valor} moedas)"

class Arma(Item):
    def __init__(self, nome, peso, valor, dano):
        super().__init__(nome, peso, valor)
        self.dano = dano
    
    def __str__(self):
        return f"⚔️ {super().__str__()} - Dano: {self.dano}"

class Armadura(Item):
    def __init__(self, nome, peso, valor, defesa):
        super().__init__(nome, peso, valor)
        self.defesa = defesa
    
    def __str__(self):
        return f"🛡️ {super().__str__()} - Defesa: {self.defesa}"

class Consumivel(Item):
    def __init__(self, nome, peso, valor, efeito, quantidade=1):
        super().__init__(nome, peso, valor)
        self.efeito = efeito
        self.quantidade = quantidade
    
    def usar(self):
        if self.quantidade > 0:
            self.quantidade -= 1
            print(f"✨ Usou {self.nome}! {self.efeito}")
            return True
        return False

if __name__ == "__main__":
    espada = Arma("Espada Longa", 3.5, 100, 25)
    escudo = Armadura("Escudo de Ferro", 5.0, 80, 15)
    pocao = Consumivel("Poção de Vida", 0.2, 20, "Restaura 50 HP", 3)
    
    print(espada)
    print(escudo)
    print(pocao)
    pocao.usar()
