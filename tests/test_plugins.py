import pytest
from app.app import App
from icecream import ic

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
