# Este exemplo mostra como os decoradores podem ser usados em um cenário do mundo real para adicionar funcionalidades
# importantes, como verificação de autenticação, de forma clara e reutilizável.




# 1. Função de Verificação de Autenticação: A função is_authenticated() simula uma verificação de autenticação. 
# Em um sistema real, esta função deve incluir a lógica para verificar se o usuário está autenticado 
# (por exemplo, verificando tokens, sessões, etc.).

# 2. Definição do Decorador: O decorador require_authentication é definido para aceitar uma função func 
# como argumento. Dentro desta função, outra função wrapper é definida para realizar a verificação de 
# autenticação antes de chamar func.

# 3. Wrapper: A função wrapper verifica se o usuário está autenticado chamando is_authenticated(). Se o usuário 
# não estiver autenticado, uma exceção é lançada. Caso contrário, func é chamada e seu resultado é retornado.

# 4. Aplicação do Decorador: O decorador require_authentication é aplicado à função pagina_restrita usando 
# a sintaxe @require_authentication. Isso significa que quando pagina_restrita é chamada, a verificação 
# de autenticação é realizada primeiro.

# 5. Tentando Acessar a Página Restrita: Ao tentar acessar pagina_restrita(), o decorador garante que a 
# verificação de autenticação seja realizada. Se o usuário não estiver autenticado, uma mensagem de erro 
# será exibida; caso contrário, o conteúdo da página restrita será mostrado.


# Simulação de uma função que verifica a autenticação do usuário
def is_authenticated():
    # Aqui você deve implementar a lógica de verificação de autenticação
    # Por exemplo, verificar tokens, sessões, etc.
    return True  # Simulação de um usuário autenticado

# Definindo o decorador de autenticação
def require_authentication(func):
    def wrapper(*args, **kwargs):
        if not is_authenticated():
            raise Exception("Usuário não autenticado. Acesso negado.")
        return func(*args, **kwargs)
    return wrapper

# Aplicando o decorador a uma função que gera uma página
@require_authentication
def pagina_restrita():
    return "Bem-vindo à página restrita!"

# Tentando acessar a página restrita
try:
    conteudo = pagina_restrita()
    print(conteudo)
except Exception as e:
    print(e)
