"""
################### Aula 99 - __init__ ########################

como __init__ é possível transformar o package em módulo

__init__ é executado na importacao e pode ser usado para
realizar configurações do package.




"""


from sys import path

from package import soma, variavel2, hello_world



# from aula99_package.modulo import hello_world


print(soma(1,1))
print(variavel2)

#print(*path, sep='\n')

hello_world()
