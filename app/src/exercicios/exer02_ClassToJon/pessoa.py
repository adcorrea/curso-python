# Salve sua classe em em Json
# Salve usa classe em Json e depois crie novamente as intancias da classe com os dados
# salvos.

# Faça em arquivos separados.

import json
import os

class Pessoa:
    PATH_TOJSON = f'{os.path.abspath(os.path.dirname(__file__))}/pessoa.json'
    PATH_FROMJSON = f'{os.path.abspath(os.path.dirname(__file__))}/carga.json'

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def toJson(self):
        with open (self.PATH_TOJSON, 'w', encoding='utf8') as arquivo:
            json.dump(vars(self), arquivo, ensure_ascii=False, indent=2)

    @classmethod
    def fromJson(cls):
        with open(cls.PATH_FROMJSON, 'r', encoding='utf8') as arquivo:
            pessoa = json.load(arquivo)
            return cls(pessoa['nome'], pessoa['idade'])


if __name__ == '__main__':
    oPessoa = Pessoa('Junior', 38)
    oPessoa.toJson()

    instacia_P = Pessoa.fromJson()

    print(vars(instacia_P))