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
        self.cor_tinta = cor

    def get_cor(self):
        return self.cor
    
    @property
    def cor(self):
        return self.cor_tinta
    
    @property
    def cor_tampa(self):
        return '123'
    

caneta = Caneta('Azul')

print(caneta.get_cor())

print(caneta.cor)
print(caneta.cor_tampa)

