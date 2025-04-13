
import unittest
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

#print(*sys.path, sep='\n')

from banco.conta import Conta, ContaCorrente, ContaPoupanca
from banco.excecoes import SaldoInsuficienteError

class TestConta (unittest.TestCase):

    def setUp(self):
        self.conta_corrente = ContaCorrente(agencia='11', numero='1234-8')
        self.conta_poupanca = ContaPoupanca(agencia='11', numero='1254-9')

    # TESTE DE CONTA CORRENTE    
    def test_instancia_de_conta_corrente_e_conta(self):

        self.assertIsInstance(self.conta_corrente, Conta)
        self.assertIsInstance(self.conta_corrente, ContaCorrente)


    def test_conta_corrente_deposito(self):
       self.conta_corrente.depositar(450.00)
       
       self.assertEqual(self.conta_corrente.saldo, 450.00)

    def test_conta_corrente_saque_com_saldo_positivo(self):
        self.conta_corrente.depositar(450.00)
        self.conta_corrente.sacar(100.00)
        self.assertEqual(self.conta_corrente.saldo, 350.00)


    def test_conta_corrente_saque_com_saldo_zerado_sem_limite(self):
        with self.assertRaises(SaldoInsuficienteError):
            self.conta_corrente.sacar(100.00)

    def test_conta_corrente_saque_maior_que_saldo_sem_limite(self):
        self.conta_corrente.depositar(50.00)
        
        with self.assertRaises(SaldoInsuficienteError):
            self.conta_corrente.sacar(100.00)


    def test_conta_corrente_saque_com_saldo_zerado_com_limite(self):
        self.conta_corrente.limite_extra = 400.00
        self.conta_corrente.sacar(300.00)
        self.assertEqual(self.conta_corrente.saldo, -300.00)

    def test_conta_corrente_saque_com_saldo_zerado_maior_que_limite(self):
        self.conta_corrente.limite_extra = 400.00
        
        with self.assertRaises(SaldoInsuficienteError):
            self.conta_corrente.sacar(500)


    # TESTE DE CONTA POUPANÇA
    def test_instancia_de_conta_poupanca_e_conta(self):
        self.assertIsInstance(self.conta_poupanca, Conta)
        self.assertIsInstance(self.conta_poupanca, ContaPoupanca)

    def test_conta_poupanca_deposito(self):
       self.conta_poupanca.depositar(450.00)
       
       self.assertEqual(self.conta_poupanca.saldo, 450.00)

    def test_conta_poupanca_saque_com_saldo_positivo(self):
        self.conta_poupanca.depositar(450.00)
        self.conta_poupanca.sacar(100.00)
        self.assertEqual(self.conta_poupanca.saldo, 350.00)


    def test_conta_poupanca_saque_com_saldo_zerado(self):
        with self.assertRaises(SaldoInsuficienteError):
            self.conta_poupanca.sacar(100.00)

    def test_conta_poupanca_saque_maior_que_saldo(self):
        self.conta_poupanca.depositar(50.00)
        
        with self.assertRaises(SaldoInsuficienteError):
            self.conta_poupanca.sacar(100.00)

    


if __name__ == '__main__':
    unittest.main(verbosity=2)

