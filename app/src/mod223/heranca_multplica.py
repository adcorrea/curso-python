# Herança Múltipla - Python Orientada a Objetos

# Quer dizer que no Python, uma classe pode estender
# várias outras classe.

# Herança simples:
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente

# Herança múltipla e mixins
# Log -> FileLog
# Animal -> Mamifero -> Humano -> Pessoa -> Cliente
# Cliente(Pessoa, FileLog)


# Python 3 usa C3 superclasse linearization
# para gerar o mro.
# https://en.wikipedia.org/wiki/C3_linearization

# Para saber a ordem de chamada dos métodos
# Use o método de calsse Classe.mro()
# Ou o atributo __mro__ (Dunder - Double underscore)