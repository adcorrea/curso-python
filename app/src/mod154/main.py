import sys
import os


"""
Adicionando a pasta raiz do projeto no path do módulo __main__

"""
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))


# Entendendo cada trecho do comando cima.

print(__file__)
print(os.path.dirname(__file__))
print(os.path.join(os.path.dirname(__file__), '../../..'))
print(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..')))


#print(*sys.path, sep='\n')


# agora é possível importar módulo fora da pasta do __main__
from app.src.utils.modulo import hello

hello()


