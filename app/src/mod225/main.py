# Um Mixin em Python é uma classe projetada para fornecer funcionalidades adicionais a outras classes por meio de herança, sem ser considerada uma classe base principal. Geralmente, os Mixins contêm um conjunto específico e modular de métodos ou atributos que podem ser combinados com outras classes para ampliar suas capacidades. Eles são comumente utilizados para promover a reutilização de código e evitar redundância, permitindo que desenvolvedores componham comportamentos complexos ao invés de depender de herança hierárquica profunda.

# Em termos de design, Mixins:

# São tipicamente usados para adicionar funcionalidades específicas, como autenticação, log, ou formatação.

# Não são concebidos para serem instanciados diretamente, funcionando apenas como classes complementares.

# Incentivam um estilo de programação baseado em composição em oposição a uma herança tradicional.

# Ref: https://docs.python.org/3/tutorial/classes.html?form=MG0AV3#multiple-inheritance


from utils.log import LogFileMixin, LogPrintMixin


if __name__ == '__main__':
    l = LogFileMixin()
    l.log_error('Ola')
    l.log_success('Ola')

    l_2 = LogPrintMixin()
    l_2.log_error('Ola')