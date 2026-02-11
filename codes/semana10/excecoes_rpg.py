"""
Semana 10: Tratamento de Exceções Customizadas
"""

class RPGException(Exception):
    """Exceção base do sistema RPG"""
    pass

class InventarioCheioException(RPGException):
    pass

class ItemNaoEncontradoException(RPGException):
    pass

class ManaInsuficienteException(RPGException):
    pass

class Mago:
    def __init__(self, nome):
        self.nome = nome
        self.mana = 50
    
    def lancar_magia(self, custo):
        if custo > self.mana:
            raise ManaInsuficienteException(
                f"{self.nome} precisa de {custo} mana, mas tem apenas {self.mana}"
            )
        self.mana -= custo
        print(f"✨ Magia lançada! Mana restante: {self.mana}")

class Inventario:
    def __init__(self, capacidade=5):
        self.itens = []
        self.capacidade = capacidade
    
    def adicionar(self, item):
        if len(self.itens) >= self.capacidade:
            raise InventarioCheioException(
                f"Inventário cheio! Capacidade: {self.capacidade}"
            )
        self.itens.append(item)
    
    def buscar(self, nome):
        for item in self.itens:
            if item == nome:
                return item
        raise ItemNaoEncontradoException(f"Item '{nome}' não encontrado")

if __name__ == "__main__":
    mago = Mago("Gandalf")
    inv = Inventario(capacidade=2)
    
    # Teste 1: Mana insuficiente
    try:
        mago.lancar_magia(100)
    except ManaInsuficienteException as e:
        print(f"❌ Erro: {e}")
    
    # Teste 2: Inventário cheio
    try:
        inv.adicionar("Espada")
        inv.adicionar("Escudo")
        inv.adicionar("Poção")  # Vai falhar
    except InventarioCheioException as e:
        print(f"❌ Erro: {e}")
    
    # Teste 3: Item não encontrado
    try:
        inv.buscar("Elixir")
    except ItemNaoEncontradoException as e:
        print(f"❌ Erro: {e}")
