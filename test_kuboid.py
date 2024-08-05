#import workfile.kuboid as kuboid
from workfile import kuboid
import pytest

def test_kuboid(monkeypatch, capsys):
    # Define a function to simulate multiple user inputs
    user_inputs = ["3.5", "4.2", "5.38"]

    def mock_input(_):
        return user_inputs.pop(0)

    # Use the function to simulate user input
    monkeypatch.setattr('builtins.input', mock_input)

    # Call the main function, which uses input() and prints the result
    kuboid.kuboid()

    # Capture the printed output
    captured = capsys.readouterr()
    assert captured.out.strip() == "Isipadu kuboid = 79.086"