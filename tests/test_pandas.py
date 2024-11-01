# chatgpt helped me with this code. i could not figure out why my test was not working
import pytest
import pandas as pd
from unittest.mock import patch, mock_open
from app.plugins.pandas import PandasCommand
from app.calculator.calculations import Calculations
from app.calculator.ops import add, subtract, multiply, divide
from decimal import Decimal

@pytest.fixture
def pandas_command():
    return PandasCommand()

@pytest.fixture
def mock_calculations():
    Calculations.clear_history()
    Calculations.create(Decimal('2'), Decimal('3'), add)
    Calculations.create(Decimal('5'), Decimal('2'), subtract)
    return Calculations.history()

def test_pandas_no_history(pandas_command, capfd):
    Calculations.clear_history()
    result = pandas_command.execute([])
    captured = capfd.readouterr()
    assert result == "No calculations in history to write."
    assert "No calculations in history to write." in captured.out

def test_pandas_new_file(pandas_command, mock_calculations, capfd):
    with patch('os.path.exists', return_value=False):
        with patch('pandas.DataFrame.to_csv') as mock_to_csv:
            result = pandas_command.execute([])
            captured = capfd.readouterr()
            assert result == "Calculation history appended to pandas.csv"
            assert "Calculation history appended to pandas.csv" in captured.out
            mock_to_csv.assert_called_once()

def test_pandas_existing_file(pandas_command, mock_calculations, capfd):
    existing_data = pd.DataFrame({
        'Number1': [1],
        'Operation': ['multiply'],
        'Number2': [4],
        'Result': [4]
    })
    with patch('os.path.exists', return_value=True):
        with patch('os.path.getsize', return_value=100):
            with patch('pandas.read_csv', return_value=existing_data):
                with patch('pandas.DataFrame.to_csv') as mock_to_csv:
                    result = pandas_command.execute([])
                    captured = capfd.readouterr()
                    assert result == "Calculation history appended to pandas.csv"
                    assert "Calculation history appended to pandas.csv" in captured.out
                    mock_to_csv.assert_called_once()

def test_pandas_empty_existing_file(pandas_command, mock_calculations, capfd):
    with patch('os.path.exists', return_value=True):
        with patch('os.path.getsize', return_value=100):
            with patch('pandas.read_csv', side_effect=pd.errors.EmptyDataError):
                with patch('pandas.DataFrame.to_csv') as mock_to_csv:
                    result = pandas_command.execute([])
                    captured = capfd.readouterr()
                    assert result == "Calculation history appended to pandas.csv"
                    assert "Calculation history appended to pandas.csv" in captured.out
                    mock_to_csv.assert_called_once()