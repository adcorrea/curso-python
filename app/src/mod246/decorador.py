# Classes decoradoras (Decorator Classes)

class Multiplicador:
    def __init__(self, func):
        self.func = func
        self._multiplicador = 10


    # Para criar uma classe decoradora, é precisa implementar o dunder method __call__
    def __call__(self, *args, **kwds):

        # o método deve retornar a função após a aplicação do
        # código desejado
        resultado = self.func(*args, **kwds)

        # No caso, o retorno do call é o resultado multiplicado por _multiplicador
        return resultado * self._multiplicador
    
@Multiplicador
def soma(x, y):
    return x + y


if __name__ == '__main__':
    resultado = soma(2, 4)
    print(resultado)