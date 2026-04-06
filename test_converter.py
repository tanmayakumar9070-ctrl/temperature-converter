import unittest
from converter import convert

class TestConverter(unittest.TestCase):

    def test_celsius_to_fahrenheit(self):
        self.assertAlmostEqual(convert(0, "C", "F"), 32.0)
        self.assertAlmostEqual(convert(100, "C", "F"), 212.0)

    def test_fahrenheit_to_celsius(self):
        self.assertAlmostEqual(convert(32, "F", "C"), 0.0)

    def test_celsius_to_kelvin(self):
        self.assertAlmostEqual(convert(0, "C", "K"), 273.15)

    def test_negative_kelvin_raises(self):
        with self.assertRaises(ValueError):
            convert(-1, "K", "C")

    def test_same_unit(self):
        self.assertEqual(convert(25, "C", "C"), 25)

if __name__ == "__main__":
    unittest.main()