# Context Manager com classes

# Você pode implementar seus próprios protocolos apenas implementando
# os dunder methods que o Python vai usar. 

# Isso é chamado de Duck typing. Um conceito relacionado com tipagem
# dinâmica onde o Python não está interessado no tipo, mas se alguns
# métodos existem no seu objeto para que el funcione de forma 
# adequada.

# Duck typing:

# Quando vejo um pássaro que caminha como um pato, nada como um pato
# e grasna como um pato, eu chamo aquele pássaro de pato.

# Para criar um context manager, os métodos __enter__ e __exit__
# devem ser implementados.

# O método __exit__ receberá a classe de exceção, a exceção e traceback.
# Se ele retornar True, exceção no with será suprimidas.


# Implementando o contexto de arquivo
# with open('caminho_arquivo', 'x') as arquivo

class MyContextManager:

    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        print('ENTER')
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo
    
    def __exit__(self, class_exception, exception_, traceback_):
        print('EXIT')
        self._arquivo.close()





if __name__ == '__main__':

    with MyContextManager('arquivo.txt', 'w') as arquivo:
        arquivo.write('Linha 1 \n')
        arquivo.write('Linha 2 \n')
        arquivo.write('Linha 3 \n')

        print('WITH', arquivo)