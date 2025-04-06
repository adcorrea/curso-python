# Context Manager com classes

# Context Manager com função = Criando e Usando gerenciadores de contexto

from contextlib import contextmanager

@contextmanager
def my_open(caminho_arquivo, modo):

    try:
        print('Abrindo arquivo')
        arquivo = open(caminho_arquivo, modo, encoding='utf8')
        
        # generator
        yield arquivo
    except Exception as e:
        raise e
    finally:
        print('Fechando arquivo')
        arquivo.close()




if __name__ == '__main__':

    with my_open('arquivo.txt', 'w') as arquivo:
        arquivo.write('Linha 1 \n')
        arquivo.write('Linha 2 \n')
        arquivo.write('Linha 3 \n')

    with my_open('arquivo.txt', 'w') as arquivo:
        arquivo.write('Linha 1 \n', 12)
        arquivo.write('Linha 2 \n')
        arquivo.write('Linha 3 \n')