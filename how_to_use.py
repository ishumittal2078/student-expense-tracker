"""
HOW TO USE THE STUDENT EXPENSE TRACKER
Step-by-step guide with examples
"""

import expense_tracker

print("=" * 60)
print("HOW TO USE THE STUDENT EXPENSE TRACKER")
print("=" * 60)

# Clear any existing data
expense_tracker.expense_list = []

print("\n" + "=" * 60)
print("STEP 1: ADD YOUR FIRST EXPENSE")
print("=" * 60)
print("\nFormat: add_expense(date, amount, category)")
print("  • date: 'YYYY-MM-DD' format (e.g., '2024-01-15')")
print("  • amount: number between 0.01 and 1,000,000.00")
print("  • category: 'food', 'travel', 'recharge', or 'other'")

print("\nExample:")
print(">>> expense_tracker.add_expense('2024-01-10', 150.50, 'food')")
expense_tracker.add_expense('2024-01-10', 150.50, 'food')

print("\n" + "=" * 60)
print("STEP 2: ADD MORE EXPENSES")
print("=" * 60)

print("\nAdding lunch expense:")
print(">>> expense_tracker.add_expense('2024-01-11', 45.00, 'food')")
expense_tracker.add_expense('2024-01-11', 45.00, 'food')

print("\nAdding bus fare:")
print(">>> expense_tracker.add_expense('2024-01-12', 25.50, 'travel')")
expense_tracker.add_expense('2024-01-12', 25.50, 'travel')

print("\nAdding mobile recharge:")
print(">>> expense_tracker.add_expense('2024-01-13', 299.00, 'recharge')")
expense_tracker.add_expense('2024-01-13', 299.00, 'recharge')

print("\nAdding miscellaneous:")
print(">>> expense_tracker.add_expense('2024-01-14', 75.25, 'other')")
expense_tracker.add_expense('2024-01-14', 75.25, 'other')

print("\n" + "=" * 60)
print("STEP 3: VIEW ALL YOUR EXPENSES")
print("=" * 60)

print("\nCommand:")
print(">>> expense_tracker.view_expenses()")
print()
expense_tracker.view_expenses()

print("\n" + "=" * 60)
print("STEP 4: CHECK TOTAL SPENDING")
print("=" * 60)

print("\nCommand:")
print(">>> expense_tracker.view_total_spending()")
expense_tracker.view_total_spending()

print("\n" + "=" * 60)
print("ADVANCED: INPUT VALIDATION")
print("=" * 60)

print("\n1. VALIDATING DATE:")
print("   >>> expense_tracker.validate_date('2024-01-15')")
try:
    expense_tracker.validate_date('2024-01-15')
    print("   ✓ Valid!")
except ValueError as e:
    print(f"   ✗ {e}")

print("\n2. VALIDATING AMOUNT:")
print("   >>> expense_tracker.validate_amount('150.50')")
try:
    amount = expense_tracker.validate_amount('150.50')
    print(f"   ✓ Valid! Amount: {amount}")
except ValueError as e:
    print(f"   ✗ {e}")

print("\n3. VALIDATING CATEGORY:")
print("   >>> expense_tracker.validate_category('Food')  # case-insensitive")
try:
    category = expense_tracker.validate_category('Food')
    print(f"   ✓ Valid! Normalized to: '{category}'")
except ValueError as e:
    print(f"   ✗ {e}")

print("\n" + "=" * 60)
print("COMMON MISTAKES TO AVOID")
print("=" * 60)

print("\n❌ WRONG DATE FORMAT:")
print("   expense_tracker.add_expense('01/15/2024', 150.50, 'food')")
print("   ✓ CORRECT: '2024-01-15'")

print("\n❌ INVALID CATEGORY:")
print("   expense_tracker.add_expense('2024-01-15', 150.50, 'shopping')")
print("   ✓ CORRECT: 'food', 'travel', 'recharge', or 'other'")

print("\n❌ AMOUNT TOO SMALL OR TOO LARGE:")
print("   expense_tracker.add_expense('2024-01-15', 0.00, 'food')")
print("   ✓ CORRECT: Must be between 0.01 and 1,000,000.00")

print("\n❌ TOO MANY DECIMAL PLACES:")
print("   expense_tracker.add_expense('2024-01-15', 150.505, 'food')")
print("   ✓ CORRECT: Maximum 2 decimal places (150.50)")

print("\n" + "=" * 60)
print("PYTHON CODE EXAMPLE")
print("=" * 60)

example_code = '''
# Import the module
import expense_tracker

# Add expenses
expense_tracker.add_expense('2024-01-10', 150.50, 'food')
expense_tracker.add_expense('2024-01-12', 80.75, 'travel')
expense_tracker.add_expense('2024-01-15', 299.00, 'recharge')

# View all expenses
expense_tracker.view_expenses()

# Check total spending
expense_tracker.view_total_spending()
'''

print(example_code)

print("=" * 60)
print("TIP: Categories are case-insensitive!")
print("  'Food', 'FOOD', 'food' are all valid and become 'food'")
print("=" * 60)
