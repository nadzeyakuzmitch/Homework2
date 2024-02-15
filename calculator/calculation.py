from decimal import Decimal
from typing import Callable
from calculator.operations import add, subtract, multiply, divide
from calculator.calculation import Calculation

class Calculation:
    @staticmethod
    def _perform_operation(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        calculation = Calculation.create(a, b, operation)
        return calculation.perform()

    @staticmethod
    def operate(a: Decimal, b: Decimal, operation: Callable[[Decimal, Decimal], Decimal]) -> Decimal:
        return Calculation._perform_operation(a, b, operation)

    @staticmethod
    def _operation_method(operation_func: Callable[[Decimal, Decimal], Decimal]) -> Callable[[Decimal, Decimal], Decimal]:
        return lambda a, b: Calculation.operate(a, b, operation_func)

    add = _operation_method(add)
    subtract = _operation_method(subtract)
    multiply = _operation_method(multiply)
    divide = _operation_method(divide)