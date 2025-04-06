# Classes decoradoras (Decorator Classes)

class Multiplicador:
    def __init__(self, multiplicador):
        self._multiplicador = multiplicador


    # Para criar uma classe decoradora, é precisa implementar o dunder method __call__
    def __call__(self, func):

        # o método deve retornar a função após a aplicação do
        # código desejado
        def interna(*args, **kwds):
            resultado = func(*args, **kwds)

            # No caso, o retorno do call é o resultado multiplicado por _multiplicador
            return resultado * self._multiplicador
        
        return interna
    
@Multiplicador(10)
def soma(x, y):
    return x + y


if __name__ == '__main__':
    resultado = soma(2, 4)
    print(resultado)