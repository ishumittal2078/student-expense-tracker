"""
Quick demo of what the Student Expense Tracker can do now
"""

import expense_tracker

print("=" * 50)
print("STUDENT EXPENSE TRACKER - Current Features Demo")
print("=" * 50)

# Clear any existing data for clean demo
expense_tracker.expense_list = []

print("\n1. ADDING EXPENSES")
print("-" * 50)
# Add some expenses
expense_tracker.add_expense('2024-01-10', 150.50, 'food')
expense_tracker.add_expense('2024-01-12', 80.75, 'travel')
expense_tracker.add_expense('2024-01-15', 299.00, 'recharge')
expense_tracker.add_expense('2024-01-08', 45.25, 'other')

print("\n2. VIEWING ALL EXPENSES")
print("-" * 50)
expense_tracker.view_expenses()

print("\n3. CALCULATING TOTAL SPENDING")
print("-" * 50)
expense_tracker.view_total_spending()

print("\n4. INPUT VALIDATION EXAMPLES")
print("-" * 50)

# Test date validation
print("\n✓ Testing date validation:")
try:
    expense_tracker.validate_date('2024-01-15')
    print("  Valid date accepted: 2024-01-15")
except ValueError as e:
    print(f"  Error: {e}")

try:
    expense_tracker.validate_date('2024-02-30')
    print("  Invalid date accepted (shouldn't happen)")
except ValueError as e:
    print("  ✗ Invalid calendar date rejected: 2024-02-30")

# Test amount validation
print("\n✓ Testing amount validation:")
try:
    amount = expense_tracker.validate_amount('150.50')
    print(f"  Valid amount accepted: ${amount}")
except ValueError as e:
    print(f"  Error: {e}")

try:
    expense_tracker.validate_amount('1000000.50')
except ValueError as e:
    print("  ✗ Out-of-range amount rejected: 1000000.50")

# Test category validation
print("\n✓ Testing category validation:")
try:
    cat = expense_tracker.validate_category('FOOD')
    print(f"  Valid category accepted (case-insensitive): FOOD -> {cat}")
except ValueError as e:
    print(f"  Error: {e}")

try:
    expense_tracker.validate_category('shopping')
except ValueError as e:
    print("  ✗ Invalid category rejected: shopping")

print("\n" + "=" * 50)
print("WHAT'S WORKING:")
print("=" * 50)
print("✓ Add expenses with date, amount, and category")
print("✓ View all expenses in a formatted table")
print("✓ Calculate total spending")
print("✓ Sort expenses by date (oldest first)")
print("✓ Validate all inputs (date, amount, category)")
print("✓ Handle empty expense list gracefully")
print("✓ Case-insensitive category matching")
print("✓ Comprehensive error messages")
print("\n" + "=" * 50)
print("STILL TO IMPLEMENT:")
print("=" * 50)
print("⧗ Category analysis (highest spending)")
print("⧗ Monthly budget management")
print("⧗ Budget warnings")
print("⧗ Menu-driven CLI interface")
print("⧗ Sample data initialization")
print("=" * 50)
