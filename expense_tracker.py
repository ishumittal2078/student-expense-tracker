"""
Student Expense Tracker

A command-line application for college students to track daily expenses
across different categories (food, travel, recharge, other).
"""

from datetime import datetime

# Global storage
# Expense dictionary format: {'date': str, 'amount': float, 'category': str}
expense_list = []
monthly_budget = None

# Valid categories
VALID_CATEGORIES = {'food', 'travel', 'recharge', 'other'}


def validate_date(date_str):
    """
    Validate date string is in YYYY-MM-DD format and represents a valid
    calendar date.

    Args:
        date_str: String to validate as a date

    Returns:
        True if valid date

    Raises:
        ValueError: If date is invalid with specific error message
    """
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        raise ValueError(
            f"Invalid date. You entered: '{date_str}'\n"
            f"Date must be in YYYY-MM-DD format (e.g., 2024-01-15)."
        )


def validate_amount(amount_str):
    """
    Validate amount is numeric, in range [0.01, 1000000.00], and has max
    2 decimal places.

    Args:
        amount_str: String to validate as an amount

    Returns:
        float: The validated amount

    Raises:
        ValueError: If amount is invalid with specific error message
    """
    # Check for non-numeric strings like 'NAN', 'INF', etc.
    stripped = amount_str.strip()
    if stripped.lower() in ('nan', 'inf', 'infinity', 'none', 'null', ''):
        raise ValueError(
            f"Invalid amount. You entered: '{amount_str}'\n"
            "Amount must be between 0.01 and 1,000,000.00 with at most 2 "
            "decimal places."
        )

    try:
        amount = float(amount_str)
    except ValueError:
        raise ValueError(
            f"Invalid amount. You entered: '{amount_str}'\n"
            "Amount must be between 0.01 and 1,000,000.00 with at most 2 "
            "decimal places."
        )

    # Check for special float values
    if not (amount == amount):  # NaN check
        raise ValueError(
            f"Invalid amount. You entered: '{amount_str}'\n"
            "Amount must be between 0.01 and 1,000,000.00 with at most 2 "
            "decimal places."
        )

    if amount == float('inf') or amount == float('-inf'):
        raise ValueError(
            f"Invalid amount. You entered: '{amount_str}'\n"
            "Amount must be between 0.01 and 1,000,000.00 with at most 2 "
            "decimal places."
        )

    # Check range
    if amount < 0.01 or amount > 1_000_000.00:
        raise ValueError(
            f"Invalid amount. You entered: '{amount_str}'\n"
            "Amount must be between 0.01 and 1,000,000.00 with at most 2 "
            "decimal places."
        )

    # Check decimal places using string manipulation
    if '.' in amount_str:
        decimal_part = amount_str.split('.')[1]
        if len(decimal_part) > 2:
            raise ValueError(
                f"Invalid amount. You entered: '{amount_str}'\n"
                "Amount must be between 0.01 and 1,000,000.00 with at most 2 "
                "decimal places."
            )

    return amount


def validate_category(category_str):
    """
    Validate category is one of the valid categories (case-insensitive).

    Args:
        category_str: String to validate as a category

    Returns:
        str: The normalized (lowercase) category

    Raises:
        ValueError: If category is invalid with specific error message
    """
    normalized = category_str.lower()

    if normalized not in VALID_CATEGORIES:
        valid_list = ', '.join(sorted(VALID_CATEGORIES))
        raise ValueError(
            f"Invalid category. You entered: '{category_str}'\n"
            f"Valid categories are: {valid_list}"
        )

    return normalized


def add_expense(date, amount, category):
    """
    Add a new expense to the expense list.

    Args:
        date: Validated date string in YYYY-MM-DD format
        amount: Validated amount as float
        category: Validated category string (normalized to lowercase)
    """
    expense = {
        'date': date,
        'amount': amount,
        'category': category
    }
    expense_list.append(expense)

    # Display confirmation message
    print(f"Expense added: {date}, ${amount:.2f}, {category}")


def view_expenses():
    """
    Display all expenses in tabular format, sorted by date (oldest first).
    Shows 'No expenses recorded' message if list is empty.
    """
    if not expense_list:
        print("No expenses recorded")
        return

    # Sort expenses by date (oldest first)
    sorted_expenses = sorted(expense_list, key=lambda x: x['date'])

    # Display header
    print("\nAll Expenses:")
    print(f"{'Date':<12} | {'Amount':>10} | {'Category':<10}")
    print("-" * 12 + "-+-" + "-" * 10 + "-+-" + "-" * 10)

    # Display each expense
    for expense in sorted_expenses:
        print(f"{expense['date']:<12} | "
              f"{expense['amount']:>10.2f} | "
              f"{expense['category']:<10}")

    # Call budget warning stub
    display_budget_warning()


