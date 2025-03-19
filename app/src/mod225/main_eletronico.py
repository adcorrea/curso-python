from utils.eletronico import Smartphone


if __name__ == '__main__':

    galaxy_s = Smartphone('Galaxy S')
    iphone = Smartphone('IPhone XV')


    galaxy_s.ligar()
    iphone.desligar()

    iphone.ligar()
    iphone.desligar()
