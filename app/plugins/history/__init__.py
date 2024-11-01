from app.commands import Command
from app.calculator.calculations import Calculations

class HistoryCommand(Command):
    def execute(self, args):
        history = Calculations.history()
        if not history:
            print("No calculations have been performed yet.")
        else:
            for index, calc in enumerate(history, start=1):
                op_name = calc.op.__name__
                result = calc.execute_calculation()
                print(f"{index}: {calc.num1} {op_name} {calc.num2} = {result}")