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
    """
    Universal temperature converter.
    Supports units: C (Celsius), F (Fahrenheit), K (Kelvin).

    Args:
        value (float): The temperature value to convert.
        from_unit (str): The unit to convert from ('C', 'F', or 'K').
        to_unit (str): The unit to convert to ('C', 'F', or 'K').

    Returns:
        float: The converted temperature.

    Raises:
        ValueError: If a unit is unrecognised or Kelvin is negative.
    """
    from_unit = from_unit.strip().upper()
    to_unit   = to_unit.strip().upper()

    supported = {"C", "F", "K"}
    if from_unit not in supported:
        raise ValueError(
            f"Unknown unit '{from_unit}'. Supported units: C, F, K."
        )
    if to_unit not in supported:
        raise ValueError(
            f"Unknown unit '{to_unit}'. Supported units: C, F, K."
        )

    # Step 1 — normalise everything to Celsius first
    if from_unit == "C":
        celsius = value
    elif from_unit == "F":
        celsius = fahrenheit_to_celsius(value)
    else:  # K
        celsius = kelvin_to_celsius(value)   # raises if negative

    # Step 2 — convert from Celsius to the target unit
    if to_unit == "C":
        return celsius
    elif to_unit == "F":
        return celsius_to_fahrenheit(celsius)
    else:  # K
        return celsius_to_kelvin(celsius)


def all_conversions(value, from_unit):
    """
    Return a dict of conversions from one unit to all three units.
    Useful for displaying a summary table.
    """
    from_unit = from_unit.strip().upper()
    return {
        unit: convert(value, from_unit, unit)
        for unit in ("C", "F", "K")
    }
