# Criando Exceptions em Python Orientado a Objetos
# Para criar uma Excption em Python, você só pecisa herdar de alguma 
# exception da linguagem.

# A recomendação da doc é herdar de Exception.
# https://docs.python.org/3/library/exceptions.html

# Criando exceptions (comum colocar Error no final)

# Levantando (raise) / Lançando (throw) exceções
# Relançando exceções
# Adicionando notas em exceções (3.11.0)


class MeuError(Exception):
    ...

class OutroError(Exception):
    ...

def levantar():
   

    excption_ = MeuError('A mensagem de erro')

    # adicionar nota
    excption_.add_note('Notações...')
    
    # Levantando (raise) o erro    
    raise excption_




try:
    levantar()
except MeuError as error:
    print(error)
    
    # Relaçando a exceção
    raise OutroError('error')


