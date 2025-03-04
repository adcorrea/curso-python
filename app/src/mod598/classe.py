class Pessoa:
    def __init__(self, nome: str, sobrenome: str, idade: int) -> None:
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    def fala(self) -> None:
        print(f'{self.nome} {self.sobrenome} {self.idade}')



if __name__ == '__main__':
    pessoa = Pessoa('Antonio', 'Junior', 38)

    pessoa.fala()