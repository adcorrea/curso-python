"""
### AULA 97: Entendendo os seus prórpios módulos Python

O primeiro módulo executado chama-se __main__
Você pode importar outro módulo inteiro ou parte

O Python conhece a pasta onde o __main__ está e abaixo dele.

Ele não reconhece pastas e módulos acima do __main__ por padrão.

O python conhece todos os módulos e pacotes presentes nos caminhos de sys.path

"""



import sys

import modulo

from modulo import variavel, soma

print('Modulo: ', __name__)
print(*sys.path, sep='\n')

print(variavel)
print(soma(1,1))