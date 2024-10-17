import pytest
from app.app import App
from icecream import ic
from tests.conftest import run_app_and_exit_on_unknown_command

def test_app_get_environment_variable():
    """Test retrieving the current environment setting."""
    app = App()
    current_env = app.get_environment_variable('ENVIRONMENT')
    ic(current_env)  # Use Icecream to log the retrieved environment variable
    assert current_env in ['DEVELOPMENT', 'TESTING', 'PRODUCTION'], f"Invalid ENVIRONMENT: {current_env}"

def test_app_start_exit_command(monkeypatch):
    """Test that the REPL exits correctly on 'exit' command."""
    # Simulate user entering 'exit'
    monkeypatch.setattr('builtins.input', lambda _: 'exit')
    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()
    ic(e.value.code)  # Log the exit code
    assert e.value.code == 0, "The app did not exit as expected"

def test_app_start_unknown_command(monkeypatch, app_instance):
    """Test how the REPL handles an unknown command before exiting."""
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    # Ensure you're using the app_instance fixture correctly
    with pytest.raises(SystemExit) as e:
        app_instance.start()  # This should now correctly call the start method of the App instance

    assert e.value.code == 1, "The app did not exit with the expected failure code"