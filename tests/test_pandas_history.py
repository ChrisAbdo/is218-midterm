# chatgpt helped me with this code. i could not figure out why my test was not working
import pytest
from unittest.mock import patch, mock_open
import pandas as pd
from app.plugins.pandas_history import PandasHistoryCommand

@pytest.fixture
def pandas_history_command():
    return PandasHistoryCommand()

def test_pandas_history_no_file(pandas_history_command, capfd):
    with patch('os.path.exists', return_value=False):
        result = pandas_history_command.execute([])
        captured = capfd.readouterr()
        assert result == "No pandas history file found."
        assert "No pandas history file found." in captured.out

def test_pandas_history_empty_file(pandas_history_command, capfd):
    with patch('os.path.exists', return_value=True):
        with patch('pandas.read_csv', return_value=pd.DataFrame()):
            result = pandas_history_command.execute([])
            captured = capfd.readouterr()
            assert result == "The pandas history file is empty."
            assert "The pandas history file is empty." in captured.out

def test_pandas_history_with_data(pandas_history_command, capfd):
    test_data = pd.DataFrame({
        'Number1': [2, 5],
        'Operation': ['add', 'multiply'],
        'Number2': [3, 4],
        'Result': [5, 20]
    })
    with patch('os.path.exists', return_value=True):
        with patch('pandas.read_csv', return_value=test_data):
            result = pandas_history_command.execute([])
            captured = capfd.readouterr()
            assert result == "Pandas history displayed successfully."
            assert "1: 2 add 3 = 5" in captured.out
            assert "2: 5 multiply 4 = 20" in captured.out

def test_pandas_history_file_error(pandas_history_command, capfd):
    with patch('os.path.exists', return_value=True):
        with patch('pandas.read_csv', side_effect=Exception("Test error")):
            result = pandas_history_command.execute([])
            captured = capfd.readouterr()
            assert "Error reading pandas history: Test error" in result
            assert "Error reading pandas history: Test error" in captured.out