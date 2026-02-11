"""
Semana 11: Padrões Factory e Singleton
"""

# SINGLETON
class GerenciadorDeJogo:
    _instancia = None
    
    def __new__(cls):
        if cls._instancia is None:
            cls._instancia = super().__new__(cls)
            cls._instancia.jogadores = []
        return cls._instancia
    
    def adicionar_jogador(self, jogador):
        self.jogadores.append(jogador)
        print(f"✅ {jogador} adicionado. Total: {len(self.jogadores)}")

# FACTORY
class ItemFactory:
    @staticmethod
    def criar_arma(tipo):
        armas = {
            "espada": ("Espada Longa", 25),
            "machado": ("Machado de Guerra", 30),
            "adaga": ("Adaga Rápida", 15)
        }
        if tipo in armas:
            nome, dano = armas[tipo]
            return {"nome": nome, "dano": dano, "tipo": "arma"}
        return None
    
    @staticmethod
    def criar_pocao(tipo):
        pocoes = {
            "vida": ("Poção de Vida", 50),
            "mana": ("Poção de Mana", 30)
        }
        if tipo in pocoes:
            nome, efeito = pocoes[tipo]
            return {"nome": nome, "efeito": efeito, "tipo": "poção"}
        return None

if __name__ == "__main__":
    # Testando Singleton
    g1 = GerenciadorDeJogo()
    g2 = GerenciadorDeJogo()
    print(f"g1 é g2? {g1 is g2}")  # True
    
    g1.adicionar_jogador("Arthur")
    g2.adicionar_jogador("Merlin")  # Mesma instância!
    
    # Testando Factory
    espada = ItemFactory.criar_arma("espada")
    pocao = ItemFactory.criar_pocao("vida")
    print(f"\nItem criado: {espada}")
    print(f"Item criado: {pocao}")
