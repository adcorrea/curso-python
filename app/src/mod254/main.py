# Enum -> Enumerações

# Enumerações na programação, são usadas em ocasiões onde temos
# um determinado número de coisas.

# Enums têm membros e seus valroes são constantes.

# Enums em Python:
#     - são um conjunto de nomes simbólicos (membros) ligados a valores unicos.
#     - podem ser iterados para tornar seus membros canônicos na ordem de definição.

# enum.Enum é uma superclasse para suas enumerações. Mas também pode ser usada diretamente
# (mesmo assim, Enum não são classes normais em Python)

# Você poderá user seu Enum em type annotations, com isinstance e outras coisas relacionadas
# com tipo.

# Para obter os dados:
#     membro = Classe(valor), Classe['chave']
#     chave = Classe.chave.name
#     valor = Classe.chave.value

import enum

Direcoes = enum.Enum('Direcoes', ['ESQUERDA', 'DIREITA'])

def mover(direcao):
    if not isinstance(direcao, Direcoes):
        raise ValueError('Direção não encontrada')

    print(f'Movendo para {direcao}')


if __name__ == '__main__':
    mover(Direcoes.DIREITA)
    mover(Direcoes.ESQUERDA)


    print(Direcoes(1), Direcoes['ESQUERDA'], Direcoes.ESQUERDA)
    print(Direcoes(1).name, Direcoes.ESQUERDA.value)