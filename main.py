"""
Student Expense Tracker - Main Menu Interface
Interactive command-line interface for managing expenses
"""

import expense_tracker


def display_menu():
    """Display the main menu options."""
    print("\n" + "=" * 50)
    print("STUDENT EXPENSE TRACKER")
    print("=" * 50)
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Total Spending")
    print("4. View Highest Spending Category")
    print("5. Set Monthly Budget")
    print("6. Exit")
    print("=" * 50)


def get_menu_choice():
    """Get and validate user's menu choice."""
    while True:
        try:
            choice = input("\nEnter your choice (1-6): ").strip()
            choice_num = int(choice)
            if 1 <= choice_num <= 6:
                return choice_num
            else:
                print(f"Error: Invalid choice '{choice}'. Please enter a number between 1 and 6.")
        except ValueError:
            print(f"Error: Invalid input '{choice}'. Please enter a number between 1 and 6.")


def prompt_add_expense():
    """Prompt user to add a new expense."""
    print("\n--- Add New Expense ---")
    
    # Get date
    while True:
        date_input = input("Enter date (YYYY-MM-DD): ").strip()
        try:
            expense_tracker.validate_date(date_input)
            break
        except ValueError as e:
            print(e)
    
    # Get amount
    while True:
        amount_input = input("Enter amount (0.01 to 1,000,000.00): ").strip()
        try:
            amount = expense_tracker.validate_amount(amount_input)
            break
        except ValueError as e:
            print(e)
    
    # Get category
    print("Valid categories: food, travel, recharge, other")
    while True:
        category_input = input("Enter category: ").strip()
        try:
            category = expense_tracker.validate_category(category_input)
            break
        except ValueError as e:
            print(e)
    
    # Add the expense
    expense_tracker.add_expense(date_input, amount, category)
    print("\n✓ Expense added successfully!")


def prompt_view_expenses():
    """Display all expenses."""
    print("\n--- All Expenses ---")
    expense_tracker.view_expenses()


def prompt_view_total():
    """Display total spending."""
    print("\n--- Total Spending ---")
    expense_tracker.view_total_spending()


def prompt_view_highest_category():
    """Display the highest spending category."""
    print("\n--- Highest Spending Category ---")
    
    if not expense_tracker.expense_list:
        print("No expense data available")
        return
    
    # Calculate category totals
    category_totals = {}
    for expense in expense_tracker.expense_list:
        cat = expense['category']
        category_totals[cat] = category_totals.get(cat, 0.0) + expense['amount']
    
    # Find highest
    if category_totals:
        highest_cat = max(category_totals, key=category_totals.get)
        highest_amount = category_totals[highest_cat]
        print(f"\nHighest spending category: {highest_cat}")
        print(f"Total spent: ${highest_amount:.2f}")
        
        # Show all category totals
        print("\n--- All Categories ---")
        for cat in sorted(category_totals.keys()):
            print(f"{cat:<12}: ${category_totals[cat]:>10.2f}")
    else:
        print("No expense data available")


def prompt_set_budget():
    """Prompt user to set monthly budget."""
    print("\n--- Set Monthly Budget ---")
    
    while True:
        budget_input = input("Enter monthly budget (0.01 to 999,999,999.99): ").strip()
        try:
            budget = expense_tracker.validate_amount(budget_input)
            if budget > 999_999_999.99:
                print(f"Invalid budget. You entered: '{budget_input}'")
                print("Budget must be between 0.01 and 999,999,999.99")
                continue
            break
        except ValueError as e:
            print(e)
    
    expense_tracker.monthly_budget = budget
    print(f"\n✓ Monthly budget set to: ${budget:.2f}")


def initialize_sample_data():
    """Add sample expenses if list is empty."""
    if not expense_tracker.expense_list:
        print("\n📝 Loading sample data...")
        expense_tracker.add_expense('2024-01-10', 150.00, 'food')
        expense_tracker.add_expense('2024-01-12', 80.50, 'travel')
        expense_tracker.add_expense('2024-01-15', 299.00, 'recharge')
        print("✓ 3 sample expenses loaded\n")


def main():
    """Main application loop."""
    print("\n" + "=" * 50)
    print("Welcome to Student Expense Tracker!")
    print("=" * 50)
    
    # Initialize with sample data
    initialize_sample_data()
    
    while True:
        display_menu()
        choice = get_menu_choice()
        
        if choice == 1:
            prompt_add_expense()
        elif choice == 2:
            prompt_view_expenses()
        elif choice == 3:
            prompt_view_total()
        elif choice == 4:
            prompt_view_highest_category()
        elif choice == 5:
            prompt_set_budget()
        elif choice == 6:
            print("\n" + "=" * 50)
            print("Thank you for using Student Expense Tracker!")
            print("Goodbye! 👋")
            print("=" * 50)
            break
        
        # Pause before showing menu again
        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
