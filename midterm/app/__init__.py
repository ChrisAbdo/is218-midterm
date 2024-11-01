import os
import pkgutil
import importlib
from app.commands import CommandHandler
from app.commands import Command
from dotenv import load_dotenv
import logging
import logging.config

class App:
    def __init__(self):
        self.command_handler = CommandHandler()
        os.makedirs('logs', exist_ok=True)
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.settings.setdefault('ENVIRONMENT', 'PRODUCTION')
        
    def configure_logging(self):
        logging_conf_path = 'logging.conf'
        if os.path.exists(logging_conf_path):
            logging.config.fileConfig(logging_conf_path, disable_existing_loggers=False)
        else:
            logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_environment_variables(self):
        settings = {key: value for key, value in os.environ.items()}
        # print(settings)
        logging.info("Environment variables loaded.")
        return settings

    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        return self.settings.get(env_var, None)

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