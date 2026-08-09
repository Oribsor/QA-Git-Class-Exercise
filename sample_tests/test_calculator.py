"""Sample test cases for calculator.py.

Each student adds ONE new test function below,
named: test_<something>_<your_name>
Run the tests locally with:  pytest sample_tests/
"""
from calculator import add, subtract, multiply, divide
import pytest


def test_add_two_positive_numbers():
    assert add(2, 3) == 5


def test_subtract_returns_negative():
    assert subtract(3, 10) == -7


def test_multiply_by_zero():
    assert multiply(99, 0) == 0


def test_divide_by_zero_raises_error():
    with pytest.raises(ValueError):
        divide(10, 0)

# === Add your test below this line ===
