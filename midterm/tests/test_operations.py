from decimal import Decimal
import pytest
from app.calculator.calculations import Calculations
from app.calculator.ops import add, subtract, multiply, divide

def test_op_add():
    calculation = Calculations.create(Decimal('10'), Decimal('5'), add)
    assert calculation.execute() == Decimal('15'), "Add operation failed"

def test_op_subtract():
    calculation = Calculations.create(Decimal('10'), Decimal('5'), subtract)
    assert calculation.execute() == Decimal('5'), "Subtract operation failed"

def test_op_multiply():
    calculation = Calculations.create(Decimal('10'), Decimal('5'), multiply)
    assert calculation.execute() == Decimal('50'), "Multiply operation failed"

def test_op_divide():
    calculation = Calculations.create(Decimal('10'), Decimal('5'), divide)
    assert calculation.execute() == Decimal('2'), "Divide operation failed"

def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError, match="Cannot divide by zero."):
        calculation = Calculations.create(Decimal('10'), Decimal('0'), divide)
        calculation.execute()