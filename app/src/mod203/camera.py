# Mantendo estados dentro da classe

class Camera:
    def __init__(self, nome, filmando=False) -> None:
        self.nome = nome
        self.filmando = filmando

    def filmar(self):
        if self.filmando:
            print(f'{self.nome} ja está filmando...')
            return
        
        print(f'{self.nome} está filmando...')
        self.filmando = True

    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} não pode fotografar filmando!')
            return
        
        print(f'{self.nome} tirou uma foto!')

    def parar_filmar(self):
        if not self.filmando:
            print(f'{self.nome} NÃO está filmando...')
            return
        
        self.filmando = False
        print(f'{self.nome} está parou de filmar...')


c1 = Camera('Canon')
c2 = Camera('Sony')

c1.filmar()
print(c1.filmando)
print(c2.filmando)

