"""
Semana 5: Polimorfismo e Sistema de Combate
"""

class Jogador:
    def __init__(self, nome):
        self.nome = nome
        self.hp = 100
    
    def atacar(self, alvo):
        raise NotImplementedError("Subclasses devem implementar atacar()")
    
    def receber_dano(self, dano):
        self.hp -= dano
        print(f"{self.nome} HP: {self.hp}")

class Guerreiro(Jogador):
    def atacar(self, alvo):
        dano = 25
        print(f"⚔️ {self.nome} ataca com espada!")
        alvo.receber_dano(dano)

class Mago(Jogador):
    def atacar(self, alvo):
        dano = 30
        print(f"✨ {self.nome} lança magia!")
        alvo.receber_dano(dano)

# Teste polimórfico
def batalha(atacante, defensor):
    print(f"\n=== {atacante.nome} vs {defensor.nome} ===")
    atacante.atacar(defensor)

if __name__ == "__main__":
    g = Guerreiro("Arthur")
    m = Mago("Merlin")
    
    personagens = [g, m]
    for p in personagens:
        batalha(p, Jogador("Alvo"))
