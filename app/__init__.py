import pkgutil
import importlib
from dotenv import load_dotenv
from app.commands import CommandHandler
from app.commands import Command

class App:
    def __init__(self):
        self.command_handler = CommandHandler()
        self.command_handler = CommandHandler()

    def load_plugins(self):
        plugins_package = "app.plugins"
        for _, plugin_name, is_pkg in pkgutil.iter_modules(
            [plugins_package.replace(".", "/")]
        ):
            if is_pkg:
                plugin_module = importlib.import_module(
                    f"{plugins_package}.{plugin_name}"
                )
                for item_name in dir(plugin_module):
                    item = getattr(plugin_module, item_name)
                    try:
                        if issubclass(item, (Command)):
                            self.command_handler.register_command(plugin_name, item())
                    except TypeError:
                        continue

    def start(self):
        self.load_plugins()
        self.command_handler.execute_command("menu", [])

        while True:
            input_line = input(">>> ").strip()
            if not input_line:
                continue
            parts = input_line.split()
            command_name = parts[0].lower()
            args = parts[1:]
            if command_name == "exit":
                print("Goodbye!")
                break
            else:
                self.command_handler.execute_command(command_name, args)