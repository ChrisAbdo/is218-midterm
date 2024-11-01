from app.commands import Command

class MenuCommand(Command):
    def execute(self, args):
        print("\nAvailable commands:")
        print("- add")
        print("- subtract")
        print("- multiply")
        print("- divide")
        print("- history")
        print("- pandas (append calculation history to pandas.csv)")
        print("- pandas-history (display calculation history from pandas.csv)")
        print("- pandas-clear (clear all calculations from pandas.csv)")
        print("- menu (display this menu)")
        print("- exit (quit the app)")