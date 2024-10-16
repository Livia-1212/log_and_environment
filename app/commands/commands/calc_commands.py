# app/commands/commands/calc_commands.py

from abc import ABC, abstractmethod

class Command(ABC):
    @abstractmethod
    def execute(self, *args):
        """Execute the command with the given arguments."""
        pass

class AddCommand(Command):
    def execute(self, a, b):
        result = a + b
        print(f"The result of adding {a} and {b} is: {result}")
        return result

class SubtractCommand(Command):
    def execute(self, a, b):
        result = a - b
        print(f"The result of subtracting {b} from {a} is: {result}")
        return result

class MultiplyCommand(Command):
    def execute(self, a, b):
        result = a * b
        print(f"The result of adding {a} and {b} is: {result}")
        return result
    
class DivideCommand(Command):
    def execute(self, a, b):
        result = a / b
        print(f"The result of adding {a} and {b} is: {result}")
        return result
