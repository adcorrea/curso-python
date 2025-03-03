# Explicação Detalhada

# Função fora(x)

# A função fora recebe um parâmetro x.

# Dentro da função fora, a variável a é definida como x. Isso faz de a uma variável que é local à função fora,
# mas quando referenciada na função dentro, ela se torna uma Free Variable.

# Função Interna dentro()

# A função dentro está aninhada dentro da função fora. Isso significa que dentro tem acesso às variáveis locais de fora, 
# mas fora não tem acesso às variáveis locais de dentro.

# dentro utiliza print(locals()) para exibir as variáveis locais definidas dentro dela.

# print(dentro.__code__.co_freevars) é utilizado para exibir as Free Variables da função dentro. 
# No contexto deste código, a Free Variable é a.

# return a faz com que a função dentro retorne o valor de a.



# Retorno e Execução

# A função fora retorna a função dentro, sem executá-la.

# Ao chamar dentro1 = fora(10), a função fora é executada com x igual a 10, definindo 
# a como 10 e retornando a função dentro.

# print(dentro1()) chama a função dentro retornada e executa suas instruções.

# Fluxo do Programa
# fora(10) é chamada e x é 10.

# a = x, portanto a é 10.

# fora retorna a função dentro.

# dentro1 = fora(10) associa a função dentro retornada à variável dentro1.

# dentro1() executa a função dentro:

# print(locals()) exibirá um dicionário vazio, pois dentro não possui variáveis locais próprias.

# print(dentro.__code__.co_freevars) exibirá ('a',), indicando que a é uma Free Variable.

# return a retornará 10, que é o valor da Free Variable a definida no escopo de fora.




def fora(x):

    # a é uma free var
    a = x

    def dentro():
        print(locals())
        print(dentro.__code__.co_freevars)
        return a
    
    return dentro


dentro1 = fora(10)
print(dentro1())


