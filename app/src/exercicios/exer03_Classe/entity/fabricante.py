
class Fabricante:

    def __init__(self, nome):
        self.nome = nome
        self.__carros = []


    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def carros(self):
        return self.__carros
    
    def inserir_carro(self, *args):
        for carro in args:
            self.__carros.append(carro)

    def listar_carros(self):
        print(f'Carros do fabrincante {self.nome}')
        for carro in self.carros:
            print(f'Carro {carro.nome} com motor {carro.motor.nome}')