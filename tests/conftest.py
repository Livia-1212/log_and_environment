# tests/conftest.py

import pytest
from app.commands.command_handler import CommandHandler
from app.commands.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

@pytest.fixture
def calculator():
    """Fixture to create a Calculator instance for testing."""
    return calculator()  # Ensure you have a Calculator class defined somewhere

@pytest.fixture
def command_handler(calculator):
    """Fixture to create a CommandHandler linked to a Calculator instance."""
    handler = CommandHandler()
    handler.register_command('add', AddCommand())
    handler.register_command('subtract', SubtractCommand())
    handler.register_command('multiply', MultiplyCommand())
    handler.register_command('divide', DivideCommand())
    return handler

@pytest.fixture
def add_command(calculator):
    """Fixture to create an AddCommand instance."""
    return AddCommand(calculator, 10)

@pytest.fixture
def subtract_command(calculator):
    """Fixture to create a SubtractCommand instance."""
    return SubtractCommand(calculator, 5)

@pytest.fixture
def multiply_command(calculator):
    """Fixture to create a MultiplyCommand instance."""
    return MultiplyCommand(calculator, 2)

@pytest.fixture
def divide_command(calculator):
    """Fixture to create a DivideCommand instance."""
    return DivideCommand(calculator, 2)
