from abc import ABC, abstractmethod
from banco.excecoes import SaldoInsuficienteError

class Conta (ABC):

    def __init__(self, agencia: str, numero: str):
        self._agencia = agencia
        self._numero = numero
        self._saldo = 0.00

    @abstractmethod
    def sacar(self, valor: float) -> None:...


    @property
    def numero (self) -> str:
        return self._numero
    
    @property
    def agencia(self) -> str:
        return self._agencia
    
    @property
    def saldo(self) -> float:
        return self._saldo
    
    @numero.setter
    def conta(self, numero: str) -> None:
        self._numero = numero

    @agencia.setter
    def agencia(self, agencia: str) -> None:
        self._agencia = agencia

    def depositar(self, valor: float) -> None:
        print(f'Depositando {valor}...')
        self._saldo += valor
        print(f'Deposito concluído!')
        self.mostrar_saldo()
    
    def mostrar_saldo(self) -> None:
        print(f'--------> Saldo: {self.saldo}')




class ContaCorrente(Conta):

    def __init__(self, agencia: str, conta: str, limite_extra: float = 0.00):
        super().__init__(agencia, conta)
        self._limite_extra = limite_extra

    @property
    def limite_extra(self) -> float:
        return self._limite_extra
    
    @limite_extra.setter
    def limite_extra(self, valor: float) -> None:
        self._limite_extra = valor

    def sacar(self, valor: float) -> None:
        print(f'Sacando {valor}...')
        if valor > (self._saldo + self._limite_extra):
            print('Não foi possível realizar o saque...')
            raise SaldoInsuficienteError('Saldo Insuficiente!')
        
        self._saldo -= valor
        print('Saque concluído!')
        self.mostrar_saldo()


class ContaPoupança(Conta):

    def sacar(self, valor: float) -> None:
        print(f'Sacando {valor}...')
        if valor > self._saldo:
            print('Não foi possível realizar o saque...')
            raise SaldoInsuficienteError('Saldo Insuficiente!') 
        self._saldo -= valor
        print('Saque concluído!')
        self.mostrar_saldo()


    