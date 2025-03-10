class A:
    atributo_a = 'valor A'

    def __init__(self, atributo):
        self.atributo_a = atributo

    def metodo(self):
        print('A')

class B(A):
    atributo_b = 'valor B'

    def __init__(self, atributo, outro_atributo):
        super().__init__(atributo)
        self.outro_atributo = outro_atributo

    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'valor C'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def metodo(self):
        # pode ser executado como super(C, self).metodo()
        # super() chama o metodo da classe super imediata a subclasse
        super().metodo()

        # Chamando a classe super especifica da cadeia de herança
        super(B, self).metodo()
        print('C')



if __name__ == '__main__':

    c = C('Valor C', 'Valor N')



    print(c.atributo_a)
    print(c.atributo_b)
    print(c.atributo_c)
    print(c.outro_atributo)
