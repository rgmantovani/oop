"""
Semana 1: Introdução à POO e Primeira Classe
Exemplo: Classe Jogador básica em Python

Conceitos abordados:
- Definição de classe
- Atributos de instância
- Métodos
- Método __init__ (construtor)
"""


class Jogador:
    """Representa um jogador no sistema de RPG"""
    
    def __init__(self, nome, nivel=1, hp=100):
        """
        Inicializa um novo jogador
        
        Args:
            nome: Nome do jogador
            nivel: Nível inicial (padrão: 1)
            hp: Pontos de vida iniciais (padrão: 100)
        """
        self.nome = nome
        self.nivel = nivel
        self.hp = hp
        self.hp_maximo = hp
    
    def exibir_status(self):
        """Exibe o status atual do jogador"""
        print(f"=== Status do Jogador ===")
        print(f"Nome: {self.nome}")
        print(f"Nível: {self.nivel}")
        print(f"HP: {self.hp}/{self.hp_maximo}")
        print("=" * 25)
    
    def esta_vivo(self):
        """
        Verifica se o jogador ainda está vivo
        
        Returns:
            bool: True se HP > 0, False caso contrário
        """
        return self.hp > 0
    
    def receber_dano(self, dano):
        """
        Aplica dano ao jogador
        
        Args:
            dano: Quantidade de dano a receber
        """
        self.hp -= dano
        if self.hp < 0:
            self.hp = 0
        print(f"{self.nome} recebeu {dano} de dano!")
        
    def curar(self, quantidade):
        """
        Cura o jogador
        
        Args:
            quantidade: Quantidade de HP a recuperar
        """
        self.hp += quantidade
        if self.hp > self.hp_maximo:
            self.hp = self.hp_maximo
        print(f"{self.nome} recuperou {quantidade} HP!")


# ============================================
# Programa de Teste
# ============================================

def main():
    print("=" * 50)
    print("SEMANA 1: Classe Jogador Básica")
    print("=" * 50)
    print()
    
    # Criando jogadores
    jogador1 = Jogador("Aragorn", nivel=5, hp=150)
    jogador2 = Jogador("Legolas", nivel=4, hp=120)
    jogador3 = Jogador("Gandalf")  # Usando valores padrão
    
    # Exibindo status inicial
    print(">>> Jogadores criados:\n")
    jogador1.exibir_status()
    print()
    jogador2.exibir_status()
    print()
    jogador3.exibir_status()
    print()
    
    # Testando métodos
    print(">>> Testando combate:\n")
    jogador1.receber_dano(30)
    jogador1.exibir_status()
    print()
    
    print(f"{jogador1.nome} está vivo? {jogador1.esta_vivo()}")
    print()
    
    jogador1.curar(20)
    jogador1.exibir_status()
    print()
    
    # Simulando morte
    print(">>> Simulando dano fatal:\n")
    jogador2.receber_dano(200)
    jogador2.exibir_status()
    print(f"{jogador2.nome} está vivo? {jogador2.esta_vivo()}")
    print()


if __name__ == "__main__":
    main()
