from abc import ABC, abstractmethod

# Produto abstrato
class Transporte(ABC):

    @abstractmethod
    def viajar(self):
        pass


# Produtos concretos
class Onibus(Transporte):

    def viajar(self):
        print("Ônibus realizando rota urbana.")


class Taxi(Transporte):

    def viajar(self):
        print("Táxi transportando passageiro.")


class Bicicleta(Transporte):

    def viajar(self):
        print("Bicicleta compartilhada iniciando trajeto.")


# Factory Method
class FabricaTransporte:

    @staticmethod
    def criar_transporte(tipo):

        if tipo == "onibus":
            return Onibus()

        elif tipo == "taxi":
            return Taxi()

        elif tipo == "bicicleta":
            return Bicicleta()

        else:
            raise ValueError("Tipo de transporte inválido")


# Programa principal
tipo = input("Escolha o transporte: ")

transporte = FabricaTransporte.criar_transporte(tipo)

transporte.viajar()