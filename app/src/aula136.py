"""
Relações entre classes: associação, agregação e composição

composição é uma espcializada da agregação.
Mas nela, quando o objeto "pai" for apagado, todas as referencias dos objetos filhos também
são apagados.

"""

class Cliente:
    def __init__(self, nome) -> None:
        self.nome = nome
        self.enderecos = []

    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero))

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def __del__(self):
        print(f'apagando cliente {self.nome}')


class Endereco:
    def __init__(self, rua, numero) -> None:
        self.rua = rua
        self.numero = numero

    def __del__(self):
        print(f'apagando endereco {self.rua} {self.numero}')

cliente = Cliente('Maria')
cliente.inserir_endereco('Rua 01', '01')
cliente.inserir_endereco('Rua 02', '01')
cliente.listar_enderecos()

endereco = Endereco('Avenida', '1000')

del cliente

print('#### Acabou o programa #####')