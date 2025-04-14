# https://github.com/dshvetsov2025/lab10-DS-CZ
# Partner 1: Dmitrii Shvetsov
# Partner 2: Case Zumbrum

# Full code for the test_calculator file
import unittest
import calculator
import math


class TestCalculator(unittest.TestCase):

    def test_add(self):  # 3 assertions
        pass

    def test_subtract(self):  # 3 assertions
        pass

# Function for the testing of the multiplication
    def test_multiply(self):
        self.assertEqual(calculator.multiply(3, 4), 12)
        self.assertEqual(calculator.multiply(-2, 5), -10)
        self.assertEqual(calculator.multiply(0, 10), 0)

# Function for ther testing of the division
    def test_divide(self):
        self.assertEqual(calculator.divide(2, 10), 5)
        self.assertAlmostEqual(calculator.divide(2, 9), 4.5)
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(0, 5)


    def test_divide_by_zero(self):
        pass


    def test_logarithm(self):
        pass


    def test_log_invalid_base(self):
        pass

# Functon for the testing of the logarithms with invalid arguments
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            calculator.logarithm(-1, 10)
        with self.assertRaises(ValueError):
            calculator.logarithm(2, -5)
        with self.assertRaises(ValueError):
            calculator.logarithm(1, 10)

# Function for the testing of the hypotenuse
    def test_hypotenuse(self):
        self.assertAlmostEqual(calculator.hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(calculator.hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(calculator.hypotenuse(0, 0), 0.0)

# Function for the testing of the square root
    def test_sqrt(self):
        self.assertAlmostEqual(calculator.square_root(9), 3.0)
        self.assertAlmostEqual(calculator.square_root(2), math.sqrt(2))
        with self.assertRaises(ValueError):
            calculator.square_root(-4)


# Do not touch this
if __name__ == "__main__":
    unittest.main()
