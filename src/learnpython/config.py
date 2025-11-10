"""
Configuration management for the LearnPython package.

This module handles configuration settings, environment variables,
and application settings.
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()


class Config:
    """
    Configuration class for managing application settings.
    """

    def __init__(self):
        self.debug = os.getenv("DEBUG", "False").lower() == "true"
        self.environment = os.getenv("ENVIRONMENT", "development")

    @property
    def is_development(self) -> bool:
        """Check if running in development mode."""
        return self.environment == "development"

    @property
    def is_production(self) -> bool:
        """Check if running in production mode."""
        return self.environment == "production"


# Global config instance
config = Config()
