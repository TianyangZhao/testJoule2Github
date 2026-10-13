"""Unit tests for the arithmetic tool."""
import pytest
from app.tools.arithmetic import arithmetic


def test_add():
    result = arithmetic.invoke({"operation": "add", "a": 10.0, "b": 5.0})
    assert "15" in result


def test_subtract():
    result = arithmetic.invoke({"operation": "subtract", "a": 10.0, "b": 3.0})
    assert "7" in result


def test_multiply():
    result = arithmetic.invoke({"operation": "multiply", "a": 4.0, "b": 6.0})
    assert "24" in result


def test_divide():
    result = arithmetic.invoke({"operation": "divide", "a": 15.0, "b": 3.0})
    assert "5" in result


def test_divide_by_zero():
    result = arithmetic.invoke({"operation": "divide", "a": 10.0, "b": 0.0})
    assert "Error" in result
    assert "zero" in result.lower()


def test_power():
    result = arithmetic.invoke({"operation": "power", "a": 2.0, "b": 8.0})
    assert "256" in result


def test_modulo():
    result = arithmetic.invoke({"operation": "modulo", "a": 17.0, "b": 5.0})
    assert "2" in result


def test_modulo_by_zero():
    result = arithmetic.invoke({"operation": "modulo", "a": 10.0, "b": 0.0})
    assert "Error" in result


def test_unknown_operation():
    result = arithmetic.invoke({"operation": "sqrt", "a": 9.0, "b": 0.0})
    assert "Error" in result
    assert "Unknown operation" in result
