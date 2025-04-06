# Classes decoradoras (Decorator Classes)

# Para criar uma classe decoradora, é precisa implementar o dunder method __call__

class Multiplicador:
    def __init__(self, func):
        self.func = func

    # Para criar uma classe decoradora, é precisa implementar o dunder method __call__
    def __call__(self, *args, **kwds):
        print(args, kwds)
        return self.func(*args, **kwds)
    
@Multiplicador
def soma(x, y):
    return x + y


if __name__ == '__main__':
    resultado = soma(2, 4)
    print(resultado)