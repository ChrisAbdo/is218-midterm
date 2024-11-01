from typing import Dict, List, Callable
from decimal import Decimal
from app.pd.operations import PandasOperations

class Calculations:
    @classmethod
    def create(cls, num1: Decimal, num2: Decimal, op: Callable[[Decimal, Decimal], Decimal]):
        calculation = cls(num1, num2, op)
        result = calculation.execute()
        history_entry = {
            'num1': str(num1),
            'num2': str(num2),
            'operation': op.__name__,
            'result': str(result)
        }
        history = PandasOperations.load_history()
        history.append(history_entry)
        PandasOperations.save_history(history)
        return calculation

    @classmethod
    def history(cls) -> List[Dict]:
        return PandasOperations.load_history()

    @classmethod
    def clear_history(cls):
        PandasOperations.clear_history()

    @classmethod
    def delete_history_record(cls, index: int):
        PandasOperations.delete_record(index)