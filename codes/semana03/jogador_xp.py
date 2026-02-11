"""
Semana 3: Construtores, Destrutores e Métodos Especiais
Exemplo: Sistema de experiência e progressão de nível

Conceitos abordados:
- Construtores com parâmetros default
- Métodos de classe (@classmethod)
- Métodos estáticos (@staticmethod)
- Métodos especiais (__repr__, __eq__, __lt__)
"""


class Jogador:
    """Jogador com sistema de progressão"""
    
    # Constante de classe
    XP_POR_NIVEL = 100
    
    def __init__(self, nome, nivel=1, hp=100, exp=0):
        self._nome = nome
        self._nivel = nivel
        self._hp_maximo = hp
        self._hp = hp
        self._exp = exp
        self._exp_proximo_nivel = self.calcular_exp_necessaria(nivel)
    
    # ========================================
    # Métodos de Classe (Construtores Alternativos)
    # ========================================
    
    @classmethod
    def criar_jogador_iniciante(cls, nome):
        """Cria um jogador iniciante com valores padrão"""
        return cls(nome, nivel=1, hp=100, exp=0)
    
    @classmethod
    def criar_jogador_veterano(cls, nome):
        """Cria um jogador veterano de nível alto"""
        return cls(nome, nivel=10, hp=250, exp=0)
    
    @classmethod
    def criar_do_save(cls, dados):
        """Reconstrói jogador a partir de dados salvos"""
        return cls(
            nome=dados['nome'],
            nivel=dados['nivel'],
            hp=dados['hp_maximo'],
            exp=dados['exp']
        )
    
    # ========================================
    # Métodos Estáticos
    # ========================================
    
    @staticmethod
    def calcular_exp_necessaria(nivel):
        """Calcula XP necessária para alcançar o próximo nível"""
        return Jogador.XP_POR_NIVEL * nivel
    
    @staticmethod
    def validar_nome(nome):
        """Valida se o nome é aceitável"""
        return nome and len(nome.strip()) >= 3 and len(nome) <= 20
    
    # ========================================
    # Sistema de Experiência
    # ========================================
    
    @property
    def exp(self):
        return self._exp
    
    def ganhar_exp(self, quantidade):
        """Adiciona experiência e verifica subida de nível"""
        if quantidade < 0:
            raise ValueError("Experiência não pode ser negativa")
        
        self._exp += quantidade
        print(f"⭐ {self._nome} ganhou {quantidade} XP! (Total: {self._exp})")
        
        # Verifica subidas de nível
        while self._exp >= self._exp_proximo_nivel:
            self._subir_nivel()
    
    def _subir_nivel(self):
        """Aumenta o nível do jogador (método privado)"""
        self._nivel += 1
        self._exp -= self._exp_proximo_nivel
        self._exp_proximo_nivel = self.calcular_exp_necessaria(self._nivel)
        
        # Aumenta atributos
        bonus_hp = 20
        self._hp_maximo += bonus_hp
        self._hp = self._hp_maximo
        
        print(f"\n🎉 LEVEL UP! {self._nome} subiu para o nível {self._nivel}!")
        print(f"   HP máximo aumentou em {bonus_hp} ({self._hp_maximo})")
        print(f"   XP para próximo nível: {self._exp_proximo_nivel}\n")
    
    # ========================================
    # Métodos Especiais
    # ========================================
    
    def __repr__(self):
        """Representação técnica para debugging"""
        return (f"Jogador(nome='{self._nome}', nivel={self._nivel}, "
                f"hp={self._hp_maximo}, exp={self._exp})")
    
    def __str__(self):
        """Representação amigável"""
        return (f"{self._nome} - Nível {self._nivel} "
                f"[HP: {self._hp}/{self._hp_maximo}] "
                f"[XP: {self._exp}/{self._exp_proximo_nivel}]")
    
    def __eq__(self, outro):
        """Compara se dois jogadores são iguais (mesmo nome)"""
        if not isinstance(outro, Jogador):
            return False
        return self._nome == outro._nome
    
    def __lt__(self, outro):
        """Compara jogadores por nível (para ordenação)"""
        if not isinstance(outro, Jogador):
            return NotImplemented
        return self._nivel < outro._nivel
    
    def __del__(self):
        """Destrutor - chamado quando o objeto é destruído"""
        print(f"🗑️  Jogador {self._nome} foi removido da memória")
    
    # ========================================
    # Métodos Regulares
    # ========================================
    
    @property
    def nome(self):
        return self._nome
    
    @property
    def nivel(self):
        return self._nivel
    
    def to_dict(self):
        """Converte jogador para dicionário (útil para salvar)"""
        return {
            'nome': self._nome,
            'nivel': self._nivel,
            'hp_maximo': self._hp_maximo,
            'exp': self._exp
        }


# ============================================
# Programa de Teste
# ============================================

def main():
    print("=" * 70)
    print("SEMANA 3: Construtores, Métodos Especiais e Sistema de XP")
    print("=" * 70)
    print()
    
    # Testando diferentes construtores
    print(">>> Criando jogadores com diferentes construtores:\n")
    
    j1 = Jogador("Arthur", nivel=5, hp=150)
    j2 = Jogador.criar_jogador_iniciante("Lancelot")
    j3 = Jogador.criar_jogador_veterano("Merlin")
    
    print(f"j1: {j1}")
    print(f"j2: {j2}")
    print(f"j3: {j3}")
    print()
    
    # Testando __repr__
    print(f"repr(j1): {repr(j1)}\n")
    
    # Testando sistema de XP
    print(">>> Testando sistema de experiência:\n")
    j2.ganhar_exp(50)
    j2.ganhar_exp(60)  # Deve subir de nível
    j2.ganhar_exp(150)  # Deve subir múltiplos níveis
    print(j2)
    print()
    
    # Testando comparações
    print(">>> Testando operadores de comparação:\n")
    jogadores = [j1, j2, j3]
    print("Antes de ordenar:", [j.nome for j in jogadores])
    jogadores.sort()
    print("Depois de ordenar por nível:", [f"{j.nome}(Nv.{j.nivel})" for j in jogadores])
    print()
    
    # Testando igualdade
    j4 = Jogador("Arthur", nivel=1)  # Mesmo nome que j1
    print(f"{j1.nome} == {j4.nome}? {j1 == j4}")
    print()
    
    # Testando save/load
    print(">>> Testando serialização:\n")
    dados_salvos = j2.to_dict()
    print(f"Dados salvos: {dados_salvos}")
    
    j_carregado = Jogador.criar_do_save(dados_salvos)
    print(f"Jogador carregado: {j_carregado}")
    print()
    
    # Testando validação estática
    print(">>> Testando validação de nome:\n")
    nomes = ["Jo", "Arthur", "Um Nome Muito Longo Demais Para Ser Aceito"]
    for nome in nomes:
        valido = Jogador.validar_nome(nome)
        print(f"'{nome}' é válido? {valido}")


if __name__ == "__main__":
    main()
    print("\n>>> Destrutor será chamado ao sair do programa...\n")
