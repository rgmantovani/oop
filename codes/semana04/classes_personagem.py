"""
Semana 4: Herança - Classes de Personagem
Guerreiro, Mago e Ladrão herdam de Jogador
"""

class Jogador:
    """Classe base para todos os personagens"""
    
    def __init__(self, nome, nivel=1):
        self.nome = nome
        self.nivel = nivel
        self.hp = 100
        self.hp_maximo = 100
    
    def atacar(self):
        """Método genérico - será sobrescrito"""
        return 10
    
    def __str__(self):
        return f"{self.__class__.__name__}: {self.nome} (Nv.{self.nivel}) - HP: {self.hp}/{self.hp_maximo}"


class Guerreiro(Jogador):
    """Classe especializada em combate físico"""
    
    def __init__(self, nome, nivel=1):
        super().__init__(nome, nivel)
        self.forca = 15
        self.armadura = 10
        self.hp_maximo = 150
        self.hp = 150
    
    def atacar(self):
        """Ataque físico poderoso"""
        dano = self.forca * 2
        print(f"⚔️  {self.nome} desfere um golpe poderoso!")
        return dano
    
    def defender(self):
        """Habilidade especial: aumenta armadura temporariamente"""
        bonus_armadura = 5
        self.armadura += bonus_armadura
        print(f"🛡️  {self.nome} assume posição defensiva! (+{bonus_armadura} armadura)")


class Mago(Jogador):
    """Classe especializada em magia"""
    
    def __init__(self, nome, nivel=1):
        super().__init__(nome, nivel)
        self.poder_magico = 20
        self.mana = 100
        self.mana_maxima = 100
        self.hp_maximo = 80
        self.hp = 80
    
    def atacar(self):
        """Ataque mágico que consome mana"""
        custo_mana = 20
        if self.mana >= custo_mana:
            self.mana -= custo_mana
            dano = self.poder_magico * 2
            print(f"✨ {self.nome} lança uma bola de fogo! (Mana: {self.mana}/{self.mana_maxima})")
            return dano
        else:
            print(f"❌ {self.nome} não tem mana suficiente!")
            return 0
    
    def meditar(self):
        """Habilidade especial: recupera mana"""
        recuperacao = 30
        self.mana = min(self.mana + recuperacao, self.mana_maxima)
        print(f"🧘 {self.nome} medita e recupera {recuperacao} de mana")


class Ladrao(Jogador):
    """Classe especializada em agilidade e furtividade"""
    
    def __init__(self, nome, nivel=1):
        super().__init__(nome, nivel)
        self.agilidade = 18
        self.furtividade = 15
        self.hp_maximo = 100
        self.hp = 100
    
    def atacar(self):
        """Ataque furtivo com chance de crítico"""
        import random
        
        dano_base = self.agilidade
        if random.random() < 0.3:  # 30% de chance de crítico
            dano = dano_base * 3
            print(f"💀 {self.nome} acerta um GOLPE CRÍTICO!")
        else:
            dano = dano_base
            print(f"🗡️  {self.nome} ataca rapidamente!")
        
        return dano
    
    def esconder(self):
        """Habilidade especial: fica invisível"""
        print(f"🌫️  {self.nome} se esconde nas sombras! (Furtividade: {self.furtividade})")


# ============================================
# Programa de Teste
# ============================================

def main():
    print("=" * 60)
    print("SEMANA 4: Herança - Classes de Personagem")
    print("=" * 60)
    print()
    
    # Criando personagens de diferentes classes
    guerreiro = Guerreiro("Conan", nivel=5)
    mago = Mago("Gandalf", nivel=6)
    ladrao = Ladrao("Robin Hood", nivel=4)
    
    personagens = [guerreiro, mago, ladrao]
    
    # Exibindo informações
    print(">>> Personagens criados:\n")
    for p in personagens:
        print(p)
    print()
    
    # Testando polimorfismo (todos têm o método atacar)
    print(">>> Todos atacam:\n")
    for p in personagens:
        dano = p.atacar()
        print(f"   Dano causado: {dano}\n")
    
    # Testando habilidades específicas
    print(">>> Habilidades especiais:\n")
    guerreiro.defender()
    mago.meditar()
    ladrao.esconder()
    print()
    
    # Demonstrando herança
    print(">>> Verificando hierarquia de classes:\n")
    print(f"Guerreiro é um Jogador? {isinstance(guerreiro, Jogador)}")
    print(f"Mago é um Guerreiro? {isinstance(mago, Guerreiro)}")
    print(f"Tipo do Ladrao: {type(ladrao).__name__}")


if __name__ == "__main__":
    main()
