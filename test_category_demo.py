"""
Quick demonstration of category analysis functionality.
"""

import expense_tracker

# Clear any existing expenses
expense_tracker.expense_list = []

# Add some test expenses
print("Adding test expenses...")
expense_tracker.add_expense('2024-01-10', 150.00, 'food')
expense_tracker.add_expense('2024-01-11', 80.50, 'travel')
expense_tracker.add_expense('2024-01-12', 299.00, 'recharge')
expense_tracker.add_expense('2024-01-13', 120.00, 'food')
expense_tracker.add_expense('2024-01-14', 45.75, 'travel')

print("\n" + "="*50)
print("Testing calculate_category_totals()...")
print("="*50)
totals = expense_tracker.calculate_category_totals()
print(f"Category totals: {totals}")

print("\n" + "="*50)
print("Testing find_highest_category()...")
print("="*50)
highest = expense_tracker.find_highest_category()
print(f"Highest category result: {highest}")

print("\n" + "="*50)
print("Testing view_highest_category()...")
print("="*50)
expense_tracker.view_highest_category()

print("\n" + "="*50)
print("Testing with empty list...")
print("="*50)
expense_tracker.expense_list = []
print("Empty list totals:", expense_tracker.calculate_category_totals())
print("Empty list highest:", expense_tracker.find_highest_category())
expense_tracker.view_highest_category()

print("\n" + "="*50)
print("All tests completed successfully!")
print("="*50)
