# Exercicio - Unir listas

# Crie uma função zipper (como o zipper de roupas)

# O trabalho dessa função será unir duas listas na ordem.

# Use todos ovalores da menos lista.

# Ex.

# ['Salvador', 'Ubatuba', 'Belo Horizonte']
# ['BA', 'SP', 'MG', 'RJ']
# Resultado 
# ['('Salvador', 'BA'), ('Ubatuba', 'SP'), ('Belo Horizonte', 'MG')]



def une_lista(lista1, lista2) -> list:
    if len(lista1) > len(lista2):
        menor_lista = lista2
        maior_lista = lista1
    else:
        menor_lista = lista1
        maior_lista = lista2


    lista_unica = []

    #enumerate - enumera iteráveis (índices)
    for item in enumerate(menor_lista):
        indice, nome = item
        nova_lista = []
        nova_lista.append(nome)
        nova_lista.append(maior_lista[indice])
        lista_unica.append(tuple(nova_lista))

    return lista_unica



if __name__ == '__main__':

    cidades =  ['Salvador', 'Ubatuba', 'Belo Horizonte']
    estados = ['BA', 'SP', 'MG', 'RJ']

    print(une_lista(cidades, estados))

