"""
Relações entre classes: associação, agregação e composição

Associação é um tipo de relação onde os objetos estão ligados dentro do sistema.

Essa é a relação mais comum entre objeto e tem subconjuntos como agregação e composição.
Geralmente, temos uma associação quando um objeto tem um atributo que referencia outro objeto.

A associação não especifica como um objeto controla o ciclo de vida de outro objeto

"""

class Escritor:
    def __init__(self, nome) -> None:
        self.nome = nome
        self._ferramenta = None

    @property
    def ferramenta(self):
        return self._ferramenta
    
    @ferramenta.setter
    def ferramenta(self, valor):
        self._ferramenta = valor

class FerramentaDeEscrever:
    def __init__(self, nome) -> None:
        self.nome = nome

    def escrever(self):
        return f'{self.nome} está escrevendo'
    

escritor = Escritor('Vinicius de Moraes')
caneta = FerramentaDeEscrever('Caneta')

escritor.ferramenta = caneta
print(escritor.ferramenta.escrever())
