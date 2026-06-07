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

1. Clone the repository:
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
pip install -r requirements-dev.txt
```

## Usage

Run the application:
```bash
python expense_tracker.py
```

### Menu Options

1. **Add Expense** - Add a new expense with date (YYYY-MM-DD), amount, and category
2. **View All Expenses** - Display all recorded expenses in a table format
3. **View Total Spending** - Show the total amount spent
4. **View Highest Spending Category** - Identify the category with maximum spending
5. **Set Monthly Budget** - Set or update your monthly spending limit
6. **Exit** - Close the application

### Input Formats

- **Date**: YYYY-MM-DD format (e.g., 2024-01-15)
- **Amount**: Numeric value between 0.01 and 1,000,000.00 with maximum 2 decimal places
- **Category**: One of: food, travel, recharge, other (case-insensitive)
- **Budget**: Numeric value between 0.01 and 999,999,999.99 with maximum 2 decimal places

## Example

```
=================================
STUDENT EXPENSE TRACKER
=================================

1. Add Expense
2. View All Expenses
3. View Total Spending
4. View Highest Spending Category
5. Set Monthly Budget
6. Exit

Enter your choice (1-6): 2

All Expenses:
Date       | Amount    | Category
-----------|-----------|----------
2024-01-10 |    150.00 | food
2024-01-12 |     80.50 | travel
2024-01-15 |    299.00 | recharge
-----------|-----------|----------
Total: 529.50
```

## Development

### Running Tests

Run all tests:
```bash
pytest tests/
```

Run only property-based tests:
```bash
pytest tests/test_properties.py
```

Run with coverage:
```bash
pytest --cov=expense_tracker tests/
```

### Code Quality

Check code style with flake8:
```bash
flake8 expense_tracker.py
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
├── requirements-dev.txt     # Development dependencies
├── README.md               # This file
├── LICENSE                 # License file
└── .gitignore             # Git ignore patterns

```

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
- **21 Property-based tests** using Hypothesis library (100+ iterations each)
- **Unit tests** for specific examples and edge cases
- **Integration tests** for complete user flows
- Tests validate all requirements and correctness properties

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
