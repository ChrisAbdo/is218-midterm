from typing import List, Callable
from decimal import Decimal

class Calculations:
    calculation_history: List['Calculations'] = []

    def __init__(self, num1: Decimal, num2: Decimal, op: Callable[[Decimal, Decimal], Decimal]):
        self.num1 = num1
        self.num2 = num2
        self.op = op
        self.result = None
    
    @staticmethod
    def create(num1: Decimal, num2: Decimal, op: Callable[[Decimal, Decimal], Decimal]):
        calculation = Calculations(num1, num2, op)
        Calculations.calculation_history.append(calculation)
        return calculation
    
    def execute(self) -> Decimal:
        if self.result is None:
            self.result = self.op(self.num1, self.num2)
        return self.result

    @classmethod
    def history(cls) -> List['Calculations']:
        return cls.calculation_history

    @classmethod
    def clear_history(cls):
        cls.calculation_history.clear()