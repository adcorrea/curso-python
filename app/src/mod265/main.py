# dataclasses - o que são dataclasses?

# O módulo dataclasses fornece um decorador e funçoes para cria métodos como 

# __init__(), __repr__(), __eq__() (entre outros) em classes definidas pelo usuário.

# Em resumo: dataclasses são syntax sugar para criar classes normais.
# Foi descrito na PEP 557 e adicionado na versão 3.7 do Python.

# doc: https://docs.python.org/library/dataclasses.html


from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    idade: int

    # def __repr__ (self):
    #     return f'{self.__class__.__name__}({self.__dict__})'

if __name__ == '__main__':
    obj = Pessoa('Junior', 38)

    print(obj == Pessoa('Junior', 38))
    print(obj)