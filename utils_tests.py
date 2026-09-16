import unittest
from utils import utils


class TestUtils(unittest.TestCase):

    def setUp(self):
        # Runs before every test - gives us a fresh utils instance to work with
        self.u = utils()

    # --- REVERSED tests ---

    def test_reversed_integer(self):
        # INTEGER case: a normal positive integer should have its digits reversed
        self.assertEqual(self.u.reversed(12345), 54321)

    def test_reversed_string_raises_error(self):
        # STRING input: a string should not be accepted, even if it looks numeric
        with self.assertRaises(TypeError):
            self.u.reversed("12345")

    def test_reversed_float_raises_error(self):
        # FLOAT input: a float should be rejected since the function expects an int
        with self.assertRaises(TypeError):
            self.u.reversed(123.45)

    # --- FORMATTER tests ---

    def test_formatter_integer(self):
        # INTEGER case: check that a normal integer converts correctly to both binary and octal string representations
        result = self.u.formatter(10)
        self.assertEqual(result, ("0b1010", "0o12"))

    def test_formatter_string_raises_error(self):
        # STRING input: a string should not be accepted, even if it looks numeric
        with self.assertRaises(TypeError):
            self.u.formatter("10")

    def test_formatter_float_raises_error(self):
        # FLOAT input: a float should be rejected since the function expects an int
        with self.assertRaises(TypeError):
            self.u.formatter(10.5)


if __name__ == "__main__":
    unittest.main()