
class Carro:

    def __init__(self, nome):
        self.nome = nome


    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def motor(self):
        return self.__motor
    
    @motor.setter
    def motor(self, motor):
        self.__motor = motor