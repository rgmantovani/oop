"""
Semana 6: Composição - Sistema de Raças
"""

class Raca:
    def __init__(self, nome, bonus_forca=0, bonus_inteligencia=0, bonus_agilidade=0):
        self.nome = nome
        self.bonus_forca = bonus_forca
        self.bonus_inteligencia = bonus_inteligencia
        self.bonus_agilidade = bonus_agilidade

class Humano(Raca):
    def __init__(self):
        super().__init__("Humano", bonus_forca=2, bonus_inteligencia=2, bonus_agilidade=2)

class Elfo(Raca):
    def __init__(self):
        super().__init__("Elfo", bonus_agilidade=5, bonus_inteligencia=3)

class Orc(Raca):
    def __init__(self):
        super().__init__("Orc", bonus_forca=6, bonus_agilidade=-2)

class Jogador:
    def __init__(self, nome, raca, forca_base=10):
        self.nome = nome
        self.raca = raca  # Composição
        self.forca_base = forca_base
    
    @property
    def forca_total(self):
        return self.forca_base + self.raca.bonus_forca
    
    def __str__(self):
        return f"{self.nome} ({self.raca.nome}) - Força: {self.forca_total}"

if __name__ == "__main__":
    j1 = Jogador("Aragorn", Humano())
    j2 = Jogador("Legolas", Elfo())
    j3 = Jogador("Thrall", Orc())
    
    for j in [j1, j2, j3]:
        print(j)
