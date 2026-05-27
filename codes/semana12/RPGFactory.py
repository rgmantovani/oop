from abc import ABC, abstractmethod

# Produto abstrato
class Personagem(ABC):

    @abstractmethod
    def atacar(self):
        pass


# Produtos concretos
class Guerreiro(Personagem):

    def atacar(self):
        print("Guerreiro atacou com espada!")


class Mago(Personagem):

    def atacar(self):
        print("Mago lançou uma bola de fogo!")


class Arqueiro(Personagem):

    def atacar(self):
        print("Arqueiro disparou uma flecha!")


# Factory
class FabricaPersonagem:

    @staticmethod
    def criar_personagem(tipo):

        if tipo == "guerreiro":
            return Guerreiro()

        elif tipo == "mago":
            return Mago()

        elif tipo == "arqueiro":
            return Arqueiro()

        else:
            raise ValueError("Classe inválida")


# Programa principal
tipo = input("Escolha o personagem: ")

personagem = FabricaPersonagem.criar_personagem(tipo)

personagem.atacar()