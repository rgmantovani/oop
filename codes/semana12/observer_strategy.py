"""
Semana 12: Padrões Observer e Strategy
"""

# OBSERVER
class EventoJogo:
    def __init__(self):
        self.observers = []
    
    def adicionar_observer(self, observer):
        self.observers.append(observer)
    
    def notificar(self, evento, dados):
        for obs in self.observers:
            obs.atualizar(evento, dados)

class LogObserver:
    def atualizar(self, evento, dados):
        print(f"📝 LOG: {evento} - {dados}")

class PontuacaoObserver:
    def __init__(self):
        self.pontos = 0
    
    def atualizar(self, evento, dados):
        if evento == "inimigo_derrotado":
            self.pontos += dados
            print(f"⭐ Pontuação: {self.pontos}")

# STRATEGY
class EstrategiaCombate:
    def atacar(self):
        pass

class EstrategiaAgressiva(EstrategiaCombate):
    def atacar(self):
        return 30

class EstrategiaDefensiva(EstrategiaCombate):
    def atacar(self):
        return 10

class NPC:
    def __init__(self, nome):
        self.nome = nome
        self.estrategia = EstrategiaAgressiva()
    
    def mudar_estrategia(self, estrategia):
        self.estrategia = estrategia
    
    def atacar(self):
        dano = self.estrategia.atacar()
        print(f"{self.nome} ataca com {dano} de dano")

if __name__ == "__main__":
    # Observer
    eventos = EventoJogo()
    eventos.adicionar_observer(LogObserver())
    eventos.adicionar_observer(PontuacaoObserver())
    
    eventos.notificar("inimigo_derrotado", 100)
    eventos.notificar("item_coletado", "Espada")
    
    # Strategy
    print()
    npc = NPC("Goblin")
    npc.atacar()
    npc.mudar_estrategia(EstrategiaDefensiva())
    npc.atacar()
