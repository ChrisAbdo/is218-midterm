from typing import List
from .calculations import Calculations

class Functions:
    calculation_history: List[Calculations] = []

    @classmethod
    def register(cls, calculation: Calculations):
        cls.calculation_history.append(calculation)

    @classmethod
    def history(cls) -> List[Calculations]:
        return cls.calculation_history

    @classmethod
    def clear(cls):
        cls.calculation_history.clear()

    @classmethod
    def last(cls) -> Calculations:
        return cls.calculation_history[-1] if cls.calculation_history else None