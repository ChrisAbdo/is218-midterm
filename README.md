# IS218 Midterm

## Installation

1. Clone the repository
   `git clone https://github.com/ChrisAbdo/is218-midterm.git`

2. Change directory to the repository
   `cd is218-midterm`

3. Install the required packages
   `pip install -r requirements.txt`

4. Run the application
   `python app.py`

## Usage

This calculator application offers a variety of operations and features:

### Basic Operations

- Addition: `add <number1> <number2>`
- Subtraction: `subtract <number1> <number2>`
- Multiplication: `multiply <number1> <number2>`
- Division: `divide <number1> <number2>`

### Additional Features

- History: View recent calculations with `history`
- Pandas Integration:
  - Save calculations to CSV: `pandas`
  - View saved calculations: `pandas-history`
  - Clear saved calculations: `pandas-clear`
- Menu: Display available commands with `menu`

### Example Usage

`>>> add 5 3`<br>
8<br><br>
`>>> multiply 4 7`<br>
28<br><br>
`>>> history`<br>
1: 5 add 3 = 8 <br>
2: 4 multiply 7 = 28 <br><br>
`>>> pandas`<br>
Calculation history appended to pandas.csv<br><br>
`>>> exit`<br>
Goodbye!

### Notes

- The application uses a REPL (Read-Eval-Print Loop) interface.
- All calculations are performed with high precision using the Decimal type.
- Division by zero is handled gracefully with an error message.
- Use the `exit` command to quit the application.

For more information on available commands, type `menu` in the application.

##### Built by Chris Abdo
