import unittest

from calculator import add, calculate, divide, multiply, subtract


class CalculatorTest(unittest.TestCase):
    def test_basic_operations(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(divide(10, 4), 2.5)

    def test_calculate(self):
        self.assertEqual(calculate(3, "+", 4), 7)
        self.assertEqual(calculate(8, "/", 2), 4)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            divide(1, 0)

    def test_unknown_operator(self):
        with self.assertRaises(ValueError):
            calculate(1, "%", 2)


if __name__ == "__main__":
    unittest.main()
