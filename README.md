# IS218 Midterm

## Demo Video

[![Demo Video](https://img.youtube.com/vi/1Q1Q1Q1Q1Q1Q/0.jpg)](https://www.youtube.com/watch?v=1Q1Q1Q1Q1Q1Q)

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

### Design Patterns

This project uses a Command Pattern to encapsulate a request as an object, allowing for the parameterization of clients with different requests. This pattern is implemented with the `Command` class and its subclasses, which represent different operations that can be performed by the calculator.

The app is set up in a way that allows continuous development and easy integration of new plugins without affecting the main system. The `Command` class can be extended to add new operations, and the `menu` command will automatically display the new commands.

### Environment Variables

This app uses `python-dotenv` to load environment variables from the `.env` file. The env file contains the following variables:

```env
ENVIRONMENT=x
DATABASE_USERNAME=x
```

The env variables primarily effect the logging in this application. The `ENVIRONMENT` variable is used to determine the logging level. If the environment is set to `development`, the logging level will be set to `DEBUG`. If the environment is set to `production`, the logging level will be set to `INFO`. The `DATABASE_USERNAME` variable is used to determine the username for the database connection. (also just placeholder for now)

### Logging

I set up the logging in a comprehensive manner to capture as much valuable information as possible. The logging is set up to capture the following:

- The time the log was created
- The log level
- The message
- The name of the logger

The logs are differentiated between INFO, WARNING, ERROR. If an error occurs, the logger will capture the error and log it to the log file. The log file is named `app.log` and is located in the root directory of the project. Similarly, the logger will also log successful operations and warnings to the file to give a comprehensive view of the application's operations and what is happening.

The logging configuration is setup in logging.conf in the root directory of the project. The logging configuration is set up to log to the console and to the log file.

### LBYL / EAFP

I implemented LBYL by checking the number of arguments passed to a command. If the number of arguments is incorrect, the application will raise an error. This is done in the `Command` class. An example would be this in the logs:

```log
2024-11-01 15:02:45,294 - root - WARNING - Invalid number of arguments: []
2024-11-01 15:02:45,295 - root - INFO - Executed command: add with args: []. Result: Usage: command <number1> <number2>
```

I implemented EAFP mainly in the division operation. If the user tries to divide by zero, the application will raise an error and log the error. This is done in the `divide` method in the `Command` class. An example would be this in the logs:

```log
2024-11-01 15:03:28,629 - root - INFO - Executed command: divide with args: ['12', '0']. Result: Cannot divide by zero
```

##### Built by Chris Abdo
