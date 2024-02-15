from decimal import Decimal
from typing import Callable, List
from calculator.calculation import Calculation

class Calculations:
    history: List[Calculation] = []

    @classmethod
    def add_calculation(cls, calculation: Calculation):
        cls.history.append(calculation)

    @classmethod
    def get_history(cls) -> List[Calculation]:
        return cls.history

    @classmethod
    def clear_history(cls):
        cls.history.clear()

    @classmethod
    def get_latest(cls) -> Calculation:
        if cls.history:
            return cls.history[-1]
        return None

    @classmethod
    def _create_find_by_operation(cls, operation_name: str) -> Callable[..., List[Calculation]]:
        def find_by_operation() -> List[Calculation]:
            return [calc for calc in cls.history if calc.operation.__name__ == operation_name]
        return classmethod(find_by_operation)

    for operation_name in ['add', 'subtract', 'multiply', 'divide']:
        locals()[f'find_by_{operation_name}'] = _create_find_by_operation(operation_name)

