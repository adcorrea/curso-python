from banco.pessoa import Cliente
from banco.excecoes import AutenticacaoErro

class Banco:

    def __init__(self, nome: str):
        self._nome_banco = nome
        self._clientes = []


    @property
    def nome_banco(self) -> str:
        return self._nome_banco
    
    def listar_clientes(self) -> None:
        print(f'Mostrando clientes de {self.nome_banco}')
        for cliente in self._clientes:
            print(f'Cliente: {cliente.nome}')
            cliente.conta.mostrar_saldo()
    
    def incluir_cliente(self, cliente: Cliente) -> None:
        if not isinstance(cliente, Cliente):
            raise TypeError('Tipo não é um cliente!')
        
        self._clientes.append(cliente)


    def autenticar(self, agencia: str, numero: str, cpf: str) -> Cliente|None:
        for cliente in self._clientes:
            if cliente.cpf == cpf:
                if cliente.conta.agencia == agencia and cliente.conta.numero == numero:
                    print(f'{cliente.nome} autenticado!')
                    return(cliente)
                
        raise AutenticacaoErro(f'Credenciais inválidas!')

    