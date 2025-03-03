"""
########### Adiando execução de funções


"""


def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y



def criar_funcao(funcao, x):
    """
        Parametros:
            funcao: uma funcao python de dois parametros.
            x: uma constante
         
        Retorno: a função interna esperando o parametro y.
        
    """

    # A função criar_funcao recebe por parametro uma função (funcao) e um valor (x).
    # a funcao interna é definida esperando um parametro y. Ela vai retornar o parametro funcao recebendo
    # como parametro o x, passado na função criar_funcao e o y passado na funcao interna

    def interna(y):
        return funcao(x, y)
    
    # o retorno será a funcao interna esperando uma parametro y -> interna(y)
    # Dentro dela terá duas variáveis, x e funcao
    return interna

# cria a função soma_com_cinco, passando na função criar_funcao
# o parametro soma e a o valor 5 no x.
# função soma_com_cinco ficará agora com a assinatura de soma_com_cinco(y)
soma_com_cinco = criar_funcao(soma, 5)


multiplica_por_dez = criar_funcao(multiplica, 10)

# Executar a função soma_com_cinco(y), ele vai executar a função interna(y)
# no qual vai usar o valor da variável funcao, que agora é soma, a variável x, que é 5, e o parametro
# y passado que é 10
print(f'Soma com cinco: {soma_com_cinco(10)}')

print(f'Multiplica por dez: {multiplica_por_dez(2)}')

