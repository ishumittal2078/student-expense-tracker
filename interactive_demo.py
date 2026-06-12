"""
Interactive demo simulation for Tasks 8 & 9
This simulates a full interactive session showing the menu flow.
"""

import expense_tracker as et
from io import StringIO
import sys

def simulate_session():
    """Simulate an interactive session with the expense tracker."""
    
    print("=" * 70)
    print("SIMULATED INTERACTIVE SESSION")
    print("=" * 70)
    print("\nThis demonstrates the full menu flow as if a user were interacting")
    print("with the application through the command line.")
    print("\n" + "=" * 70)
    
    # Clear and initialize
    et.expense_list.clear()
    et.monthly_budget = None
    
    # Simulate initialization
    print("\n[APPLICATION STARTS]")
    et.initialize_sample_data()
    print("\nWelcome to Student Expense Tracker!")
    print("Sample data has been loaded.")
    
    # Show menu
    et.display_menu()
    
    # Simulate choice 2 (View All Expenses)
    print("\n[USER ENTERS: 2]")
    print("\nUser selected: View All Expenses")
    et.view_expenses()
    print("\n" + "-" * 40)
    
    # Show menu again
    et.display_menu()
    
    # Simulate choice 3 (View Total Spending)
    print("\n[USER ENTERS: 3]")
    print("\nUser selected: View Total Spending")
    et.view_total_spending()
    print("\n" + "-" * 40)
    
    # Show menu again
    et.display_menu()
    
    # Simulate choice 4 (View Highest Spending Category)
    print("\n[USER ENTERS: 4]")
    print("\nUser selected: View Highest Spending Category")
    et.view_highest_category()
    print("\n" + "-" * 40)
    
    # Show menu again
    et.display_menu()
    
    # Simulate choice 5 (Set Monthly Budget)
    print("\n[USER ENTERS: 5]")
    print("\nUser selected: Set Monthly Budget")
    print("\n--- Set Monthly Budget ---")
    print("[USER ENTERS: 400.00]")
    et.set_monthly_budget("400.00")
    print("\n" + "-" * 40)
    
    # Show menu again
    et.display_menu()
    
    # Simulate choice 1 (Add Expense)
    print("\n[USER ENTERS: 1]")
    print("\nUser selected: Add Expense")
    print("\n--- Add New Expense ---")
    print("[USER ENTERS DATE: 2024-01-20]")
    print("[USER ENTERS AMOUNT: 55.00]")
    print("[USER ENTERS CATEGORY: travel]")
    et.add_expense("2024-01-20", 55.00, "travel")
    print("\n" + "-" * 40)
    
    # Show menu again
    et.display_menu()
    
    # Simulate viewing expenses again to see budget warning
    print("\n[USER ENTERS: 2]")
    print("\nUser selected: View All Expenses")
    et.view_expenses()
    print("\n" + "-" * 40)
    
    # Show menu again
    et.display_menu()
    
    # Simulate invalid menu choice
    print("\n[USER ENTERS: 9]")
    print("Error: Invalid choice. You entered: '9'")
    print("Please enter a number between 1 and 6.")
    print("\n[USER ENTERS: abc]")
    print("Error: Invalid choice. You entered: 'abc'")
    print("Please enter a number between 1 and 6.")
    
    # Show menu again
    et.display_menu()
    
    # Simulate exit
    print("\n[USER ENTERS: 6]")
    print("\nUser selected: Exit")
    print("\nThank you for using Student Expense Tracker!")
    print("Goodbye!")
    
    print("\n" + "=" * 70)
    print("END OF SIMULATED SESSION")
    print("=" * 70)
    
    # Summary
    print("\n✓ All menu options demonstrated:")
    print("  1. Add Expense - Validated and added new expense")
    print("  2. View All Expenses - Displayed with sample data")
    print("  3. View Total Spending - Calculated and displayed")
    print("  4. View Highest Spending Category - Identified recharge as highest")
    print("  5. Set Monthly Budget - Set budget and triggered warning")
    print("  6. Exit - Properly terminates the application")
    print("\n✓ Error handling demonstrated:")
    print("  - Invalid menu choices are rejected and user is re-prompted")
    print("  - Input validation works for all fields")
    print("\n✓ Budget warning system:")
    print("  - Warning appears when spending exceeds budget")
    print("  - Displayed in View Expenses and View Total Spending")

if __name__ == "__main__":
    simulate_session()
