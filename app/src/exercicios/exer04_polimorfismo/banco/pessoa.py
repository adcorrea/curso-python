from banco.conta import Conta


class Pessoa:
    def __init__(self, nome: str, cpf: str, idade: int):
        self._nome = nome
        self._cpf = cpf
        self._idade = idade        


    @property
    def nome (self) -> str:
        return self._nome
    
    @property
    def cpf (self) -> str:
        return self._cpf
    
    @property
    def idade(self) -> int:
        return self._idade


class Cliente (Pessoa):
    def __init__(self, nome: str, cpf: str, idade: int):
        super().__init__(nome, cpf, idade)

        self._conta = None

    def abrir_conta(self, conta: Conta) -> None:
        if not isinstance(conta, Conta):
            raise TypeError('Tipo não é conta.')
        
        self._conta = conta



    @property
    def conta(self) -> Conta:
        return self._conta

    