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
    Validate date string is in YYYY-MM-DD format and represents a valid calendar date.
    
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
    Validate amount is numeric, in range [0.01, 1000000.00], and has max 2 decimal places.
    
    Args:
        amount_str: String to validate as an amount
        
    Returns:
        float: The validated amount
        
    Raises:
        ValueError: If amount is invalid with specific error message
    """
    try:
        amount = float(amount_str)
    except ValueError:
        raise ValueError(
            f"Invalid amount. You entered: '{amount_str}'\n"
            f"Amount must be between 0.01 and 1,000,000.00 with at most 2 decimal places."
        )
    
    # Check range
    if amount < 0.01 or amount > 1_000_000.00:
        raise ValueError(
            f"Invalid amount. You entered: '{amount_str}'\n"
            f"Amount must be between 0.01 and 1,000,000.00 with at most 2 decimal places."
        )
    
    # Check decimal places using string manipulation
    if '.' in amount_str:
        decimal_part = amount_str.split('.')[1]
        if len(decimal_part) > 2:
            raise ValueError(
                f"Invalid amount. You entered: '{amount_str}'\n"
                f"Amount must be between 0.01 and 1,000,000.00 with at most 2 decimal places."
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
        dict: Dictionary mapping category to total amount, empty dict if no expenses
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
        tuple: (category, amount) for highest spending category, or None if no expenses
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
        ValueError: If budget is invalid with specific error message
    """
    global monthly_budget
    
    try:
        budget = float(budget_str)
    except ValueError:
        raise ValueError(
            f"Invalid budget. You entered: '{budget_str}'\n"
            f"Budget must be between 0.01 and 999,999,999.99 with at most 2 decimal places."
        )
    
    # Check range
    if budget < 0.01 or budget > 999_999_999.99:
        raise ValueError(
            f"Invalid budget. You entered: '{budget_str}'\n"
            f"Budget must be between 0.01 and 999,999,999.99 with at most 2 decimal places."
        )
    
    # Check decimal places using string manipulation
    if '.' in budget_str:
        decimal_part = budget_str.split('.')[1]
        if len(decimal_part) > 2:
            raise ValueError(
                f"Invalid budget. You entered: '{budget_str}'\n"
                f"Budget must be between 0.01 and 999,999,999.99 with at most 2 decimal places."
            )
    
    monthly_budget = budget
    print(f"Monthly budget set to: ${budget:.2f}")


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
    Display budget warning message if current month spending meets or exceeds budget.
    """
    if check_budget_warning():
        print(f"\n⚠️  WARNING: You have exceeded your monthly budget of ${monthly_budget:.2f}!")


def main():
    """Main entry point for the application."""
    print("Student Expense Tracker")
    print("=" * 40)
    print("Application structure initialized.")
    print("Ready for implementation.")


if __name__ == "__main__":
    main()
