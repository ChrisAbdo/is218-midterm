from decimal import Decimal, InvalidOperation
from app.commands import Command
from app.calculator import Calculator
from app.plugins.args import get_args

class MultiplyCommand(Command):
    def execute(self, args):
        try:
            num1, num2 = get_args(args)
            result = Calculator.multiply(num1, num2)
            print(result)
            return result
        except InvalidOperation:
            print("Invalid input. Please enter numeric values.")
            return "Invalid input. Please enter numeric values."