import pytest
from app.app import App
from icecream import ic

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

def test_app_start_unknown_command(capfd, monkeypatch):
    """Test how the REPL handles an unknown command before exiting."""
    # Simulate user entering an unknown command followed by 'exit'
    inputs = iter(['unknown_command', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))
    app = App()
    with pytest.raises(SystemExit) as excinfo:
        app.start()
    # Log the exit code
    ic(excinfo.value.code)
    assert excinfo.value.code == 1, "The app did not exit with the expected failure code"

    # Verify that the unknown command was handled as expected
    captured = capfd.readouterr()
    assert "No such command: unknown_command" in captured.out

def test_app_greet_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command and outputs 'Hello, World!'."""
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    # Check that the exit was graceful with the correct exit code
    ic(e.value.code)
    assert e.value.code == 0, "The app did not exit as expected"

    # Capture the output and check if "Hello, World!" was printed
    captured = capfd.readouterr()
    ic(captured.out)  # Log the captured output
    assert "Hello, World!" in captured.out, "The greet command did not produce the expected output."
