# Exercicio com classes

# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça uma ligação entre Carro tem Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça uma ligação entre Carro e Fabricante
# Obs.: Um Fabricante pode fabricar vários carros

# Exiba o nome do carro, motor e fabricantes na tela


from entity import Carro, Fabricante, Motor


if __name__ == '__main__':

    carro_maverick = Carro('Maverick')
    carro_corcel = Carro('Corcel')

    fabricante_ford = Fabricante('Ford')
    
    motor_v8 = Motor('Ford V8')
    carro_maverick.motor = motor_v8
    carro_corcel.motor = motor_v8

    fabricante_ford.inserir_carro(carro_corcel, carro_maverick)
    
    fabricante_ford.listar_carros()
