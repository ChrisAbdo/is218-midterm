import logging
from app.commands import Command
import pandas as pd
import os

class PandasHistoryCommand(Command):
    def execute(self, args):
        file_path = 'pandas.csv'

        if not os.path.exists(file_path):
            print("No pandas history file found.")
            return "No pandas history file found."

        try:
            df = pd.read_csv(file_path)
            if df.empty:
                print("The pandas history file is empty.")
                logging.warning("The pandas history file is empty.")
                return "The pandas history file is empty."

            print("\nPandas History:")
            for index, row in df.iterrows():
                print(f"{index + 1}: {row['Number1']} {row['Operation']} {row['Number2']} = {row['Result']}")

            logging.info("Pandas history displayed successfully.")
            return "Pandas history displayed successfully."
        except Exception as e:
            print(f"Error reading pandas history: {str(e)}")
            logging.error(f"Error reading pandas history: {str(e)}")
            return f"Error reading pandas history: {str(e)}"