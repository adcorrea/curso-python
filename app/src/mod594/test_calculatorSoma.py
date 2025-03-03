import unittest
from modulo.calculate import soma


class TestSoma(unittest.TestCase):

    def test_soma_5_5_retorna_10(self):
        self.assertEqual(soma(5, 5), 10)

    def test_soma_5_neg_5_retorna_0(self):
        self.assertEqual(soma(-5, 5), 0)


    def test_varias_cases(self):
        x_y_saidas = (
            (10, 10, 20),
            (5, 5, 10),
            (1.5, 1.5, 3.0),
            (100, 100, 200),
        )

        for x_y_saida in x_y_saidas:
            with self.subTest(x_y_saida=x_y_saida):
                x, y, saida = x_y_saida
                self.assertEqual(soma(x, y), saida)


    def test_x_assertionerror_type(self):
        with self.assertRaises(AssertionError):
            soma('11', 0)
    
    def test_y_assertionerror_type(self):
        with self.assertRaises(AssertionError):
            soma(0,'11')




if __name__ == '__main__':
    unittest.main(verbosity=2)