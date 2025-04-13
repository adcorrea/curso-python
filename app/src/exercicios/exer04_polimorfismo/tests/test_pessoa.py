import os
import sys
import unittest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))


from banco.pessoa import Pessoa, Cliente
from banco.conta import ContaCorrente, ContaPoupanca


class TestPessoa (unittest.TestCase):

    def setUp(self):
        self.cliente = Cliente(cpf='58978999', nome='Antonio Junior', idade=38)


    def test_cliente_instancia_pessoa_e_cliente(self):
        self.assertIsInstance(self.cliente, Cliente)
        self.assertIsInstance(self.cliente, Pessoa)

    def test_abrir_conta_corrente(self):
        conta_corrente = ContaCorrente(agencia='11', numero='12345')
        self.cliente.abrir_conta(conta_corrente)

        self.assertIsNotNone(self.cliente.conta)
        self.assertIsInstance(self.cliente.conta, ContaCorrente)


    def test_abrir_conta_poupanca(self):
        conta_poupanca = ContaPoupanca(agencia='11', numero='12345')
        self.cliente.abrir_conta(conta_poupanca)

        self.assertIsNotNone(self.cliente.conta)
        self.assertIsInstance(self.cliente.conta, ContaPoupanca)
    
        

if __name__ == '__main__':
    unittest.main()
