from decimal import Decimal
from .functions import Functions
from .calculations import Calculations
from .ops import add, subtract, multiply, divide

class Calculator:
    @staticmethod
    def add(a: Decimal, b: Decimal) -> Decimal:
        calculation = Calculations.create(a, b, add)
        Functions.register(calculation)
        return calculation.execute()

    @staticmethod
    def subtract(a: Decimal, b: Decimal) -> Decimal:
        calculation = Calculations.create(a, b, subtract)
        Functions.register(calculation)
        return calculation.execute()

    @staticmethod
    def multiply(a: Decimal, b: Decimal) -> Decimal:
        calculation = Calculations.create(a, b, multiply)
        Functions.register(calculation)
        return calculation.execute()

    @staticmethod
    def divide(a: Decimal, b: Decimal) -> Decimal:
        calculation = Calculations.create(a, b, divide)
        Functions.register(calculation)
        return calculation.execute()