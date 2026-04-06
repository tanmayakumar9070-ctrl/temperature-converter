def celsius_to_fahrenheit(c):
    """Convert Celsius to Fahrenheit."""
    return (c * 9 / 5) + 32

def fahrenheit_to_celsius(f):
    """Convert Fahrenheit to Celsius."""
    return (f - 32) * 5 / 9

def celsius_to_kelvin(c):
    """Convert Celsius to Kelvin."""
    return c + 273.15

def kelvin_to_celsius(k):
    """Convert Kelvin to Celsius."""
    if k < 0:
        raise ValueError("Kelvin cannot be negative.")
    return k - 273.15

def convert(value, from_unit, to_unit):
    """Universal converter. Supports C, F, K."""
    from_unit = from_unit.upper()
    to_unit   = to_unit.upper()

    # First convert everything to Celsius
    if from_unit == "C":
        celsius = value
    elif from_unit == "F":
        celsius = fahrenheit_to_celsius(value)
    elif from_unit == "K":
        celsius = kelvin_to_celsius(value)
    else:
        raise ValueError(f"Unknown unit: {from_unit}")

    # Then convert from Celsius to target
    if to_unit == "C":
        return celsius
    elif to_unit == "F":
        return celsius_to_fahrenheit(celsius)
    elif to_unit == "K":
        return celsius_to_kelvin(celsius)
    else:
        raise ValueError(f"Unknown unit: {to_unit}")