# __dict__ e vars para atributos de instância

class Pessoa:
    ano_atual = 2022

    def __init__(self, nome, idade) -> None:
        self.nome = nome
        self.idade = idade

    def get_ano_nascimento(self):
        return self.ano_atual - self.idade
    

p1 = Pessoa('Joao', 35)

print(p1.get_ano_nascimento())
print(p1.__dict__)
print(vars(p1))

p1.__dict__['nome'] = 'Joana'
print(vars(p1))

dados = {'nome': 'Junior', 'idade': 38}
obj = Pessoa(**dados)
print(vars(obj))
    