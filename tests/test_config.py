"""
Tests for the config module.
"""

import os
from learnpython.config import Config


def test_config_default_values():
    """Test Config class default values."""
    config = Config()
    assert hasattr(config, "debug")
    assert hasattr(config, "environment")


def test_config_is_development():
    """Test is_development property."""
    os.environ["ENVIRONMENT"] = "development"
    config = Config()
    assert config.is_development is True
    assert config.is_production is False


def test_config_is_production():
    """Test is_production property."""
    os.environ["ENVIRONMENT"] = "production"
    config = Config()
    assert config.is_production is True
    assert config.is_development is False
