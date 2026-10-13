"""Unit tests for the statistics tool."""
import pytest
from app.tools.statistics import statistics_calculator


def test_mean():
    result = statistics_calculator.invoke({"numbers": [1.0, 2.0, 3.0, 4.0, 5.0], "measure": "mean"})
    assert "3" in result


def test_median():
    result = statistics_calculator.invoke({"numbers": [1.0, 2.0, 3.0, 4.0, 5.0], "measure": "median"})
    assert "3" in result


def test_mode():
    result = statistics_calculator.invoke({"numbers": [1.0, 2.0, 2.0, 3.0], "measure": "mode"})
    assert "2" in result


def test_variance():
    result = statistics_calculator.invoke({"numbers": [2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0], "measure": "variance"})
    assert "4" in result


def test_stdev():
    result = statistics_calculator.invoke({"numbers": [2.0, 4.0, 4.0, 4.0, 5.0, 5.0, 7.0, 9.0], "measure": "stdev"})
    assert "2" in result


def test_min():
    result = statistics_calculator.invoke({"numbers": [5.0, 3.0, 8.0, 1.0, 9.0], "measure": "min"})
    assert "1" in result


def test_max():
    result = statistics_calculator.invoke({"numbers": [5.0, 3.0, 8.0, 1.0, 9.0], "measure": "max"})
    assert "9" in result


def test_empty_list():
    result = statistics_calculator.invoke({"numbers": [], "measure": "mean"})
    assert "Error" in result
    assert "empty" in result.lower()


def test_single_value_mean():
    result = statistics_calculator.invoke({"numbers": [42.0], "measure": "mean"})
    assert "42" in result


def test_variance_requires_two_numbers():
    result = statistics_calculator.invoke({"numbers": [5.0], "measure": "variance"})
    assert "Error" in result


def test_unknown_measure():
    result = statistics_calculator.invoke({"numbers": [1.0, 2.0, 3.0], "measure": "kurtosis"})
    assert "Error" in result
    assert "Unknown measure" in result
