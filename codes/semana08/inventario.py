"""
Semana 8: Sistema de Inventário
"""

class Item:
    def __init__(self, nome, peso):
        self.nome = nome
        self.peso = peso

class Inventario:
    def __init__(self, capacidade=20, peso_maximo=50):
        self.itens = []
        self.capacidade = capacidade
        self.peso_maximo = peso_maximo
    
    def adicionar(self, item):
        if len(self.itens) >= self.capacidade:
            print(f"❌ Inventário cheio! Capacidade: {self.capacidade}")
            return False
        
        if self.peso_total() + item.peso > self.peso_maximo:
            print(f"❌ Peso excedido! Limite: {self.peso_maximo}kg")
            return False
        
        self.itens.append(item)
        print(f"✅ {item.nome} adicionado ao inventário")
        return True
    
    def remover(self, nome):
        for item in self.itens:
            if item.nome == nome:
                self.itens.remove(item)
                print(f"🗑️ {nome} removido")
                return True
        print(f"❌ {nome} não encontrado")
        return False
    
    def peso_total(self):
        return sum(item.peso for item in self.itens)
    
    def listar(self):
        print(f"\n=== Inventário ({len(self.itens)}/{self.capacidade}) ===")
        print(f"Peso: {self.peso_total():.1f}/{self.peso_maximo}kg")
        for i, item in enumerate(self.itens, 1):
            print(f"{i}. {item.nome} ({item.peso}kg)")

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.inventario = Inventario()

if __name__ == "__main__":
    j = Jogador("Link")
    j.inventario.adicionar(Item("Espada", 3.0))
    j.inventario.adicionar(Item("Escudo", 5.0))
    j.inventario.adicionar(Item("Poção", 0.5))
    j.inventario.listar()
    j.inventario.remover("Poção")
    j.inventario.listar()
