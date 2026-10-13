"""Unit conversion tool for length, weight, temperature, and volume conversions."""

from langchain_core.tools import tool

# Conversion factors relative to a base SI unit
LENGTH_TO_METERS = {
    "m": 1.0, "meter": 1.0, "meters": 1.0,
    "km": 1000.0, "kilometer": 1000.0, "kilometers": 1000.0,
    "cm": 0.01, "centimeter": 0.01, "centimeters": 0.01,
    "mm": 0.001, "millimeter": 0.001, "millimeters": 0.001,
    "ft": 0.3048, "foot": 0.3048, "feet": 0.3048,
    "in": 0.0254, "inch": 0.0254, "inches": 0.0254,
    "mi": 1609.344, "mile": 1609.344, "miles": 1609.344,
    "yd": 0.9144, "yard": 0.9144, "yards": 0.9144,
}

WEIGHT_TO_KG = {
    "kg": 1.0, "kilogram": 1.0, "kilograms": 1.0,
    "g": 0.001, "gram": 0.001, "grams": 0.001,
    "mg": 0.000001, "milligram": 0.000001, "milligrams": 0.000001,
    "lb": 0.453592, "pound": 0.453592, "pounds": 0.453592,
    "oz": 0.0283495, "ounce": 0.0283495, "ounces": 0.0283495,
    "t": 1000.0, "tonne": 1000.0, "metric ton": 1000.0,
}

VOLUME_TO_LITERS = {
    "l": 1.0, "liter": 1.0, "liters": 1.0, "litre": 1.0, "litres": 1.0,
    "ml": 0.001, "milliliter": 0.001, "milliliters": 0.001,
    "gal": 3.78541, "gallon": 3.78541, "gallons": 3.78541,
    "qt": 0.946353, "quart": 0.946353, "quarts": 0.946353,
    "pt": 0.473176, "pint": 0.473176, "pints": 0.473176,
    "fl oz": 0.0295735, "fluid ounce": 0.0295735, "fluid ounces": 0.0295735,
    "cup": 0.236588, "cups": 0.236588,
}


def _convert_temperature(value: float, from_unit: str, to_unit: str) -> str:
    """Convert temperature between Celsius, Fahrenheit, and Kelvin."""
    from_unit = from_unit.strip().lower().replace("°", "").replace("degrees ", "")
    to_unit = to_unit.strip().lower().replace("°", "").replace("degrees ", "")

    # Convert to Celsius first
    if from_unit in ("c", "celsius"):
        celsius = value
    elif from_unit in ("f", "fahrenheit"):
        celsius = (value - 32) * 5 / 9
    elif from_unit in ("k", "kelvin"):
        celsius = value - 273.15
    else:
        return None

    # Convert from Celsius to target
    if to_unit in ("c", "celsius"):
        result = celsius
        unit_label = "°C"
    elif to_unit in ("f", "fahrenheit"):
        result = celsius * 9 / 5 + 32
        unit_label = "°F"
    elif to_unit in ("k", "kelvin"):
        result = celsius + 273.15
        unit_label = "K"
    else:
        return None

    return f"{value} {from_unit.upper()} = {round(result, 6)} {unit_label}"


@tool
def unit_conversion(value: float, from_unit: str, to_unit: str) -> str:
    """Convert a value from one unit to another.

    Supported categories:
    - Length: m, km, cm, mm, ft, in, mi, yd
    - Weight: kg, g, mg, lb, oz, t
    - Temperature: C, F, K (Celsius, Fahrenheit, Kelvin)
    - Volume: l, ml, gal, qt, pt, fl oz, cup

    Args:
        value: Numeric value to convert
        from_unit: Source unit (e.g. 'km', 'kg', 'C', 'gal')
        to_unit: Target unit (e.g. 'mi', 'lb', 'F', 'l')

    Returns:
        Converted value with units as a string.
    """
    from_key = from_unit.strip().lower()
    to_key = to_unit.strip().lower()

    # Temperature (special case)
    temp_result = _convert_temperature(value, from_key, to_key)
    if temp_result is not None:
        return temp_result

    # Length
    if from_key in LENGTH_TO_METERS and to_key in LENGTH_TO_METERS:
        base = value * LENGTH_TO_METERS[from_key]
        result = base / LENGTH_TO_METERS[to_key]
        return f"{value} {from_unit} = {round(result, 6)} {to_unit}"

    # Weight
    if from_key in WEIGHT_TO_KG and to_key in WEIGHT_TO_KG:
        base = value * WEIGHT_TO_KG[from_key]
        result = base / WEIGHT_TO_KG[to_key]
        return f"{value} {from_unit} = {round(result, 6)} {to_unit}"

    # Volume
    if from_key in VOLUME_TO_LITERS and to_key in VOLUME_TO_LITERS:
        base = value * VOLUME_TO_LITERS[from_key]
        result = base / VOLUME_TO_LITERS[to_key]
        return f"{value} {from_unit} = {round(result, 6)} {to_unit}"

    # Mixed or unknown units
    return (
        f"Error: Cannot convert from '{from_unit}' to '{to_unit}'. "
        "Both units must be in the same category (length, weight, temperature, or volume). "
        "Check supported units: length (m, km, cm, mm, ft, in, mi, yd), "
        "weight (kg, g, mg, lb, oz, t), temperature (C, F, K), "
        "volume (l, ml, gal, qt, pt, fl oz, cup)."
    )
