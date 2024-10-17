# app/commands/command_handler.py
import sys
from app.commands.commands import Command
import logging

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
            sys.exit(1)  # Exit the application with a failure status

        try:
            result = self.commands[command_name].execute(*args)
            return result
        except Exception as e:
            logging.error(f"An error occurred while executing '{command_name}': {e}")
            print(f"Error: {e}")  # Print error to user
