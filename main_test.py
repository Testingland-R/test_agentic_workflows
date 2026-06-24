import pytest
from main import Main


def test_main_init():
    """Test the initialization of the Main class."""
    main = Main("red")
    assert main.colour == "red"

def test_main_get_colour():
    """Test the get_colour method of the Main class."""
    main = Main("red")
    assert main.get_colour() == "The colour is red."

    main = Main("invalid")
    assert main.get_colour() == "The colour is not in the list."

def test_main_run(capsys):
    """Test the run method of the Main class."""
    main = Main("blue")
    main.run()
    captured = capsys.readouterr()
    assert captured.out == "The colour is blue.\n"
