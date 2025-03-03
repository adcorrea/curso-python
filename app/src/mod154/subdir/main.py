

# Tentando importar um módulo fora da subpasta do __main__
try:
    from app.src.utils.modulo import hello
    hello()
    
except ModuleNotFoundError as ex:
    print('Não foi possível importar o módulo. ', ex)


# importando modulo dentro da pasta no diretório do __main__
try:
    from modulo.mod1 import hello

    hello()

except ModuleNotFoundError as ex:
    print('Não foi possível importar o módulo. ', ex)

# main
print('Hello World!', __name__)