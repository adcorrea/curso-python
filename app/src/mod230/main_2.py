# abstractmethod para qualquer método já decorado
# É possível criar @property @setter @classmethod @staticmethod e @method
# como abstratos, para isso use @abstractmethod como decorator mais interno.

# Foo - Bar são palavras usadas como placeholder
# para palavras que podem mudar na programação

from abc import ABC, abstractmethod


class AbstracFoo(ABC):
    def __init__(self, nome):
        self._name = None
        self.name = nome

    @property
    def name(self):
        return self._name
    
    @name.setter
    @abstractmethod
    def name(self, nome):...



class Foo(AbstracFoo):
    def __init__(self, nome):
        super().__init__(nome)
        print('Sou Inútil')



    @AbstracFoo.name.setter
    def name(self, nome):
        self._name = nome



if __name__ == '__main__':
    foo = Foo('Bar')

    print(foo.name)


