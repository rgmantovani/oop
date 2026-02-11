"""
Semana 2: Encapsulamento e Validação de Dados
Exemplo: Classe Jogador com encapsulamento em Python

Conceitos abordados:
- Atributos privados (convenção _)
- Propriedades (@property)
- Getters e Setters
- Validação de dados
- Método __str__
"""


class Jogador:
    """Representa um jogador no sistema de RPG com encapsulamento"""
    
    def __init__(self, nome, nivel=1, hp=100):
        """Inicializa um novo jogador"""
        self._nome = nome
        self._nivel = nivel
        self._hp_maximo = hp
        self._hp = hp
    
    # ========================================
    # Propriedades (Getters e Setters)
    # ========================================
    
    @property
    def nome(self):
        """Retorna o nome do jogador"""
        return self._nome
    
    @nome.setter
    def nome(self, valor):
        """Define o nome do jogador com validação"""
        if not valor or len(valor.strip()) == 0:
            raise ValueError("Nome não pode ser vazio")
        self._nome = valor.strip()
    
    @property
    def nivel(self):
        """Retorna o nível do jogador"""
        return self._nivel
    
    @nivel.setter
    def nivel(self, valor):
        """Define o nível com validação"""
        if valor < 1:
            raise ValueError("Nível não pode ser menor que 1")
        if valor > 100:
            raise ValueError("Nível máximo é 100")
        self._nivel = valor
    
    @property
    def hp(self):
        """Retorna HP atual"""
        return self._hp
    
    @hp.setter
    def hp(self, valor):
        """Define HP com validação (não pode exceder máximo)"""
        if valor < 0:
            self._hp = 0
        elif valor > self._hp_maximo:
            self._hp = self._hp_maximo
        else:
            self._hp = valor
    
    @property
    def hp_maximo(self):
        """Retorna HP máximo"""
        return self._hp_maximo
    
    @hp_maximo.setter
    def hp_maximo(self, valor):
        """Define HP máximo com validação"""
        if valor < 1:
            raise ValueError("HP máximo deve ser positivo")
        self._hp_maximo = valor
        # Ajusta HP atual se necessário
        if self._hp > self._hp_maximo:
            self._hp = self._hp_maximo
    
    # ========================================
    # Métodos Públicos
    # ========================================
    
    def receber_dano(self, dano):
        """
        Aplica dano ao jogador com validação
        
        Args:
            dano: Quantidade de dano (deve ser positivo)
        """
        if dano < 0:
            raise ValueError("Dano não pode ser negativo")
        
        self.hp -= dano  # Usa o setter para validação automática
        print(f"{self.nome} recebeu {dano} de dano! HP: {self.hp}/{self.hp_maximo}")
        
        if self.hp == 0:
            print(f"💀 {self.nome} foi derrotado!")
    
    def curar(self, quantidade):
        """
        Cura o jogador com validação
        
        Args:
            quantidade: Quantidade de HP a recuperar (deve ser positivo)
        """
        if quantidade < 0:
            raise ValueError("Cura não pode ser negativa")
        
        hp_anterior = self.hp
        self.hp += quantidade  # Usa o setter para validação automática
        hp_recuperado = self.hp - hp_anterior
        
        print(f"❤️  {self.nome} recuperou {hp_recuperado} HP! HP: {self.hp}/{self.hp_maximo}")
    
    def esta_vivo(self):
        """Verifica se o jogador está vivo"""
        return self.hp > 0
    
    def exibir_status(self):
        """Exibe o status do jogador"""
        print(self)
    
    # ========================================
    # Métodos Especiais
    # ========================================
    
    def __str__(self):
        """Representação em string do jogador"""
        status = "VIVO" if self.esta_vivo() else "MORTO"
        barra_hp = self._criar_barra_hp()
        
        return f"""
╔════════════════════════════════════════╗
║       STATUS DO JOGADOR                ║
╠════════════════════════════════════════╣
║ Nome:   {self.nome:<30} ║
║ Nível:  {self.nivel:<30} ║
║ Status: {status:<30} ║
║ HP:     {barra_hp}
╚════════════════════════════════════════╝
"""
    
    def _criar_barra_hp(self):
        """Cria uma barra visual de HP (método privado)"""
        percentual = (self.hp / self.hp_maximo) * 100
        barras_cheias = int(percentual / 10)
        barras_vazias = 10 - barras_cheias
        
        barra = "█" * barras_cheias + "░" * barras_vazias
        return f"[{barra}] {self.hp}/{self.hp_maximo}"


# ============================================
# Programa de Teste
# ============================================

def main():
    print("=" * 60)
    print("SEMANA 2: Encapsulamento e Validação de Dados")
    print("=" * 60)
    print()
    
    # Criando jogador
    jogador = Jogador("Thorin", nivel=10, hp=200)
    jogador.exibir_status()
    
    # Testando validações
    print("\n>>> Testando validações:\n")
    
    try:
        jogador.nivel = -5  # Deve gerar erro
    except ValueError as e:
        print(f"❌ Erro capturado: {e}")
    
    try:
        jogador.nome = ""  # Deve gerar erro
    except ValueError as e:
        print(f"❌ Erro capturado: {e}")
    
    try:
        jogador.receber_dano(-10)  # Deve gerar erro
    except ValueError as e:
        print(f"❌ Erro capturado: {e}")
    
    # Testando HP com validação automática
    print("\n>>> Testando controle de HP:\n")
    jogador.receber_dano(50)
    jogador.curar(30)
    jogador.curar(200)  # Tenta curar além do máximo (é limitado automaticamente)
    
    jogador.exibir_status()
    
    # Testando dano fatal
    print("\n>>> Testando dano fatal:\n")
    jogador.receber_dano(300)
    jogador.exibir_status()
    
    # Tentando curar jogador morto
    print("\n>>> Tentando curar jogador morto:\n")
    jogador.curar(50)
    jogador.exibir_status()


if __name__ == "__main__":
    main()
