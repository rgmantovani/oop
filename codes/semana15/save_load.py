"""
Semana 15: Sistema de Persistência com JSON
"""

import json
from pathlib import Path

class Jogador:
    def __init__(self, nome, nivel=1, hp=100, exp=0):
        self.nome = nome
        self.nivel = nivel
        self.hp = hp
        self.exp = exp
        self.inventario = []
    
    def to_dict(self):
        """Serializa jogador para dicionário"""
        return {
            'nome': self.nome,
            'nivel': self.nivel,
            'hp': self.hp,
            'exp': self.exp,
            'inventario': self.inventario,
            'versao': '1.0'
        }
    
    @classmethod
    def from_dict(cls, dados):
        """Desserializa jogador de dicionário"""
        j = cls(dados['nome'], dados['nivel'], dados['hp'], dados['exp'])
        j.inventario = dados.get('inventario', [])
        return j
    
    def __str__(self):
        return f"{self.nome} (Nv.{self.nivel}) HP:{self.hp} EXP:{self.exp}"

class SistemaDeArquivos:
    @staticmethod
    def salvar_jogo(jogador, arquivo="save.json"):
        """Salva estado do jogo em JSON"""
        dados = jogador.to_dict()
        with open(arquivo, 'w', encoding='utf-8') as f:
            json.dump(dados, f, indent=2, ensure_ascii=False)
        print(f"💾 Jogo salvo em {arquivo}")
    
    @staticmethod
    def carregar_jogo(arquivo="save.json"):
        """Carrega estado do jogo de JSON"""
        if not Path(arquivo).exists():
            print(f"❌ Arquivo {arquivo} não encontrado")
            return None
        
        with open(arquivo, 'r', encoding='utf-8') as f:
            dados = json.load(f)
        
        jogador = Jogador.from_dict(dados)
        print(f"📂 Jogo carregado de {arquivo}")
        return jogador

if __name__ == "__main__":
    # Criando e salvando
    j1 = Jogador("Arthur", nivel=10, hp=200, exp=1500)
    j1.inventario = ["Espada", "Escudo", "Poção"]
    print(f"Original: {j1}")
    
    SistemaDeArquivos.salvar_jogo(j1, "meu_save.json")
    
    # Carregando
    j2 = SistemaDeArquivos.carregar_jogo("meu_save.json")
    print(f"Carregado: {j2}")
    print(f"Inventário: {j2.inventario}")
