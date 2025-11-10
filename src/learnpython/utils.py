"""
Utility functions for the LearnPython package.

This module contains common utility functions that can be used
across the application.
"""


def hello_world() -> str:
    """
    A simple hello world function to demonstrate the package structure.

    Returns:
        str: A greeting message
    """
    return "Hello from LearnPython!"


def add_numbers(a: int, b: int) -> int:
    """
    Add two numbers together.

    Args:
        a: First number
        b: Second number

    Returns:
        int: Sum of a and b
    """
    return a + b
