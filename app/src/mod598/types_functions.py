from typing import Callable, Sequence, Iterable

# Tipos em funções
def retorna_funcao(funcao: Callable[[], None]) -> Callable:
    return funcao

def fala_oi():
    print('Oi')

retorna_funcao(fala_oi)()

def returna_funcao_s(funcao: Callable[[int, int], int]) -> Callable:
    return funcao

def soma(x: int, y: int) -> int:
    return (x + y)

print(returna_funcao_s(soma)(1,2))

def iterar_s(sequencia: Sequence[int]):
    return [x * 2 for x in sequencia]

def iterar_i(sequencia: Iterable[int]):
    return [x * 2 for x in sequencia]

print(iterar_s([1, 2, 3]))
print(iterar_i([1, 2, 3]))