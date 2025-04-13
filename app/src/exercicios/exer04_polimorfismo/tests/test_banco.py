
import unittest
import os
import sys


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

#print(*sys.path, sep='\n')

from banco.banco import Banco
from banco.pessoa import Cliente
from banco.conta import ContaCorrente, ContaPoupanca
from banco.excecoes import AutenticacaoErro


class TestBanco(unittest.TestCase):

    def setUp(self):
        self.cliente_banco_conta_corrente = Cliente(nome='Antonio Junior', cpf='123123',idade=58)
        self.cliente_banco_conta_corrente.abrir_conta(ContaCorrente(agencia='11', numero='12345'))

        self.cliente_banco_conta_poupanca = Cliente(nome='Maria das Dores', cpf='789456', idade=65)
        self.cliente_banco_conta_poupanca.abrir_conta(ContaPoupanca(agencia='66', numero='55555'))

    def test_banco_instancia_banco(self):
        banco_teste = Banco(nome='Teste')

        self.assertIsInstance(banco_teste, Banco)

    def test_banco_incluir_um_cliente(self):
        banco_teste = Banco(nome='Teste')
        banco_teste.incluir_cliente(self.cliente_banco_conta_corrente)

        self.assertIn(self.cliente_banco_conta_corrente, banco_teste._clientes)

    def test_banco_incluir_dois_cliente(self):
        banco_teste = Banco(nome='Teste')
        banco_teste.incluir_cliente(self.cliente_banco_conta_corrente)
        banco_teste.incluir_cliente(self.cliente_banco_conta_poupanca)

        self.assertIn(self.cliente_banco_conta_corrente, banco_teste._clientes)
        self.assertIn(self.cliente_banco_conta_poupanca, banco_teste._clientes)



    def test_banco_autenticao_com_sucesso(self):
        banco_teste = Banco(nome='Teste')
        banco_teste.incluir_cliente(self.cliente_banco_conta_corrente)
        banco_teste.incluir_cliente(self.cliente_banco_conta_poupanca)

        cliente = banco_teste.autenticar(agencia='11', numero='12345', cpf='123123')

        self.assertIs(cliente, self.cliente_banco_conta_corrente)

    def test_banco_autenticao_com_falha_com_cpf_invalido(self):
        banco_teste = Banco(nome='Teste')
        banco_teste.incluir_cliente(self.cliente_banco_conta_corrente)
        banco_teste.incluir_cliente(self.cliente_banco_conta_poupanca)
        
       

        with self.assertRaises(AutenticacaoErro):
            cliente = banco_teste.autenticar(agencia='11', numero='12345', cpf='123')

    def test_banco_autenticao_com_falha_com_conta_invalida(self):
        banco_teste = Banco(nome='Teste')
        banco_teste.incluir_cliente(self.cliente_banco_conta_corrente)
        banco_teste.incluir_cliente(self.cliente_banco_conta_poupanca)
        
       

        with self.assertRaises(AutenticacaoErro):
            cliente = banco_teste.autenticar(agencia='11', numero='555', cpf='123123')


    def test_banco_autenticao_com_falha_com_conta_de_outro_cliente(self):
        banco_teste = Banco(nome='Teste')
        banco_teste.incluir_cliente(self.cliente_banco_conta_corrente)
        banco_teste.incluir_cliente(self.cliente_banco_conta_poupanca)
        
       

        with self.assertRaises(AutenticacaoErro):
            cliente = banco_teste.autenticar(agencia='66', numero='55555', cpf='123123')




if __name__ == '__main__':
    unittest.main(verbosity=2)

