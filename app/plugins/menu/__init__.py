from app.commands import Command

class MenuCommand(Command):
    def execute(self, args):
        print("\nAvailable commands:")
        print("- add <num1> <num2>")
        print("- subtract <num1> <num2>")
        print("- multiply <num1> <num2>")
        print("- divide <num1> <num2>")
        print("- history")
        print("- clear_history")
        print("- delete_history <index>")
        print("- menu (display this menu)")
        print("- exit (quit the app)")