def calculate_total():
    """
    Calculate the sum of all expense amounts.

    Returns:
        float: Total spending with 2 decimal precision, 0.00 if list is empty
    """
    if not expense_list:
        return 0.00

    total = sum(expense['amount'] for expense in expense_list)
    return round(total, 2)


def view_total_spending():
    """
    Display the total spending amount with 2 decimal places.
    """
    total = calculate_total()
    print(f"\nTotal Spending: ${total:.2f}")

    # Call budget warning stub
    display_budget_warning()


def calculate_category_totals():
    """
    Calculate total spending for each category.

    Returns:
        dict: Dictionary mapping category to total amount, empty dict if no
        expenses
    """
    if not expense_list:
        return {}

    totals = {}
    for expense in expense_list:
        cat = expense['category']
        if cat in totals:
            totals[cat] += expense['amount']
        else:
            totals[cat] = expense['amount']

    return totals


def find_highest_category():
    """
    Identify the category with the highest total spending.

    Returns:
        tuple: (category, amount) for highest spending category, or None if
        no expenses
    """
    category_totals = calculate_category_totals()

    if not category_totals:
        return None

    # Find category with maximum total
    highest_cat = max(category_totals.items(), key=lambda x: x[1])
    return highest_cat


def view_highest_category():
    """
    Display the highest spending category and its total amount.
    Shows 'No data available' message if list is empty.
    """
    result = find_highest_category()

    if result is None:
        print("No data available")
        return

    category, amount = result
    print(f"\nHighest Spending Category: {category}")
    print(f"Amount: ${amount:.2f}")


def set_monthly_budget(budget_str):
    """
    Validate and store monthly budget.

    Args:
        budget_str: String to validate as a budget amount

    Raises:
        ValueError: If budget is invalid with specific error message. The
        error message includes the invalid value and valid range.
    """
    global monthly_budget

    # Check for non-numeric strings like 'NAN', 'INF', etc.
    stripped = budget_str.strip()
    if stripped.lower() in ('nan', 'inf', 'infinity', 'none', 'null', ''):
        raise ValueError(
            f"Invalid budget. You entered: '{budget_str}'\n"
            "Budget must be between 0.01 and 999,999,999.99 with at most 2 "
            "decimal places."
        )

    try:
        budget = float(budget_str)
    except ValueError:
        raise ValueError(
            f"Invalid budget. You entered: '{budget_str}'\n"
            "Budget must be between 0.01 and 999,999,999.99 with at most 2 "
            "decimal places."
        )

    # Check for special float values
    if not (budget == budget):  # NaN check
        raise ValueError(
            f"Invalid budget. You entered: '{budget_str}'\n"
            "Budget must be between 0.01 and 999,999,999.99 with at most 2 "
            "decimal places."
        )

    if budget == float('inf') or budget == float('-inf'):
        raise ValueError(
            f"Invalid budget. You entered: '{budget_str}'\n"
            "Budget must be between 0.01 and 999,999,999.99 with at most 2 "
            "decimal places."
        )

    # Check range
    if budget < 0.01 or budget > 999_999_999.99:
        raise ValueError(
            f"Invalid budget. You entered: '{budget_str}'\n"
            "Budget must be between 0.01 and 999,999,999.99 with at most 2 "
            "decimal places."
        )

    # Check decimal places using string manipulation
    if '.' in budget_str:
        decimal_part = budget_str.split('.')[1]
        if len(decimal_part) > 2:
            raise ValueError(
                f"Invalid budget. You entered: '{budget_str}'\n"
                "Budget must be between 0.01 and 999,999,999.99 with at most "
                "2 decimal places."
            )

    monthly_budget = budget
    msg = f"Monthly budget set to: ${budget:.2f}"
    print(msg)


