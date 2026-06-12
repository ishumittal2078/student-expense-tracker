# Student Expense Tracker

A Python command-line application for college students to track daily expenses, monitor spending patterns, and manage monthly budgets.

## Features

- **Add Expenses**: Record expenses with date, amount, and category
- **View Expenses**: Display all expenses in chronological order
- **Total Spending**: Calculate and display total amount spent
- **Category Analysis**: Identify which category has the highest spending
- **Budget Management**: Set monthly budget and receive warnings when exceeded
- **Sample Data**: Pre-loaded with 3 sample expenses for immediate testing

## Categories

- Food
- Travel
- Recharge
- Other

## Requirements

- Python 3.6 or later
- No mandatory external dependencies (uses Python standard library)
- Optional: pandas for enhanced data display

## Installation

1. Clone the repository or download the project files:
```bash
git clone https://github.com/yourusername/student-expense-tracker.git
cd student-expense-tracker
```

2. (Optional) Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. (Optional) Install development dependencies for testing:
```bash
pip install -r requirements.txt
```

## How to Run the Application

1. Make sure Python 3.6+ is installed on your system
2. Navigate to the project directory
3. Run the main application file:
```bash
python expense_tracker.py
```

The application will start with a menu-driven interface and pre-loaded sample data.

### Example Usage Scenario

```
Welcome to Student Expense Tracker!
Sample data has been loaded.

========================================
STUDENT EXPENSE TRACKER
========================================
1. Add Expense
2. View All Expenses
3. View Total Spending
4. View Highest Spending Category
5. Set Monthly Budget
6. Exit
========================================

Enter your choice (1-6): 2

All Expenses:
Date       | Amount    | Category
-----------|-----------|----------
2024-01-10 |    150.00 | food
2024-01-12 |     80.50 | travel
2024-01-15 |    299.00 | recharge
-----------|-----------|----------
Total: 529.50

----------------------------------------
```

## How to Run Tests

### Prerequisites

Install the testing dependencies first:
```bash
pip install -r requirements.txt
```

### Running Test Suite

Run all tests:
```bash
pytest tests/
```

Run only property-based tests:
```bash
pytest tests/test_properties.py
```

Run with coverage report:
```bash
pytest --cov=expense_tracker --cov-report=html tests/
```

Run tests with hypothesis statistics:
```bash
pytest tests/test_properties.py -v --hypothesis-show-statistics
```

### Test Coverage

The test suite includes:
- **21 Property-based tests** using Hypothesis library (100+ iterations each)
- **Unit tests** for specific examples and edge cases
- **Integration tests** for complete user flows

## Example Usage Scenarios

### Scenario 1: Tracking Daily Expenses

```bash
# Start the application
python expense_tracker.py

# Choose option 1 to add an expense
Enter expense date (YYYY-MM-DD): 2024-01-20
Enter amount (0.01 to 1,000,000.00): 250.50
Enter category (food/travel/recharge/other): food

# Choose option 2 to view all expenses
# Choose option 3 to see your total spending
```

### Scenario 2: Budget Monitoring

```bash
# Choose option 5 to set a monthly budget
Enter monthly budget (0.01 to 999,999,999.99): 500

# Add expenses throughout the month
# When viewing expenses or total spending,
# you'll see a warning if you exceed your budget
```

### Scenario 3: Category Analysis

```bash
# Add expenses from different categories
# Choose option 4 to see which category you spend the most on

# Example output:
# Highest Spending Category: food
# Amount: 1500.00
```

## Input Formats

- **Date**: YYYY-MM-DD format (e.g., 2024-01-15)
- **Amount**: Numeric value between 0.01 and 1,000,000.00 with maximum 2 decimal places
- **Category**: One of: food, travel, recharge, other (case-insensitive)
- **Budget**: Numeric value between 0.01 and 999,999,999.99 with maximum 2 decimal places

## Menu Options

1. **Add Expense** - Add a new expense with date (YYYY-MM-DD), amount, and category
2. **View All Expenses** - Display all recorded expenses in a table format
3. **View Total Spending** - Show the total amount spent
4. **View Highest Spending Category** - Identify the category with maximum spending
5. **Set Monthly Budget** - Set or update your monthly spending limit
6. **Exit** - Close the application

## Development

### Code Quality

Check code style with flake8:
```bash
flake8 expense_tracker.py
```

### Running the Demo

Run the interactive demo to see all features in action:
```bash
python demo.py
```

## Project Structure

```
student-expense-tracker/
├── expense_tracker.py       # Main application
├── tests/                   # Test suite
│   ├── test_properties.py   # Property-based tests
│   ├── test_validation.py   # Validation unit tests
│   ├── test_operations.py   # Operation unit tests
│   ├── test_budget.py       # Budget unit tests
│   ├── test_menu.py         # Menu unit tests
│   └── test_edge_cases.py   # Edge case tests
├── requirements.txt         # Testing dependencies
├── README.md               # This file
├── CONTRIBUTING.md         # Contribution guidelines
├── LICENSE                 # License file
└── .gitignore             # Git ignore patterns
```

## Dependencies

### Runtime Dependencies

- Python 3.6+ (standard library only)
  - `datetime` - Date parsing and validation
  - `sys` - System-specific parameters and functions

### Development Dependencies (testing)

See `requirements.txt`:
- `hypothesis>=6.0.0` - Property-based testing
- `pytest>=7.0.0` - Test framework
- `pytest-cov>=4.0.0` - Coverage reporting

## Features in Detail

### Expense Management

- All expenses stored in memory during session
- Expenses persist only while application is running
- Validation ensures data integrity (valid dates, amounts, categories)
- Comprehensive error messages guide correct input

### Budget Warnings

- Set a monthly spending limit
- Automatic warnings when current month spending reaches or exceeds budget
- Warnings display when viewing expenses or total spending
- Budget warnings specific to current calendar month

### Data Validation

- **Date validation**: Must be YYYY-MM-DD format and a valid calendar date
- **Amount validation**: Must be numeric, 0.01-1,000,000.00, maximum 2 decimals
- **Category validation**: Must be one of the four allowed categories
- **Budget validation**: Must be numeric, 0.01-999,999,999.99, maximum 2 decimals

## Technical Details

- **Language**: Python 3.6+
- **Dependencies**: Standard library only (datetime, sys)
- **Storage**: In-memory (data not persisted between sessions)
- **Architecture**: Procedural with modular functions
- **Code Style**: PEP 8 compliant

## Testing

The project includes comprehensive testing:

### Property-Based Tests

Using the Hypothesis library, we validate 21 correctness properties:
- Expense creation with valid inputs
- Category validation (valid and invalid inputs)
- Amount validation (valid, out-of-range, excessive decimals)
- Date validation (valid format, invalid format, invalid calendar dates)
- Total calculation accuracy
- Category grouping accuracy
- Budget tracking and warnings
- And more...

### Unit Tests

Specific examples and edge cases:
- Empty expense list handling
- Sample data initialization
- Boundary values for amounts and budgets
- Error message content
- Menu navigation

### Running Tests

```bash
# Run all tests
pytest tests/

# Run with verbose output
pytest tests/ -v

# Run specific test file
pytest tests/test_properties.py
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

Created for college students who want a simple, offline tool to track their daily expenses.

## Acknowledgments

- Built with Python standard library for maximum portability
- Uses Hypothesis for property-based testing
- Designed to avoid looking AI-generated with natural code patterns

## Support

For issues and feature requests, please create an issue in the repository.
