# Polimorfismo em Python Orientado a Objetos

# Polimorfismo é o princípio que permite que
# classes derivadas de uma mesma superclasse tenham método iguais
# (com mesma assinatura) mas comportamentos diferentes.

# Assinatura de método = Mesmo nome e quantidade de parâmetros
# (retorno não faz parte da assinatura)

# Opnião + princípios que contam:
# Assinatura do método: nome, parâmetros e retorno iguais SO"L"ID

# Princípio de substituição de liskov
# Objetos de uma superclasse devem ser substituíveis por objetos
# de uma subclasse sem quebrar a aplicação.

# Sobrecarga de métodos (overload) - Não existe em python!
# Sobreposição de métodos (override)

from abc import ABC, abstractmethod

class Notificacao(ABC):
    def __init__(self, mensagem) -> None:
        self.mensagem = mensagem

    @abstractmethod
    def enviar(self) -> bool: ...

class NotificacaoEmail(Notificacao):
    def enviar(self):
        print('Email enviado - ', self.mensagem)

class NotificacaoSMS(Notificacao):
    def enviar(self):
        print('SMS enviado - ', self.mensagem)



def notificar(notificacao: Notificacao):
    notificacao.enviar()

if __name__ == '__main__':
    n = NotificacaoEmail('Hello World')
    notificar(n)

    n_2 = NotificacaoSMS('Hello World')
    notificar(n_2)