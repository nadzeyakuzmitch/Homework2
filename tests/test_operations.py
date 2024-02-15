from decimal import Decimal
import pytest
from calculator.calculation import Calculation
from calculator.operations import add, subtract, multiply, divide

test_cases = [
    (Decimal('10'), Decimal('5'), add, Decimal('15'), "Add operation failed"),
    (Decimal('10'), Decimal('5'), subtract, Decimal('5'), "Subtract operation failed"),
    (Decimal('10'), Decimal('5'), multiply, Decimal('50'), "Multiply operation failed"),
    (Decimal('10'), Decimal('5'), divide, Decimal('2'), "Divide operation failed"),
    (Decimal('10'), Decimal('0'), divide, None, "Expected ValueError for divide by zero"),
]

@pytest.mark.parametrize("a, b, operation, expected, error_message", test_cases)
def test_operations(a, b, operation, expected, error_message):
    """Test arithmetic operations with different operands and operations."""
    if expected is not None:
        calculation = Calculation(a, b, operation)
        assert calculation.perform() == expected, error_message
    else:
        with pytest.raises(ValueError, match="Cannot divide by zero"):
            calculation = Calculation(a, b, operation)
            calculation.perform()
