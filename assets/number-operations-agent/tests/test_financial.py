"""Unit tests for the financial calculator tool."""
import pytest
from app.tools.financial import financial_calculator


def test_simple_interest():
    result = financial_calculator.invoke({
        "operation": "simple_interest",
        "principal": 1000.0,
        "rate": 0.05,
        "time": 2.0,
    })
    assert "100" in result  # 1000 * 0.05 * 2 = 100


def test_compound_interest():
    result = financial_calculator.invoke({
        "operation": "compound_interest",
        "principal": 1000.0,
        "rate": 0.05,
        "time": 1.0,
        "n": 12.0,
    })
    assert "1051" in result  # approximately 1051.16


def test_compound_interest_zero_n():
    result = financial_calculator.invoke({
        "operation": "compound_interest",
        "principal": 1000.0,
        "rate": 0.05,
        "time": 1.0,
        "n": 0.0,
    })
    assert "Error" in result


def test_percentage_of():
    result = financial_calculator.invoke({
        "operation": "percentage_of",
        "part": 25.0,
        "total": 200.0,
    })
    assert "12.5" in result


def test_percentage_of_zero_total():
    result = financial_calculator.invoke({
        "operation": "percentage_of",
        "part": 10.0,
        "total": 0.0,
    })
    assert "Error" in result


def test_percent_value():
    result = financial_calculator.invoke({
        "operation": "percent_value",
        "value": 850.0,
        "percentage": 15.0,
    })
    assert "127.5" in result


def test_loan_repayment():
    result = financial_calculator.invoke({
        "operation": "loan_repayment",
        "principal": 100000.0,
        "rate": 0.06,
        "time": 30.0,
    })
    assert "Monthly payment" in result
    assert "599" in result  # approx 599.55


def test_loan_repayment_zero_interest():
    result = financial_calculator.invoke({
        "operation": "loan_repayment",
        "principal": 12000.0,
        "rate": 0.0,
        "time": 1.0,
    })
    assert "1000" in result  # 12000 / 12 = 1000


def test_unknown_operation():
    result = financial_calculator.invoke({"operation": "amortization_schedule"})
    assert "Error" in result
    assert "Unknown operation" in result
