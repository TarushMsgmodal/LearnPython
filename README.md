# LearnPython

A well-structured Python repository for learning and backend development.

## 📁 Project Structure

```
LearnPython/
├── src/                    # Source code
│   └── learnpython/       # Main package
│       ├── __init__.py    # Package initialization
│       ├── config.py      # Configuration management
│       └── utils.py       # Utility functions
├── tests/                 # Test files
│   ├── conftest.py       # Test configuration
│   ├── test_config.py    # Config tests
│   └── test_utils.py     # Utils tests
├── docs/                  # Documentation
├── scripts/               # Utility scripts
│   └── setup.sh          # Development setup script
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore rules
├── pyproject.toml        # Project configuration
├── requirements.txt      # Production dependencies
└── requirements-dev.txt  # Development dependencies
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Quick Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/TarushMsgmodal/LearnPython.git
   cd LearnPython
   ```

2. **Run the setup script** (Linux/Mac)
   ```bash
   ./scripts/setup.sh
   ```

   Or **manually set up**:
   ```bash
   # Create virtual environment
   python3 -m venv venv
   
   # Activate virtual environment
   # On Linux/Mac:
   source venv/bin/activate
   # On Windows:
   # venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements-dev.txt
   
   # Install package in editable mode
   pip install -e .
   ```

3. **Configure environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

## 🧪 Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=learnpython --cov-report=html

# Run specific test file
pytest tests/test_utils.py

# Run with verbose output
pytest -v
```

## 🛠️ Development

### Code Formatting

```bash
# Format code with Black
black src tests

# Check formatting without changes
black --check src tests
```

### Linting

```bash
# Run flake8
flake8 src tests

# Run pylint
pylint src/learnpython

# Run mypy for type checking
mypy src/learnpython
```

### Running the Package

```python
# Example usage
from learnpython.utils import hello_world, add_numbers

print(hello_world())
result = add_numbers(5, 3)
print(f"5 + 3 = {result}")
```

## 📦 Dependencies

### Production Dependencies
- `requests` - HTTP library
- `python-dotenv` - Environment variable management
- `pydantic` - Data validation
- `python-dateutil` - Date/time utilities

### Development Dependencies
- `pytest` - Testing framework
- `pytest-cov` - Coverage plugin
- `black` - Code formatter
- `flake8` - Linter
- `pylint` - Code analyzer
- `mypy` - Static type checker

## 🏗️ Backend Development

This structure is ready for backend development with:

- **Web Frameworks**: Add Flask, FastAPI, or Django
- **Databases**: SQLAlchemy for SQL databases, PyMongo for MongoDB
- **API Development**: Built-in request handling and validation with Pydantic
- **Configuration Management**: Environment-based configuration
- **Testing**: Comprehensive test structure with pytest

### Adding a Web Framework

**For Flask:**
```bash
pip install flask
# Add to requirements.txt
```

**For FastAPI:**
```bash
pip install fastapi uvicorn
# Add to requirements.txt
```

## 📝 Contributing

1. Create a new branch for your feature
2. Make your changes
3. Run tests and linting
4. Commit your changes
5. Push and create a pull request

## 📄 License

This project is for learning purposes.

## 🤝 Support

For questions or issues, please open an issue on GitHub.
