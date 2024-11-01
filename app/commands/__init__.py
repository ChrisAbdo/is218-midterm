from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, args):
        pass

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register(self, command_name: str, command: Command):
        self.commands[command_name] = command

    def execute_command(self, command_name: str, args):
        try:
            result = self.commands[command_name].execute(args)
            return result
        except KeyError:
            error_message = f"No command: {command_name}"
            print(error_message)
        except Exception as e:
            error_message = f"Error executing command {command_name}: {str(e)}"
            print(error_message)