from app.commands import Command

class MenuCommand(Command):
    def execute(self, args):
        print("\nAvailable commands:")
        print("- add")
        print("- subtract")
        print("- multiply")
        print("- divide")
        print("- history")
        print("- menu (display this menu)")
        print("- exit (quit the app)")