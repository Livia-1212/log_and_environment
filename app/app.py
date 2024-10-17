# Class APP to hold major logic to register commands

import os
import sys
import logging
from dotenv import load_dotenv, dotenv_values
from app.commands.command_handler import CommandHandler
from app.commands.commands.calc_commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand
from app.plugins.greet import GreetCommand

class App:
    def __init__(self):
        self.configure_logging()
        load_dotenv()
        self.settings = self.load_environment_variables()
        self.command_handler = CommandHandler()
        self.register_commands()  # Register commands here

        #access the environment variables
        database_url = os.getenv("DATABASE_URL")
        api_key = os.getenv("API_KEY")
        environment = os.getenv("ENVIRONMENT")

        #print the environment variables. Not a necessary step, only to check if environment variables are accessed
        print(f"Database URL: {database_url}")
        print(f"API Key: {api_key}")
        print(f"Environment: {environment}")



    def configure_logging(self):
        logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
        logging.info("Logging configured.")

    def load_environment_variables(self):
        """Load environment variables into a dictionary."""
        return {key: value for key, value in os.environ.items()}
    
    def get_environment_variable(self, env_var: str = 'ENVIRONMENT'):
        """Retrieve the value of a specified environment variable."""
        return self.settings.get(env_var, None)

    def register_commands(self):
        """Register calculator commands."""
        self.command_handler.register_command('add', AddCommand())
        self.command_handler.register_command('subtract', SubtractCommand())
        self.command_handler.register_command('multiply', MultiplyCommand())
        self.command_handler.register_command('divide', DivideCommand())
        self.command_handler.register_command('greet', GreetCommand())

    def start(self):
        """Start the REPL for user interaction."""
        logging.info("Application started. Type 'exit' to exit.")
        print("Enter 'add', 'subtract', 'multiply', or 'divide' followed by two numbers to perform a calculation.")
        print("Or enter 'greet' to receive a greeting.")
        
        while True:
            user_input = input(">>> ").strip().split()  # Prompt user for input
            command_name = user_input[0].lower()  # Get the command name

            if command_name == 'exit':
                logging.info("Exiting application.")
                sys.exit(0)
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
