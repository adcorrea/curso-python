# Metaclasses são o tipo das classes

# EM PYTHON, TUDO É UM OBJETO (CLASSES TAMBÉM)

# Então, qual é o tipo de uma classe? (type)
# Seu objeto é uma instância da sua classe.

# Sua classe ´uma instância de type (type é uma metaclass)
# type('Name', (Bases, ), __dict__)


# Ao criar uma classe, coisas ocorrem por padrão nessa ordem:
#     __new__ da metaclass é chamado e cria a nova classe
#     __call__ da metaclass é chamado com os argumentos e chama:
#         __new__ da classe com os argumentos (cria a instância)
#         __init__ da class com os argumentos
#     __call__ da metaclasse termina a execução

# Métodos importantes da metaclass
# __new__ (mcs, name, bases, dct) (Cria a classe)
# __call__ (cls, *args, **kwargs) (Cria e inicializa a instância)

# "Metaclasses são magias mais profundas do que 99% dos usuários deveriam
# se preocupar. Se você quer saber se precisa delas, não precisa (as pessoas
# que realmente precisam delas sabem com certeza que precisam delas e não precisam
# de uma explicação sobre o porquê)."
#     - tim Peters (CPython Core Developer)