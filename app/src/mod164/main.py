# Free Vars + nonlocal

"""
Variáveis Livres (Free Variables) em Python

Uma variável livre (Free Variable) é uma variável referenciada em uma função, mas que não está nem localmente 
declarada nem globalmente no escopo da função. Essencialmente, uma variável livre é definida em um escopo externo 
e é acessada de dentro da função. Esse conceito é fundamental quando trabalhamos com funções aninhadas 
(nested functions) e fechamentos (closures) em Python.



Aplicações Práticas
Geradores de Funções: Variáveis livres são frequentemente usadas em geradores de funções personalizadas, 
como o exemplo abaixo, onde cada função retornada possui seu próprio estado independente.

Memorização: Elas podem ser usadas para implementar memorização (caching), onde uma função lembra dos resultados anteriores.

Encapsulamento: Elas ajudam a encapsular dados que não devem ser acessíveis de fora da função, melhorando o controle 
sobre a manipulação dos dados.

As variáveis livres são ferramentas poderosas para desenvolver soluções flexíveis e eficientes em Python. 

"""


# Exemplo de Uso de Variáveis Livres


def criador_de_contador(inicial):
    contador = inicial  # 'contador' é uma variável livre na função interna 'incrementar'
    
    def incrementar():
        nonlocal contador  # 'nonlocal' permite modificar a variável livre
        contador += 1
        return contador
    
    return incrementar

contador_5 = criador_de_contador(5)
print(contador_5())  # Saída: 6
print(contador_5())  # Saída: 7

contador_10 = criador_de_contador(10)
print(contador_10())  # Saída: 11
print(contador_10())  # Saída: 12


# Explicação do Código
# criador_de_contador: Esta é uma função que cria e retorna uma função interna chamada incrementar.

# Variável Livre: A variável contador é declarada no escopo externo (de criador_de_contador), mas é referenciada e 
# modificada na função interna incrementar. Portanto, contador é uma variável livre em incrementar.

# nonlocal: A palavra-chave nonlocal é usada dentro de incrementar para indicar que queremos modificar a variável 
# contador definida no escopo externo e não criar uma nova variável local.

# Closures: A função retornada (incrementar) "lembra-se" do ambiente em que foi criada, permitindo acesso à 
# variável contador mesmo após a execução de criador_de_contador.