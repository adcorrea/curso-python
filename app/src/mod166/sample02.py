import time


# Neste exemplo, o decorador medir_tempo modifica o comportamento da função calcular_soma ao adicionar a 
# funcionalidade de medir e exibir o tempo de execução da função. 
# Isso pode ser extremamente útil para identificar gargalos de desempenho em um código.


# 1. Importação do Módulo time: O módulo time é importado para medir o tempo de execução.

# 2. Definição do Decorador: O decorador medir_tempo é definido para aceitar uma função func como argumento. 
# Dentro desta função, outra função wrapper é definida para medir o tempo de execução.

# 3. Wrapper: A função wrapper captura o tempo antes (inicio) e depois (fim) da execução de func. 
# A diferença entre fim e inicio é o tempo de execução da função. Este tempo é então impresso no console.

# 4. Aplicação do Decorador: O decorador medir_tempo é aplicado à função calcular_soma usando a 
# sintaxe @medir_tempo. Isso significa que quando calcular_soma é chamada, o tempo de execução é medido e exibido.

# 5. Chamando a Função Decorada: Ao chamar calcular_soma(1000000), o decorador mede o tempo que a função leva 
# para calcular a soma de 0 a 999999. 

# Definindo o decorador para medir o tempo de execução
def medir_tempo(func):
    def wrapper(*args, **kwargs):
        inicio = time.time()  # Captura o tempo no início da execução
        resultado = func(*args, **kwargs)
        fim = time.time()  # Captura o tempo no final da execução
        print(f"Tempo de execução da função '{func.__name__}': {fim - inicio:.4f} segundos")
        return resultado
    return wrapper

# Aplicando o decorador a uma função que realiza uma tarefa
@medir_tempo
def calcular_soma(n):
    soma = 0
    for i in range(n):
        soma += i
    return soma

# Chamando a função decorada
resultado = calcular_soma(1000000)
print(f"Resultado: {resultado}")
