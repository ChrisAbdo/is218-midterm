"""
This module contains tests for the calculator module.
"""

from decimal import Decimal
from app import App
from app.calculator.calculations import Calculations

def app():
    return App()

def test_addition(app, capfd, monkeypatch):
    """
    Test that the add command returns the expected result
    """
    inputs = iter(['add 2 3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app.start()
    out, _ = capfd.readouterr()
    assert "5" in out

def test_subtraction(app, capfd, monkeypatch):
    """
    Test that the subtract command returns the expected result
    """
    inputs = iter(['subtract 5 3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app.start()
    out, _ = capfd.readouterr()
    assert "2" in out

def test_multiplication(app, capfd, monkeypatch):
    """
    Test that the multiply command returns the expected result
    """
    inputs = iter(['multiply 2 3', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app.start()
    out, _ = capfd.readouterr()
    assert "6" in out

def test_division(app, capfd, monkeypatch):
    """
    Test that the divide command returns the expected result
    """
    inputs = iter(['divide 6 2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app.start()
    out, _ = capfd.readouterr()
    assert "3" in out

def test_divide_by_zero(app, capfd, monkeypatch):
    """
    Test that dividing by zero raises an error message
    """
    inputs = iter(['divide 5 0', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app.start()
    out, _ = capfd.readouterr()
    assert "Cannot divide by zero" in out

def test_history(app, capfd, monkeypatch):
    """
    Test that the history contains the expected number of calculations
    """
    Calculations.clear_history()  # Clear history before the test
    inputs = iter(['add 1 1', 'subtract 5 3', 'multiply 2 4', 'divide 8 2', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app.start()
    assert len(Calculations.history()) == 4

def test_clear_history(app):
    """
    Test that the history is cleared
    """
    Calculations.clear_history()
    assert len(Calculations.history()) == 0

def test_history_command(app, capfd, monkeypatch):
    """
    Test that the 'history' command outputs the expected calculation history.
    """
    from app.calculator.calculations import Calculations
    Calculations.clear_history()

    inputs = iter([
        'add 2 3',
        'subtract 5 2',
        'multiply 3 4',
        'divide 10 2',
        'history',
        'exit'
    ])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app.start()
    out, _ = capfd.readouterr()

    expected_history = [
        "1: 2 add 3 = 5",
        "2: 5 subtract 2 = 3",
        "3: 3 multiply 4 = 12",
        "4: 10 divide 2 = 5",
    ]

    for expected_line in expected_history:
        assert expected_line in out, f"Expected '{expected_line}' in output"

    assert "No calculations have been performed yet." not in out, "History should not be empty"