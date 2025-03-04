"""
@property - um getter no modo Pythonico

getter - um método para obter um atributo modo pythonico - modo Pythonico de fazer
as coisas.

@property é uma propriedade do objeto, ela é um método que se comporta como um
atributo.

Geralmente é usada nas seguintes situações:
    - como getter
    - p/ envitar quebrar código cliente
    - p/ habiliter setter
    - p/ executar ações ao obter um atributo

"""

class Caneta:
    def __init__(self, cor) -> None:
        #atributos com _ ou __ não devem ser utilizados.
        self._cor = cor

    def get_cor(self):
        return self.cor
    
    @property
    def cor(self):
        return self._cor
    
    @cor.setter
    def cor(self, valor):
       self._cor = valor
    

    

caneta = Caneta('Azul')
caneta.cor = 'Vermelha'

print(caneta.cor)
