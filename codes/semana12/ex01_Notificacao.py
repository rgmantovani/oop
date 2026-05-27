from abc import ABC, abstractmethod

# Produto abstrato
class Notificacao(ABC):

    @abstractmethod
    def enviar(self, mensagem):
        pass


# Produtos concretos
class Email(Notificacao):

    def enviar(self, mensagem):
        print(f"[EMAIL] {mensagem}")


class SMS(Notificacao):

    def enviar(self, mensagem):
        print(f"[SMS] {mensagem}")


class Push(Notificacao):

    def enviar(self, mensagem):
        print(f"[PUSH] {mensagem}")


# Factory Method
class FabricaNotificacao:

    @staticmethod
    def criar_notificacao(tipo):

        if tipo == "email":
            return Email()

        elif tipo == "sms":
            return SMS()

        elif tipo == "push":
            return Push()

        else:
            raise ValueError("Tipo inválido")


# Programa principal
tipo = input("Digite o tipo (email/sms/push): ")

notificacao = FabricaNotificacao.criar_notificacao(tipo)

notificacao.enviar("Bem-vindo ao sistema!")