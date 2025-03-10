"""

Encapsulamento (modificadores de acesso: public, _protected, __private)

Python NÃO tem modificadores de acesso

Mas podemos seguir as seguintes convenções
    (sem underline) == public
        pode ser usado em qualquer lugar

    _ (um underline) = protected
        não DEVE ser usado fora da classe ou suas subclasses

    __ (dois underlines) = private
        "name magling" (desconfiguração de nomes) em Python
        só DEVE ser usado na classe em que foi declarado.

"""


class Foo:

    def __init__(self) -> None:
        self.publico = 'isso é publico'
        self._protected = 'isso é protegido'
        self.__private = 'isso é privado'

    def metodo_publico(self):
        return 'metodo_publico'
    
    def _metodo_protected(self):
        return '_metodo_protected'
    
    def __metodo_private(self):
        return '__metodo_private'

if __name__ == '__main__':
    f = Foo()
    print(f._protected)
    print(f._Foo__metodo_private())