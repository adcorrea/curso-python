class A:
    atributo_a = 'valor A'

    def metodo(self):
        print('A')

class B(A):
    atributo_b = 'valor B'

    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'valor C'

    def metodo(self):
        # pode ser executado como super(C, self).metodo()
        # super() chama o metodo da classe super imediata a subclasse
        super().metodo()

        # Chamando a classe super especifica da cadeia de herança
        super(B, self).metodo()
        print('C')



if __name__ == '__main__':

    c = C()

    print(c.atributo_a)
    print(c.atributo_b)
    print(c.atributo_c)


    c.metodo()