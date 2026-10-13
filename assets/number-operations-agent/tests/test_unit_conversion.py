"""Unit tests for the unit conversion tool."""
import pytest
from app.tools.unit_conversion import unit_conversion


def test_length_km_to_miles():
    result = unit_conversion.invoke({"value": 1.0, "from_unit": "km", "to_unit": "miles"})
    assert "0.621" in result


def test_length_meters_to_feet():
    result = unit_conversion.invoke({"value": 1.0, "from_unit": "m", "to_unit": "ft"})
    assert "3.28" in result


def test_weight_kg_to_lb():
    result = unit_conversion.invoke({"value": 1.0, "from_unit": "kg", "to_unit": "lb"})
    assert "2.204" in result


def test_weight_g_to_oz():
    result = unit_conversion.invoke({"value": 100.0, "from_unit": "g", "to_unit": "oz"})
    assert "3.5" in result


def test_temperature_c_to_f():
    result = unit_conversion.invoke({"value": 100.0, "from_unit": "C", "to_unit": "F"})
    assert "212" in result


def test_temperature_f_to_c():
    result = unit_conversion.invoke({"value": 32.0, "from_unit": "F", "to_unit": "C"})
    assert "0" in result


def test_temperature_c_to_k():
    result = unit_conversion.invoke({"value": 0.0, "from_unit": "C", "to_unit": "K"})
    assert "273.15" in result


def test_volume_liters_to_gallons():
    result = unit_conversion.invoke({"value": 1.0, "from_unit": "l", "to_unit": "gal"})
    assert "0.264" in result


def test_unsupported_unit_pair():
    result = unit_conversion.invoke({"value": 10.0, "from_unit": "km", "to_unit": "kg"})
    assert "Error" in result
    assert "same category" in result


def test_unknown_units():
    result = unit_conversion.invoke({"value": 5.0, "from_unit": "parsec", "to_unit": "lightyear"})
    assert "Error" in result
