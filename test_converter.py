"""
test_converter.py — Unit tests for converter.py

Run with:
    python -m pytest test_converter.py -v
    python -m unittest test_converter       # no pytest needed

Test categories
---------------
  TestDirectFunctions   → individual helper functions
  TestConvertDispatch   → convert() with all unit combinations
  TestEdgeCases         → boundary values and error paths
  TestAllConversions    → all_conversions() helper
"""

import unittest
from converter import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    celsius_to_kelvin,
    kelvin_to_celsius,
    convert,
    all_conversions,
)


class TestDirectFunctions(unittest.TestCase):
    """Test each helper function in isolation."""

    # ── celsius_to_fahrenheit ────────────────────────────────────────
    def test_c_to_f_freezing(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(0), 32.0)

    def test_c_to_f_boiling(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(100), 212.0)

    def test_c_to_f_negative(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(-40), -40.0)  # C==F crossover

    def test_c_to_f_body_temp(self):
        self.assertAlmostEqual(celsius_to_fahrenheit(37), 98.6, places=1)

    # ── fahrenheit_to_celsius ────────────────────────────────────────
    def test_f_to_c_freezing(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(32), 0.0)

    def test_f_to_c_boiling(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(212), 100.0)

    def test_f_to_c_crossover(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(-40), -40.0)

    # ── celsius_to_kelvin ────────────────────────────────────────────
    def test_c_to_k_absolute_zero(self):
        self.assertAlmostEqual(celsius_to_kelvin(-273.15), 0.0)

    def test_c_to_k_freezing(self):
        self.assertAlmostEqual(celsius_to_kelvin(0), 273.15)

    def test_c_to_k_boiling(self):
        self.assertAlmostEqual(celsius_to_kelvin(100), 373.15)

    # ── kelvin_to_celsius ────────────────────────────────────────────
    def test_k_to_c_absolute_zero(self):
        self.assertAlmostEqual(kelvin_to_celsius(0), -273.15)

    def test_k_to_c_freezing(self):
        self.assertAlmostEqual(kelvin_to_celsius(273.15), 0.0)

    def test_k_to_c_negative_raises(self):
        with self.assertRaises(ValueError):
            kelvin_to_celsius(-1)

    def test_k_to_c_zero_is_valid(self):
        """0 K (absolute zero) is valid and must not raise."""
        result = kelvin_to_celsius(0)
        self.assertAlmostEqual(result, -273.15)


class TestConvertDispatch(unittest.TestCase):
    """Test all 9 from→to combinations via convert()."""

    def test_c_to_c(self):
        self.assertAlmostEqual(convert(25, "C", "C"), 25.0)

    def test_c_to_f(self):
        self.assertAlmostEqual(convert(100, "C", "F"), 212.0)

    def test_c_to_k(self):
        self.assertAlmostEqual(convert(0, "C", "K"), 273.15)

    def test_f_to_c(self):
        self.assertAlmostEqual(convert(32, "F", "C"), 0.0)

    def test_f_to_f(self):
        self.assertAlmostEqual(convert(98.6, "F", "F"), 98.6)

    def test_f_to_k(self):
        self.assertAlmostEqual(convert(32, "F", "K"), 273.15)

    def test_k_to_c(self):
        self.assertAlmostEqual(convert(373.15, "K", "C"), 100.0)

    def test_k_to_f(self):
        self.assertAlmostEqual(convert(273.15, "K", "F"), 32.0)

    def test_k_to_k(self):
        self.assertAlmostEqual(convert(300, "K", "K"), 300.0)

    def test_case_insensitive_lower(self):
        """Units should work in lowercase."""
        self.assertAlmostEqual(convert(100, "c", "f"), 212.0)

    def test_case_insensitive_mixed(self):
        """Units should work in mixed case."""
        self.assertAlmostEqual(convert(0, "C", "k"), 273.15)


class TestEdgeCases(unittest.TestCase):
    """Boundary values and error handling."""

    def test_negative_kelvin_via_convert_raises(self):
        with self.assertRaises(ValueError):
            convert(-1, "K", "C")

    def test_unknown_from_unit_raises(self):
        with self.assertRaises(ValueError):
            convert(100, "X", "C")

    def test_unknown_to_unit_raises(self):
        with self.assertRaises(ValueError):
            convert(100, "C", "Z")

    def test_float_input(self):
        self.assertAlmostEqual(convert(36.6, "C", "F"), 97.88, places=2)

    def test_very_large_value(self):
        """Should not raise — just returns a large number."""
        result = convert(1_000_000, "C", "F")
        self.assertGreater(result, 1_000_000)

    def test_very_negative_celsius(self):
        """Deep-space temperatures — valid in C and F."""
        result = convert(-270, "C", "K")
        self.assertAlmostEqual(result, 3.15, places=2)

    def test_absolute_zero_celsius_to_kelvin(self):
        """Absolute zero should produce exactly 0 K."""
        self.assertAlmostEqual(convert(-273.15, "C", "K"), 0.0, places=5)

    def test_whitespace_in_unit_stripped(self):
        """Units with surrounding spaces should still work."""
        self.assertAlmostEqual(convert(100, " C ", " F "), 212.0)


class TestAllConversions(unittest.TestCase):
    """Test the all_conversions() summary helper."""

    def test_returns_dict_with_three_keys(self):
        result = all_conversions(0, "C")
        self.assertSetEqual(set(result.keys()), {"C", "F", "K"})

    def test_values_are_correct(self):
        result = all_conversions(0, "C")
        self.assertAlmostEqual(result["C"], 0.0)
        self.assertAlmostEqual(result["F"], 32.0)
        self.assertAlmostEqual(result["K"], 273.15)

    def test_from_fahrenheit(self):
        result = all_conversions(212, "F")
        self.assertAlmostEqual(result["C"], 100.0)
        self.assertAlmostEqual(result["K"], 373.15)

    def test_invalid_unit_raises(self):
        with self.assertRaises(ValueError):
            all_conversions(100, "X")


if __name__ == "__main__":
    unittest.main(verbosity=2)
