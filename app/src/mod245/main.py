# Método especial __call__
# Callable é algo que pode ser executado com parènteses

# em classes normais, __call__ faz a instância de uma classe "callable"


class CallMe:
    def __init__(self, phone):
        self.phone = phone

    def __call__(self, nome):
        print(nome, ' está chamando, ', self.phone)


if __name__ == '__main__':
    call1 = CallMe('123456')
    call1('Junior')