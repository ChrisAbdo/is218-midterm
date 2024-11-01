from decimal import Decimal, InvalidOperation
import logging
from app.commands import Command
from app.calculator import Calculator
from app.plugins.args import get_args

class SubtractCommand(Command):
    def execute(self, args):
        try:
            num1, num2 = get_args(args)
            result = Calculator.subtract(num1, num2)
            print(result)
            return result
        except InvalidOperation:
            print("Invalid input. Please enter numeric values.")
            logging.error(f"Invalid input: {args}")
            return "Invalid input. Please enter numeric values."