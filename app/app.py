# app/app.py

import os
import logging
from dotenv import load_dotenv
from app.commands.command_handler import CommandHandler
from app.commands.commands.calc_commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

class App:
    def __init__(self):
        self.configure_logging()
        load_dotenv()
        self.command_handler = CommandHandler()
        self.register_commands()  # Register commands here

    def configure_logging(self):
        logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def register_commands(self):
        """Register calculator commands."""
        self.command_handler.register_command('add', AddCommand())
        self.command_handler.register_command('subtract', SubtractCommand())
        self.command_handler.register_command('multiply', MultiplyCommand())
        self.command_handler.register_command('divide', DivideCommand())

    def start(self):
        """Start the REPL for user interaction."""
        logging.info("Application started. Type 'exit' to exit.")
        print("Enter 'add', 'subtract', 'multiply', or 'divide' followed by two numbers to perform a calculation.")
        
        while True:
            user_input = input(">>> ").strip().split()  # Prompt user for input
            command_name = user_input[0].lower()  # Get the command name

            if command_name == 'exit':
                logging.info("Exiting application.")
                break  # Exit the REPL loop

            try:
                # Extract command arguments if any
                args = list(map(int, user_input[1:]))  # Convert arguments to integers

                # Execute the command
                result = self.command_handler.execute_command(command_name, *args)

                # Optional: Print the result if the command produces one
                if result is not None:
                    print(f"Result: {result}")

            except ValueError:
                logging.error("Invalid input: Arguments must be integers.")
                print("Error: Please provide valid integer arguments.")
            except Exception as e:
                logging.error(f"An error occurred: {e}")
                print(f"Error: {e}")  # Print error to user

if __name__ == "__main__":
    app = App()  # Create an instance of the App class
    app.start()  # Start the REPL loop
