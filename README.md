# Student Expense Tracker

A command-line application designed for college students to manage daily expenses without needing internet connectivity or complex setup.

## Features

- **Expense Management**: Add expenses with date, amount, and category
- **Budget Tracking**: Set monthly budget limits and get warnings when exceeded
- **Category Analysis**: Identify which category has the highest spending
- **Sample Data**: Pre-loaded with sample expenses for demonstration
- **Input Validation**: All user inputs are validated with clear error messages

## Categories

The application supports four expense categories:
- **Food**: Canteen bills, snacks, groceries
- **Travel**: Public transport, taxi, fuel
- **Recharge**: Mobile recharge, internet packages
- **Other**: Miscellaneous expenses

## Requirements

- Python 3.8 or higher
- Only standard Python library required (no external dependencies)

## Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/student-expense-tracker.git
cd student-expense-tracker

# Run the application
python main.py
```

## Usage

1. Run the application: `python main.py`
2. Choose from the menu options:
   - 1. Add expense
   - 2. View all expenses
   - 3. Show total spending
   - 4. Show highest category
   - 5. Set monthly budget
   - 6. Exit

## Project Structure

```
student-expense-tracker/
├── src/
│   ├── models/
│   │   ├── expense.py      # Expense class definition
│   │   └── __init__.py
│   └── __init__.py
├── README.md
└── .gitignore
```

## License

This project is for educational purposes.