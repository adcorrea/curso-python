# Escopo da classe e de métodos da Classe

class Animal:

    def __init__(self, nome) -> None:
        self.nome = nome

        variavel = 'valor'
        print(variavel)

    def comendo(self, alimento):
        return f'{self.nome} está comendo {alimento}'
    
    def executar(self, *args, **kwargs):
        return self.comendo(*args, **kwargs)
    

leao = Animal('Leão')
print(leao.comendo('Zebra'))
print(leao.executar('Zebra'))