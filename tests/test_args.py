import pytest
from decimal import Decimal
from app.plugins.args import get_args

def test_get_args_valid():
    result = get_args(['5', '3'])
    assert result == (Decimal('5'), Decimal('3'))

def test_get_args_invalid_number():
    with pytest.raises(ValueError, match="Invalid number format"):
        get_args(['a', '3'])

def test_get_args_too_few_args():
    with pytest.raises(ValueError, match="Usage: command <number1> <number2>"):
        get_args(['5'])

def test_get_args_too_many_args():
    with pytest.raises(ValueError, match="Usage: command <number1> <number2>"):
        get_args(['5', '3', '2'])

def test_get_args_empty():
    with pytest.raises(ValueError, match="Usage: command <number1> <number2>"):
        get_args([])