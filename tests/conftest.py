# tests/conftest.py

import pytest
from app.app import App
from app.commands.command_handler import CommandHandler
from app.commands.commands import AddCommand, SubtractCommand, MultiplyCommand, DivideCommand

@pytest.fixture
def app_instance():
    """Fixture to create a Calculator instance for testing."""
    return App()

def run_app_and_exit_on_unknown_command(inputs, monkeypatch):
    """Run the app and simulate inputs, expecting it to exit on unknown command."""
    with pytest.raises(SystemExit) as e:
        # Use monkeypatch to simulate user input
        monkeypatch.setattr('builtins.input', lambda _: next(inputs))
        App().start()
    return e.value.code  # Return the exit code for assertion

@pytest.fixture
def cmd_handler():
    """Fixture to create a CommandHandler instance."""
    handler = CommandHandler()
    return handler

@pytest.fixture
def add_command(calc_instance):
    """Fixture to create an AddCommand instance."""
    return AddCommand(calc_instance, 10)

@pytest.fixture
def subtract_command(calc_instance):
    """Fixture to create a SubtractCommand instance."""
    return SubtractCommand(calc_instance, 5)

@pytest.fixture
def multiply_command(calc_instance):
    """Fixture to create a MultiplyCommand instance."""
    return MultiplyCommand(calc_instance, 2)

@pytest.fixture
def divide_command(calc_instance):
    """Fixture to create a DivideCommand instance."""
    return DivideCommand(calc_instance, 2)
