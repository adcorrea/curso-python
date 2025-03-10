# PROBLEMA DO DIAMANTE EM HERANÇA MÚLTIPLAS
# 
# A, B, C, D
# D(B, C) - C(A) - B(A) - A
#
#             A
#           /   \
#          B     C
#           \   / 
#             D

class A:

    def metodo(self):
        print('A')



class B(A):

    def metodo(self):
        print('B')



class C(A):

    def metodo(self):
        print('C')



class D(B, C):

    def metodo(self):
        # PROBLEMA DO DIAMANTE: qual metodo será chamado? B ou C?
        # Python 3 usa C3 superclasse linearization para gerar o mro (Method Resolution Order)
        print(D.mro())
        super().metodo()



if __name__ == '__main__':
    d= D()
    d.metodo()
