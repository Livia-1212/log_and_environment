import pytest
from app import App
from app.commands.commands.calc_commands import AddCommand, SubtractCommand
from icecream import ic

def test_app_get_environment_variable():
    app = App()
    # Retrieve the current environment setting
    current_env = app.get_environment_variable('ENVIRONMENT')
    # Assert that the current environment is what you expect
    assert current_env in ['DEVELOPMENT', 'TESTING', 'PRODUCTION'], f"Invalid ENVIRONMENT: {current_env}"

def test_app_start_exit_command(capfd, monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    assert e.type == SystemExit

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    
    with pytest.raises(SystemExit) as excinfo:
        app.start()
    
    # Verify that the unknown command was handled as expected
    captured = capfd.readouterr()
    assert "No such command: unknown_command" in captured.out

# Tests for calculation commands
def test_add_command():
    add_command = AddCommand()
    result = add_command.execute(3, 5)
    ic(result)  # Use icecream for output verification
    assert result == 8

def test_subtract_command():
    subtract_command = SubtractCommand()
    result = subtract_command.execute(10, 4)
    ic(result)
    assert result == 6
