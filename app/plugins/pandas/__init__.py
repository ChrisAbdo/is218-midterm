import logging
from app.commands import Command
import pandas as pd
from app.calculator.calculations import Calculations
import os

# i kept getting a weird issue with my columns so i had chatgpt help me out with this

class PandasCommand(Command):
    def execute(self, args):
        file_path = 'pandas.csv'
        history = Calculations.history()

        if not history:
            print("No calculations in history to write.")
            logging.warning("No calculations in history to write.")
            return "No calculations in history to write."

        data = []
        for calc in history:
            data.append({
                'Number1': float(calc.num1),
                'Operation': calc.op.__name__,
                'Number2': float(calc.num2),
                'Result': float(calc.execute())
            })

        new_df = pd.DataFrame(data)

        if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
            try:
                existing_df = pd.read_csv(file_path)
                combined_df = pd.concat([existing_df, new_df], ignore_index=True)
            except pd.errors.EmptyDataError:
                combined_df = new_df
        else:
            combined_df = new_df

        combined_df.to_csv(file_path, index=False)

        print(f"Calculation history appended to {file_path}")
        logging.info(f"Calculation history appended to {file_path}")
        return f"Calculation history appended to {file_path}"