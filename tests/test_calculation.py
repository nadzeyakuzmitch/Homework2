from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

def perform_calculation_test(a, b, operation, expected):
   
    calc = Calculation(a, b, operation)
    assert calc.perform() == expected, f"Failed {operation.__name__} operation with {a} and {b}"

def create_calculation_test_cases():
   
    test_cases = [
        (Decimal('10'), Decimal('5'), add, Decimal('15')),  # Test addition
        (Decimal('10'), Decimal('5'), subtract, Decimal('5')),  # Test subtraction
        (Decimal('10'), Decimal('5'), multiply, Decimal('50')),  # Test multiplication
        (Decimal('10'), Decimal('2'), divide, Decimal('5')),  # Test division
        (Decimal('10.5'), Decimal('0.5'), add, Decimal('11.0')),  # Test addition with decimals
        (Decimal('10.5'), Decimal('0.5'), subtract, Decimal('10.0')),  # Test subtraction with decimals
        (Decimal('10.5'), Decimal('2'), multiply, Decimal('21.0')),  # Test multiplication with decimals
        (Decimal('10'), Decimal('0.5'), divide, Decimal('20')),  # Test division with decimals
    ]
    return test_cases

@pytest.mark.parametrize("a, b, operation, expected", create_calculation_test_cases())
def test_calculation_operations(a, b, operation, expected):
    perform_calculation_test(a, b, operation, expected)

def test_calculation_repr():
    calc = Calculation(Decimal('10'), Decimal('5'), add)
    expected_repr = "Calculation(10, 5, add)"
    assert calc.__repr__() == expected_repr, "The __repr__ method output does not match the expected string."

def test_divide_by_zero():
    calc = Calculation(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ValueError, match="Cannot divide by zero"):
        calc.perform()
