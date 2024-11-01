from app.commands import Command
from app.calculator.calculations import Calculations

class HistoryCommand(Command):
    def execute(self, args):
        history = Calculations.history()
        if not history:
            print("No calculations have been performed yet.")
        else:
            for index, calc in enumerate(history, start=1):
                print(f"{index}: {calc['num1']} {calc['operation']} {calc['num2']} = {calc['result']}")