import unittest
from modulo.calculate import subtrai


class TestSubtrai(unittest.TestCase):

    def test_5_5_retorna_0(self):
        self.assertEqual(subtrai(5,5), 0)


    def test_varios_cases(self):

        cases = (
            (5, 5, 0),
            (10, -5, 15),
            (0, 0, 0),
            (0, 1, -1),
            (1, 0, 1),
        )

        for case in cases:
            with self.subTest(case=case):
                x, y, saida = case
                self.assertEqual(subtrai(x, y), saida)

    def test_type_x(self):
        with self.assertRaises(AssertionError):
            subtrai('11', 0)

    def test_type_y(self):
        with self.assertRaises(AssertionError):
            subtrai(0, '11')


if __name__ == '__main__':
    unittest.main()