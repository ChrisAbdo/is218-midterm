import logging
from app.commands import Command
import pandas as pd
import os

class PandasClearCommand(Command):
    def execute(self, args):
        file_path = 'pandas.csv'

        if os.path.exists(file_path):
            # Clear the file by writing an empty DataFrame
            pd.DataFrame(columns=['Number1', 'Operation', 'Number2', 'Result']).to_csv(file_path, index=False)
            print(f"Pandas history file {file_path} has been cleared.")
            logging.info(f"Pandas history file {file_path} has been cleared.")
            return f"Pandas history file {file_path} has been cleared."
        else:
            print(f"No pandas history file found at {file_path}.")
            logging.warning(f"No pandas history file found at {file_path}.")
            return f"No pandas history file found at {file_path}."