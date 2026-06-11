"""
Manual test to demonstrate budget management functionality.
"""

import expense_tracker
from datetime import datetime

# Clear any existing data
expense_tracker.expense_list.clear()
expense_tracker.monthly_budget = None

print("=" * 60)
print("BUDGET MANAGEMENT FUNCTIONALITY TEST")
print("=" * 60)

# Test 1: Set a monthly budget
print("\n1. Setting monthly budget to $500.00")
expense_tracker.set_monthly_budget('500.00')

# Test 2: Add expenses below budget
print("\n2. Adding expenses for current month (below budget)")
now = datetime.now()
date1 = f"{now.year:04d}-{now.month:02d}-05"
date2 = f"{now.year:04d}-{now.month:02d}-10"

expense_tracker.add_expense(date1, 150.00, 'food')
expense_tracker.add_expense(date2, 100.00, 'travel')

print("\n3. Viewing total spending (should be $250.00, no warning)")
expense_tracker.view_total_spending()

# Test 3: Add more expenses to exceed budget
print("\n4. Adding more expenses to exceed budget")
date3 = f"{now.year:04d}-{now.month:02d}-15"
date4 = f"{now.year:04d}-{now.month:02d}-20"

expense_tracker.add_expense(date3, 200.00, 'recharge')
expense_tracker.add_expense(date4, 100.00, 'other')

print("\n5. Viewing total spending (should be $550.00, WARNING should appear)")
expense_tracker.view_total_spending()

# Test 4: View all expenses with warning
print("\n6. Viewing all expenses (WARNING should appear)")
expense_tracker.view_expenses()

# Test 5: Replace budget
print("\n7. Replacing budget with $600.00")
expense_tracker.set_monthly_budget('600.00')

print("\n8. Viewing total spending (should be $550.00, no warning with new budget)")
expense_tracker.view_total_spending()

# Test 6: Invalid budget
print("\n9. Trying to set invalid budget (should show error)")
try:
    expense_tracker.set_monthly_budget('abc')
except ValueError as e:
    print(f"Error caught: {e}")

print("\n10. Trying to set out-of-range budget (should show error)")
try:
    expense_tracker.set_monthly_budget('1000000000.00')
except ValueError as e:
    print(f"Error caught: {e}")

print("\n" + "=" * 60)
print("BUDGET MANAGEMENT FUNCTIONALITY TEST COMPLETE")
print("=" * 60)
