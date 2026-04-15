import unittest
from rpn import rpn_calculator
import math

class TestRPNCalculator(unittest.TestCase):

    # ---------- Operaciones básicas ----------
    def test_addition(self):
        self.assertEqual(rpn_calculator("2 3 +"), 5)

    def test_subtraction(self):
        self.assertEqual(rpn_calculator("5 2 -"), 3)

    def test_multiplication(self):
        self.assertEqual(rpn_calculator("4 3 *"), 12)

    def test_division(self):
        self.assertEqual(rpn_calculator("8 2 /"), 4)

    def test_power(self):
        self.assertEqual(rpn_calculator("2 3 yx"), 8)

    # ---------- Funciones matemáticas ----------
    def test_sqrt(self):
        self.assertEqual(rpn_calculator("9 sqrt"), 3)

    def test_sin(self):
        self.assertAlmostEqual(rpn_calculator("90 sin"), 1.0, places=5)

    def test_cos(self):
        self.assertAlmostEqual(rpn_calculator("0 cos"), 1.0, places=5)

    def test_tan(self):
        self.assertAlmostEqual(rpn_calculator("45 tg"), 1.0, places=5)

    # ---------- Stack operations ----------
    def test_dup(self):
        self.assertEqual(rpn_calculator("5 dup +"), 10)

    def test_chs(self):
        self.assertEqual(rpn_calculator("5 chs"), -5)

    def test_clear(self):
        self.assertEqual(rpn_calculator("5 clear 3"), 3)

    # ---------- Constantes ----------
    def test_pi(self):
        self.assertAlmostEqual(rpn_calculator("p"), math.pi)

    def test_e(self):
        self.assertAlmostEqual(rpn_calculator("e"), math.e)

    def test_phi(self):
        self.assertEqual(rpn_calculator("j"), 1.618)

    # ---------- Memoria ----------
    def test_store_and_recall(self):
        self.assertEqual(rpn_calculator("5 sto00 clear rcl00"), 5)

    # ---------- Errores ----------
    def test_stack_error(self):
        self.assertEqual(rpn_calculator("2 +"), "Error en la expresión")

    def test_invalid_token(self):
        self.assertEqual(rpn_calculator("abc"), "Error en la expresión")

    def test_division_by_zero(self):
        self.assertEqual(rpn_calculator("5 0 /"), "Error en la expresión")

    def test_unbalanced_stack(self):
        self.assertEqual(rpn_calculator("2 3"), "Error: Pila mal balanceada")


if __name__ == "__main__":
    unittest.main()