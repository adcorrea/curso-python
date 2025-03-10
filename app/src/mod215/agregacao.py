"""
Relações entre classes: associação, agregação e composição

Agregação é uma forma mais especializada de associação entre dois ou mais objetos. Cada objeto terá seu ciclo de vida independente.
Geralmente é uma relação de um para muitos, onde um objeto tem um ou muitos objetos.

Os objetos podem viver separadamente, mas pode tratar de uma relação onde um objeto precisa de 
outro para fazer determinada tarefa.

"""

class Carrinho:
    def __init__(self) -> None:        
        self._produtos = []


    def inserir_produtos(self, *produtos):
        for produto in produtos:
            self._produtos.append(produto)

    def total(self):
        return sum([f.preco for f in self._produtos])
    

    def listar_produtos(self):
        total = 0.0
        for produto in self._produtos:
            print(produto.nome, produto.preco)
            total += produto.preco

        print(f'==> TOTAL: {total}')


class Produto():
    def __init__(self, nome, preco) -> None:
        self.nome = nome
        self.preco = preco

if __name__ == '__main__':
    carrinho = Carrinho()

    p1, p2 = Produto('Caneta', 1.20), Produto('Camiseta', 20)

    carrinho.inserir_produtos(p1, p2)
    carrinho.listar_produtos()



    

    