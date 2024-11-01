import pandas as pd
from decimal import Decimal
from typing import List, Dict

class PandasOperations:
    @staticmethod
    def save_history(history: List[Dict]) -> None:
        df = pd.DataFrame(history)
        df.to_csv('calculation_history.csv', index=False)

    @staticmethod
    def load_history() -> List[Dict]:
        try:
            df = pd.read_csv('calculation_history.csv')
            return df.to_dict('records')
        except FileNotFoundError:
            return []

    @staticmethod
    def clear_history() -> None:
        pd.DataFrame(columns=['num1', 'num2', 'operation', 'result']).to_csv('calculation_history.csv', index=False)

    @staticmethod
    def delete_record(index: int) -> None:
        df = pd.read_csv('calculation_history.csv')
        df = df.drop(index)
        df.to_csv('calculation_history.csv', index=False)