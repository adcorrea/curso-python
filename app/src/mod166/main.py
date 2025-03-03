"""
Funções decoradoras e decoradores 
Decorar = Adiconar/remover/retringir/Alterar

F?unç~eos decoradoras são funçõe que decoram outra funções

Decoradores são usado para fazer o Python usar as funções decoradoras em outras funções

Decoradores são "Syntax Sugar" (Açúcar Sintático)

"""

def criar_funcao(func):
    def interna(*args, **kwargs):
        for arg in args:
            e_string(arg)
        resultado = func(*args, **kwargs)

        return resultado 
    return interna


@criar_funcao
def inverte_string(string):
    return string[::-1]


def e_string(param):
    if not isinstance(param, str):
        raise TypeError('param deve ser uma string')



invertida = inverte_string('123')
print(invertida)