# app/commands/command_handler.py
import logging
import os
import pkgutil
import importlib
from app.commands.commands import Command  # Ensure Command is imported

class CommandHandler:
    def __init__(self):
        self.commands = {}

    def register_command(self, command_name: str, command: Command):
        """Register a new command with a given name."""
        self.commands[command_name] = command
        logging.info(f"Command '{command_name}' registered successfully.")

    def execute_command(self, command_name: str, *args):
        """Execute the command based on the command name and provided arguments."""
        if command_name not in self.commands:
            logging.error(f"No such command: {command_name}")
            print(f"No such command: {command_name}")
            return None

        try:
            result = self.commands[command_name].execute(*args)
            return result
        except Exception as e:
            logging.error(f"An error occurred while executing '{command_name}': {e}")
            print(f"Error: {e}")  # Print error to user

    def load_commands(self):
        """Dynamically load command classes from plugins."""
        for package in os.listdir('app/plugins'):
            package_path = f'app.plugins.{package}'
            try:
                # Import the plugin module
                plugin_module = importlib.import_module(package_path)

                # Register commands from the plugin
                for command in dir(plugin_module):
                    cmd_class = getattr(plugin_module, command)
                    if isinstance(cmd_class, type) and issubclass(cmd_class, Command):
                        self.register_command(command.lower(), cmd_class())
            except ImportError as e:
                logging.error(f"Failed to load plugin '{package}': {e}")
