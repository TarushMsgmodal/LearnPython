"""
Tests for the utils module.
"""

from learnpython.utils import hello_world, add_numbers


def test_hello_world():
    """Test the hello_world function."""
    result = hello_world()
    assert result == "Hello from LearnPython!"
    assert isinstance(result, str)


def test_add_numbers():
    """Test the add_numbers function."""
    assert add_numbers(2, 3) == 5
    assert add_numbers(0, 0) == 0
    assert add_numbers(-1, 1) == 0
    assert add_numbers(100, 200) == 300


def test_add_numbers_negative():
    """Test add_numbers with negative numbers."""
    assert add_numbers(-5, -3) == -8
    assert add_numbers(-10, 5) == -5
