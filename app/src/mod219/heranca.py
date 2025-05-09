"""
Herança simple - Relações entre classes

Associação - usa
Agregação - tem 
Composição - É dono de
Herança - É um


Herança vs Composição

Classe principal (Pessoa)
    -> super class, base class, parent class

Classes filhas (Cliente)
    -> sub class, child class, derived class

"""

class Pessoa:
    def __init__(self, nome, sobrenome) -> None:
        self.nome = nome
        self.sobrenome = sobrenome

    def nome_classe(self):
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente(Pessoa):
    ...


class Aluno(Pessoa):
    ...

if __name__ == '__main__':
    c1 = Cliente('Luiz', 'Otavio')
    c1.nome_classe()

    c2 = Aluno('Maria', 'Helena')
    c2.nome_classe()
    help(Cliente)