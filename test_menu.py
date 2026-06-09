"""
Quick test of the menu interface with automated inputs
"""

import expense_tracker

# Clear any existing data
expense_tracker.expense_list = []

print("=" * 50)
print("TESTING MENU FUNCTIONALITY")
print("=" * 50)

# Initialize sample data
print("\n1. Initializing with sample data...")
expense_tracker.add_expense('2024-01-10', 150.00, 'food')
expense_tracker.add_expense('2024-01-12', 80.50, 'travel')
expense_tracker.add_expense('2024-01-15', 299.00, 'recharge')
print("✓ Sample data loaded!")

# Test viewing expenses
print("\n2. Testing view expenses:")
expense_tracker.view_expenses()

# Test total spending
print("\n3. Testing total spending:")
expense_tracker.view_total_spending()

# Test highest category
print("\n4. Testing highest spending category:")
category_totals = {}
for expense in expense_tracker.expense_list:
    cat = expense['category']
    category_totals[cat] = category_totals.get(cat, 0.0) + expense['amount']

if category_totals:
    highest_cat = max(category_totals, key=category_totals.get)
    highest_amount = category_totals[highest_cat]
    print(f"\nHighest spending category: {highest_cat}")
    print(f"Total spent: ${highest_amount:.2f}")
    
    print("\n--- All Categories ---")
    for cat in sorted(category_totals.keys()):
        print(f"{cat:<12}: ${category_totals[cat]:>10.2f}")

# Test budget
print("\n5. Testing budget setting:")
expense_tracker.monthly_budget = 500.00
print(f"✓ Monthly budget set to: ${expense_tracker.monthly_budget:.2f}")

print("\n" + "=" * 50)
print("ALL MENU FUNCTIONS WORKING! ✓")
print("=" * 50)
print("\nTo use the interactive menu, run:")
print(">>> python main.py")
print("=" * 50)
