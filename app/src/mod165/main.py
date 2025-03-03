"""
Funções decoradoras e decoradores 
Decorar = Adiconar/remover/retringir/Alterar

Funções decoradoras são funções que decoram outra funções

Decoradores são usado para fazer o Python usar as funções decoradoras em outras funções

"""


def criar_funcao(func):
    def interna(*args, **kwargs):
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)

        return resultado 
    return interna

def inverte_string(string):
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')


check_param = criar_funcao(inverte_string)
invertida = check_param('Junior')
print(invertida)