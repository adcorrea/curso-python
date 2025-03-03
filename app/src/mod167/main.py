# Decoradores com parâmetros


def fabrica_de_decoradores(a = None, b = None, c = None):
    def fabrica_de_funcoes(func):
        print('Decoradora 1')

        def aninhada(*args, **kwargs):
            print('Aninhada')
            res = func(*args, **kwargs)
            return res
        return aninhada
    return fabrica_de_funcoes


# Ao usar o decorador na função, a função decoradora ja é executada
@fabrica_de_decoradores(1, 2, 3)
def soma(x, y):
    return x + y

multiplica = fabrica_de_decoradores()(lambda x, y: x * y)

# Executando a função, o comando aplicado na inner function aninhada é executado
var = multiplica(2, 5)
print(var)


acm = soma(10, 5)
print(acm)