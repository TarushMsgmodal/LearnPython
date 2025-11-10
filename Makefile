.PHONY: help install install-dev test lint format clean

help:
	@echo "Available commands:"
	@echo "  make install      - Install production dependencies"
	@echo "  make install-dev  - Install development dependencies"
	@echo "  make test         - Run tests with pytest"
	@echo "  make test-cov     - Run tests with coverage report"
	@echo "  make lint         - Run linting (flake8, pylint)"
	@echo "  make format       - Format code with black"
	@echo "  make format-check - Check code formatting"
	@echo "  make clean        - Remove build artifacts and cache"

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements-dev.txt
	pip install -e .

test:
	pytest -v

test-cov:
	pytest --cov=learnpython --cov-report=html --cov-report=term

lint:
	flake8 src tests
	pylint src/learnpython

format:
	black src tests

format-check:
	black --check src tests

clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	rm -rf .pytest_cache/
	rm -rf .coverage
	rm -rf htmlcov/
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
