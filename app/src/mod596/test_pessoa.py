

import unittest
from entity.pessoa import Pessoa
from unittest.mock import patch


class TestPessoa(unittest.TestCase):
    def setUp(self):
        self.p1 = Pessoa('Antonio', 'Junior')
        self.p2 = Pessoa(1, 2)

    def test_pessoa_attr_nome_tem_valor_correto(self):
        self.assertEqual(self.p1.nome, 'Antonio')

    def test_pessoa_attr_nome_string(self):
        self.assertIsInstance(self.p1.nome, str)

    def test_pessoa_attr_nome_nao_string(self):
        with self.assertRaises(AssertionError):
            self.assertIsInstance(self.p2.nome, str)


    def test_pessoa_attr_sobrenome_tem_valor_correto(self):
        self.assertEqual(self.p1.sobrenome, 'Junior')
    
    def test_pessoa_attr_sobrenome_string(self):
        self.assertIsInstance(self.p1.sobrenome, str)


    def test_pessoa_attr_nome_nao_string(self):
        with self.assertRaises(AssertionError):
            self.assertIsInstance(self.p2.sobrenome, str)


    def test_dados_obtidos_false(self):
        self.assertFalse(self.p1.dados_obtidos)


    def test_obter_todos_os_dados_sucesso_OK(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = True
            self.assertEqual(self.p1.obter_todos_os_dados(), 'CONECTADO')
            self.assertTrue(self.p1.dados_obtidos)

    def test_obter_todos_os_dados_falha_404(self):
        with patch('requests.get') as fake_request:
            fake_request.return_value.ok = False
            self.assertEqual(self.p1.obter_todos_os_dados(), 'ERRO 404')
            self.assertFalse(self.p1.dados_obtidos)



if __name__ == '__main__':
    unittest.main(verbosity=2)