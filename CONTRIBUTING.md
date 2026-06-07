# Contributing to Student Expense Tracker

Thank you for considering contributing to the Student Expense Tracker! This document provides guidelines for contributing to the project.

## Getting Started

1. **Fork the repository** on GitHub
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/yourusername/student-expense-tracker.git
   cd student-expense-tracker
   ```
3. **Create a branch** for your changes:
   ```bash
   git checkout -b feature/your-feature-name
   ```

## Development Setup

1. **Create a virtual environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install development dependencies**:
   ```bash
   pip install -r requirements-dev.txt
   ```

3. **Verify the setup** by running tests:
   ```bash
   pytest tests/
   ```

## Coding Standards

### Python Style Guide

- Follow **PEP 8** style guide
- Maximum line length: **79 characters**
- Use **snake_case** for variables and functions (2-50 characters)
- Use **PascalCase** for class names (2-50 characters)
- Function length: Maximum **50 lines**
- Nesting depth: Maximum **3 levels**

### Code Quality Checks

Before submitting, ensure your code passes:

```bash
# Run flake8 linting
flake8 expense_tracker.py

# Run all tests
pytest tests/

# Run tests with coverage
pytest --cov=expense_tracker tests/
```

### Documentation

- Add docstrings for functions longer than 10 lines
- Comment complex logic with nesting depth > 2
- Explain "why" not "what" in comments
- Update README.md if adding new features

## Testing

### Writing Tests

- Add **property-based tests** for universal behaviors using Hypothesis
- Add **unit tests** for specific examples and edge cases
- Each property test should run minimum **100 iterations**
- Include test tags referencing design properties

### Test Structure

```python
# Property-based test example
from hypothesis import given, strategies as st

# Feature: student-expense-tracker, Property X: Description
@given(...)
@hypothesis.settings(max_examples=100)
def test_property_name(...):
    # Test implementation
    pass

# Unit test example
def test_specific_behavior():
    """Test requirement X.Y: Description"""
    # Test implementation
    pass
```

## Making Changes

### Commit Guidelines

- Write clear, descriptive commit messages
- Use present tense ("Add feature" not "Added feature")
- Reference issues when applicable (#123)

Example:
```bash
git commit -m "Add validation for negative amounts in expenses"
```

### Pull Request Process

1. **Update documentation** if needed (README.md, docstrings)
2. **Add tests** for new functionality
3. **Ensure all tests pass**
4. **Run code quality checks** (flake8)
5. **Push to your fork**:
   ```bash
   git push origin feature/your-feature-name
   ```
6. **Open a Pull Request** on GitHub with:
   - Clear title describing the change
   - Description of what was changed and why
   - Reference to any related issues
   - Confirmation that tests pass

### Pull Request Review

- Maintainers will review your PR
- Address any feedback or requested changes
- Once approved, your PR will be merged

## Types of Contributions

### Bug Reports

When reporting bugs, include:
- Python version
- Operating system
- Steps to reproduce
- Expected vs actual behavior
- Error messages (if any)

### Feature Requests

When suggesting features:
- Explain the use case
- Describe expected behavior
- Consider backwards compatibility
- Keep features aligned with project goals (simple, offline CLI tool)

### Code Contributions

Areas where contributions are welcome:
- Bug fixes
- Test coverage improvements
- Documentation improvements
- Performance optimizations
- Code quality enhancements
- New validation edge cases

### Future Enhancement Ideas

Potential areas for contribution (outside current scope):
- Persistent storage (JSON/SQLite)
- Expense editing and deletion
- Date range filtering
- Category-specific budgets
- Export to CSV
- Visualization (ASCII charts)

## Questions?

If you have questions about contributing:
- Check existing issues and documentation
- Open a new issue with your question
- Be respectful and patient

## Code of Conduct

- Be respectful and inclusive
- Focus on constructive feedback
- Help create a welcoming environment for all contributors

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

Thank you for contributing to Student Expense Tracker! 🎓💰
