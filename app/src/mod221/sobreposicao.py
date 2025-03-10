# Herança vs Composição

# super() é a super classe da sub classe
# Classe principal (Pessoa)
#     -> super class, base class, parent class

# Classes filhas (Cliente)
#     -> sub class, child class, derived class



class MinhaString(str):
    def upper(self):
        print('CHAMOU UPPER')
        return super().upper()
    

if __name__ == '__main__':

    string = MinhaString('Antonio')
    print(string.upper())