# Contributing to Pet Name Generator

First off, thank you for considering contributing to Pet Name Generator! 🎉

## Code of Conduct

This project and everyone participating in it is governed by our Code of Conduct. By participating, you are expected to uphold this code.

## How Can I Contribute?

### Reporting Bugs

Before creating bug reports, please check the issue list as you might find out that you don't need to create one. When you are creating a bug report, please include as many details as possible:

* **Use a clear and descriptive title**
* **Describe the exact steps which reproduce the problem**
* **Provide specific examples to demonstrate the steps**
* **Describe the behavior you observed after following the steps**
* **Explain which behavior you expected to see instead and why**

### Suggesting Enhancements

Enhancement suggestions are tracked as GitHub issues. When creating an enhancement suggestion, please include:

* **Use a clear and descriptive title**
* **Provide a step-by-step description of the suggested enhancement**
* **Provide specific examples to demonstrate the steps**
* **Describe the current behavior and expected behavior**
* **Explain why this enhancement would be useful**

### Pull Requests

* Fill in the required template
* Follow the Python styleguide
* Include appropriate test cases
* End all files with a newline
* Ensure tests pass: `pytest`

## Styleguides

### Git Commit Messages

* Use the present tense ("Add feature" not "Added feature")
* Use the imperative mood ("Move cursor to..." not "Moves cursor to...")
* Limit the first line to 72 characters or less
* Reference issues and pull requests liberally after the first line

### Python Styleguide

* Use [Black](https://black.readthedocs.io/) for code formatting
* Use [flake8](https://flake8.pycqa.org/) for linting
* Follow [PEP 8](https://www.python.org/dev/peps/pep-0008/)
* Write meaningful docstrings for all functions and classes

## Development Setup

1. Fork and clone the repository
```bash
git clone https://github.com/mehtabrastogi/pet-name-generator.git
cd pet-name-generator
```

2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies
```bash
pip install -r requirements.txt
```

4. Create a new branch
```bash
git checkout -b feature/your-feature-name
```

5. Make your changes and commit
```bash
git add .
git commit -m "Add description of your changes"
```

6. Run tests
```bash
pytest
```

7. Push to your fork and open a Pull Request

## Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=pet_name_generator

# Run specific test file
pytest tests/test_generator.py -v
```

Thank you for contributing! 🐾
