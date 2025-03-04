""" 
Entendo self em classe Python

Classe - Molde (geralmente sem dados)
Instância da class (objeto) - Tem os dados

Uma classe pode gerar v´rias instâncias.
Na classe o self é a própria instância

"""

class Carro:
    
    # o primeiro parametro dos métodos é sempre a instancia da classe
    # self é um nome de convenção, mas pode ser qualquer nome
    def __init__(self, nome=None):
        self.nome = nome

    def acelerar(self):
        print(f'{self.nome} está acelerando!')

fusca = Carro('Fusca')
Carro.acelerar(fusca)

celta = Carro(nome='Celta')
celta.acelerar()