"""
############################## AULA 96 ##############################################
Formas de importação de módulo do python

=> Importa o módulo inteiro
import sys

=> Importa partes do módulo
from sys import exit

=> Da alias a um módulo
import sys as sistema

=> Da alias a funções
from sys import platform as pf


=> import todos os nomes do módulo
from sys import *

####################################################################################

Módulos padrão do Python (import, from, as e *)
https://docs.python.org/3/py-modindex.html

Inteiro - import nome_modulo
Vantagens: você tem o namspace do módulo
Desvantagens: nomes grandes
"""

# import sys
# sys.exit()

"""

partes - from nome_modulo import objeto1, objeto2
Vantagenes: nomes pequenos
Desvantagens? Sem o namaspace do módulo


"""

# from sys import exit, platform
# print(platform)


"""

alias 1 - import nome_modulo as apelido
alias 2 - import nome_modulo import objeto as apelido
Vantagens: voce pode reser nomes para seu código
Desvantagens: pode ficar fora do pardrão da linguagem


"""
# import sys as s
# print(s.platform)

# from sys import platform as pf
# print(pf)

"""

Má prática - from nome_modulo import *
Vantagens: importa tudo de um módulo
Desvantagens: importa tudo de um módulo

"""

from sys import *
print(platform)





 

