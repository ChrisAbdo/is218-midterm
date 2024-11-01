from app.commands import Command
from app.calculator import Calculator
from app.plugins.args import get_args

class AddCommand(Command):
    def execute(self, args):
        try:
            num1, num2 = get_args(args)
            result = Calculator.add(num1, num2)
            print(result)
            return result
        except ValueError as e:
            print(str(e))
            return str(e)