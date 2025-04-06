# Python Special Methods, Magic Methods ou Dunder Methods

# Dunder = Double Underscore = __dunner__

# Antigo e útil: https://rszalski.github.io/magicmethods/
#                https://docs.python.org/3/reference/datamodel.html#specialnames

# __lt__(self,other) - self < other
# __le__(self,other) - self <= other
# __gt__(self,other) - self > other
# __ge__(self,other) - self >= other
# __eq__(self,other) - self == other
# __ne__(self,other) - self != other
# __add__(self,other) - self + other
# __sub__(self,other) - self - other
# __mul__(self,other) - self * other
# __truediv__(self,other) - self / other
# __neg__(self) - -self
# __str__(self) - str
# __repr__(self) - str


class Ponto:
    def __init__(self, x, y, z='String'):
        self.x = x
        self.y = y
        self.z = z

    # o str sobrepóe o __repr__
    def __str__(self):
        return f'({self.x}, {self.y}, {self.z})'

    # __repr__ é a representação do objeto
    def __repr__(self):
        class_name = type(self).__name__
        return f'{class_name}({self.x!r}, {self.y!r}, {self.z!r})'


if __name__ == '__main__':
    p1 = Ponto(1, 2)
    p2 = Ponto(978, 876)

    print(p1)

    # formas de invocar o repr
    print(repr(p2))
    print(f'{p2!r}')