from decimal import Decimal
import pytest
from app.calculator.calculations import Calculations
from app.calculator.ops import add, subtract, multiply, divide

def test_ops(a, b, operation, expected):
    calc = Calculations.create(Decimal(str(a)), Decimal(str(b)), operation)
    assert calc.execute() == Decimal(str(expected)), f"Failed {operation.__name__}"

def test_divide_by_zero():
    calc = Calculations.create(Decimal('10'), Decimal('0'), divide)
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero."):
        calc.execute()