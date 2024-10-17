from icecream import ic
from tests.conftest import app_instance, run_app_and_exit_on_unknown_command

def test_app_greet_command(capfd, monkeypatch):
    """Test that the REPL correctly handles the 'greet' command and outputs 'Hello, World!'."""
    inputs = iter(['greet', 'exit'])

    exit_code = run_app_and_exit_on_unknown_command(inputs, monkeypatch)
    ic(exit_code)

    assert exit_code == 0, "The app did not exit as expected"
    captured = capfd.readouterr()
    assert "Hello, This is a calculator!" in captured.out, "The greet command did not produce the expected output."