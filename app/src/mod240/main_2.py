# Context Manager com classes

# tratamento de exceções no context manager

class MyContextManager:

    def __init__(self, caminho_arquivo, modo):
        self.caminho_arquivo = caminho_arquivo
        self.modo = modo
        self._arquivo = None

    def __enter__(self):
        self._arquivo = open(self.caminho_arquivo, self.modo, encoding='utf8')
        return self._arquivo
    
    def __exit__(self, class_exception, exception_, traceback_):
        print(class_exception)
        print(exception_)
        print(traceback_)
        self._arquivo.close()
        
        
        raise class_exception(*exception_.args).with_traceback(traceback_)
        





if __name__ == '__main__':

    with MyContextManager('arquivo.txt', 'w') as arquivo:
        arquivo.write('Linha 1 \n', 123)
        arquivo.write('Linha 2 \n')
        arquivo.write('Linha 3 \n')

        print('WITH', arquivo)