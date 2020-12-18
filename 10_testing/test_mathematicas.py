import unittest


def mathematicas(x, y):
    return x ** y


class TestYourPackage(unittest.TestCase):

    def test_check_math(self):
        self.assertEquals(mathematicas(3, 2), 9)

    def test_raises_error(self):
        with self.assertRaises(TypeError):
            mathematicas('string', 'zing')

    def test_does_not_pass(self):
        self.assertIn(mathematicas(3, 2), 10)