def check_budget_warning():
    """
    Check if current month spending meets or exceeds the monthly budget.

    Returns:
        bool: True if spending >= budget for current month, False otherwise
              Returns False if budget is not set
    """
    if monthly_budget is None:
        return False

    # Get current month in YYYY-MM format
    current_month = datetime.now().strftime('%Y-%m')

    # Filter expenses from current month and calculate total
    month_total = sum(
        exp['amount']
        for exp in expense_list
        if exp['date'].startswith(current_month)
    )

    return month_total >= monthly_budget


def display_budget_warning():
    """
    Display budget warning message if current month spending meets or exceeds
    budget.
    """
    if check_budget_warning():
        print(
            f"\n⚠️  WARNING: You have exceeded your monthly budget of ${
                monthly_budget:.2f}!")


def initialize_sample_data():
    """
    Add 3 sample expenses covering at least 3 categories.
    """
    sample_expenses = [
        {'date': '2024-01-10', 'amount': 150.00, 'category': 'food'},
        {'date': '2024-01-12', 'amount': 80.50, 'category': 'travel'},
        {'date': '2024-01-15', 'amount': 299.00, 'category': 'recharge'}
    ]

    for expense in sample_expenses:
        expense_list.append(expense)


def display_menu():
    """
    Display the main menu with 6 options and visual separator.
    """
    print("\n" + "=" * 40)
    print("STUDENT EXPENSE TRACKER")
    print("=" * 40)
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spending")
    print("4. View Highest Spending Category")
    print("5. Set Monthly Budget")
    print("6. Exit")
    print("=" * 40)


def get_menu_choice():
    """
    Read and validate menu input (integers 1-6).
    Re-prompts until valid choice is received.

    Returns:
        int: Valid menu choice between 1 and 6
    """
    while True:
        choice = input("Enter your choice (1-6): ").strip()

        try:
            choice_num = int(choice)
            if 1 <= choice_num <= 6:
                return choice_num
            else:
                print(f"Error: Invalid choice. You entered: '{choice}'")
                print("Please enter a number between 1 and 6.")
        except ValueError:
            print(f"Error: Invalid choice. You entered: '{choice}'")
            print("Please enter a number between 1 and 6.")


def prompt_add_expense():
    """
    Prompt for date, amount, and category inputs.
    Validate all fields and only add expense if all validations pass.
    Display specific error messages for invalid inputs.
    """
    print("\n--- Add New Expense ---")

    # Prompt for date
    date_str = input("Enter expense date (YYYY-MM-DD): ").strip()
    try:
        validate_date(date_str)
    except ValueError as e:
        print(f"Error: {e}")
        return

    # Prompt for amount
    amount_str = input("Enter amount (0.01 to 1,000,000.00): ").strip()
    try:
        amount = validate_amount(amount_str)
    except ValueError as e:
        print(f"Error: {e}")
        return

    # Prompt for category
    category_str = input(
        "Enter category (food/travel/recharge/other): ").strip()
    try:
        category = validate_category(category_str)
    except ValueError as e:
        print(f"Error: {e}")
        return

    # All validations passed - add the expense
    add_expense(date_str, amount, category)


def prompt_set_budget():
    """
    Prompt for budget amount with range hint.
    Call set_monthly_budget() or display error.
    """
    print("\n--- Set Monthly Budget ---")
    budget_str = input(
        "Enter monthly budget (0.01 to 999,999,999.99): ").strip()

    try:
        set_monthly_budget(budget_str)
    except ValueError as e:
        print(f"Error: {e}")


def main_loop():
    """
    Main application loop: initialize sample data, display menu,
    get choice, execute action, and loop until exit.
    """
    # Initialize sample data at start
    initialize_sample_data()

    print("\nWelcome to Student Expense Tracker!")
    print("Sample data has been loaded.")

    while True:
        try:
            # Display menu and get choice
            display_menu()
            choice = get_menu_choice()

            # Execute action based on choice
            if choice == 1:
                prompt_add_expense()
            elif choice == 2:
                view_expenses()
            elif choice == 3:
                view_total_spending()
            elif choice == 4:
                view_highest_category()
            elif choice == 5:
                prompt_set_budget()
            elif choice == 6:
                print("\nThank you for using Student Expense Tracker!")
                print("Goodbye!")
                break

            # Display separator after each action
            print("\n" + "-" * 40)

        except Exception as e:
            # Error recovery: display user-friendly message and return to menu
            print(f"\nAn unexpected error occurred: {e}")
            print("Returning to main menu...")
            print("-" * 40)


def main():
    """Main entry point for the application."""
    main_loop()


if __name__ == "__main__":
    main()
