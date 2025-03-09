"""
@staticmethod (métodos estáticos)

Métodos estáticos são métodos que estão dentro da classe, mas não tem acesso
ao self nem ao cls.

m resumo, são funções que existem dentro da sua classe.

"""

class Classe:
    @staticmethod
    def funcao_que_esta_classe(*args, **kwargs):
        print('oi', args, kwargs)



Classe.funcao_que_esta_classe(1, 2, 3)

