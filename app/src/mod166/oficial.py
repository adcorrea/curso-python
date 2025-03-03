# Decoradores em Python são funções especiais que permitem modificar ou estender o
# comportamento de outras funções ou métodos. Eles são aplicados usando a sintaxe
# @decorator, logo acima da definição da função alvo.



# No exemplo abaixo, o decorador meu_decorator adiciona comportamento extra à função diga_ola, 
# imprimindo mensagens antes e depois da execução da função principal. 
# Decoradores são uma poderosa ferramenta para reutilização de código e para adicionar funcionalidades 
# de maneira clara e concisa.



# 1. Definição do Decorador: A função meu_decorator é definida para aceitar uma função func como argumento. 
# Dentro desta função, outra função wrapper é definida. Esta função wrapper adiciona comportamento
# antes e depois da execução da função func.

# 2. Wrapper: A função wrapper utiliza *args e **kwargs para aceitar qualquer número de argumentos 
# posicionais e nomeados. Antes de chamar func, ela imprime uma mensagem. Depois de chamar func, 
# imprime outra mensagem e retorna o resultado de func.

# 3. Aplicação do Decorador: O decorador é aplicado à função diga_ola usando a sintaxe @meu_decorator. 
# Isso significa que quando diga_ola é chamada, ela na verdade é passada para meu_decorator, 
# que retorna a função wrapper.



# Definindo o decorador
def meu_decorator(func):
    def wrapper(*args, **kwargs):
        print("Algo está sendo executado antes da função.")
        resultado = func(*args, **kwargs)
        print("Algo está sendo executado depois da função.")
        return resultado
    return wrapper

# Aplicando o decorador a uma função
@meu_decorator
def diga_ola():
    print("Olá, Mundo!")

# Chamando a função decorada
diga_ola()
