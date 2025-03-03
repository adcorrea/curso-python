
"""
### AULA 98: Recarregando módulos

"""

import importlib

import modulo


print(modulo.variavel)


for i in range(10):
    
    importlib.reload(modulo)
    print(i)

print('fim')