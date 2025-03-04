"""
Métodos de classe + factories (fábricas)


São métodos onde "self" será "cls", ou seja, ao invés de receber a instância no primeiro parâmetro, receberemos a
própria classe.

"""

class Pessoa:
    ano = 2023 # atributo de classe

    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade


    @classmethod
    def metodo_de_classe(cls):
        print('Hey')

    @classmethod
    def pessoa_com_50(cls, nome):
       return cls(nome, 50)
    
    @classmethod
    def criar_sem_nome(cls, idade):
        return cls('Anonima', idade)

    


print(Pessoa.ano)
Pessoa.metodo_de_classe()

print(vars(Pessoa.pessoa_com_50('Joao')))