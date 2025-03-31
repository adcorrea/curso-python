# Funções decoradoreas e decoradores com classes

def adiciona_repr(cls):
    def meu_repr(self):
        class_name = self.__class__.__name__
        class_dict = self.__dict__
        class_repr = f'{class_name}({class_dict})'
        return class_repr
    
    cls.__repr__ = meu_repr
    return cls

@adiciona_repr
class Time:
    def __init__(self, nome):
        self.nome = nome

   
@adiciona_repr
class Planeta:
    def __init__(self, nome):
        self.nome = nome


if __name__ == '__main__':
    
    brasil = Time('Brasil')
    portugal = Time('Portugal')
    print(brasil)
    print(portugal)

    terra = Planeta('Terra')
    marte = Planeta('Marte')
    print(terra)
    print(marte)