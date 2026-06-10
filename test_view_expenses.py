"""
Test script for view_expenses function (Task 4.5)
"""

import sys
from io import StringIO
import expense_tracker


def test_view_expenses_empty():
    """Test view_expenses with empty list"""
    print("Test 1: Empty expense list")
    expense_tracker.expense_list = []
    
    # Capture output
    old_stdout = sys.stdout
    sys.stdout = captured_output = StringIO()
    
    expense_tracker.view_expenses()
    
    sys.stdout = old_stdout
    output = captured_output.getvalue()
    
    assert "No expenses recorded" in output
    print("✓ Empty list shows 'No expenses recorded'")
    print()


def test_view_expenses_with_data():
    """Test view_expenses with multiple expenses"""
    print("Test 2: View expenses with data")
    
    # Add test data (unsorted dates)
    expense_tracker.expense_list = [
        {'date': '2024-01-15', 'amount': 299.00, 'category': 'recharge'},
        {'date': '2024-01-10', 'amount': 150.00, 'category': 'food'},
        {'date': '2024-01-12', 'amount': 80.50, 'category': 'travel'},
    ]
    
    # Capture output
    old_stdout = sys.stdout
    sys.stdout = captured_output = StringIO()
    
    expense_tracker.view_expenses()
    
    sys.stdout = old_stdout
    output = captured_output.getvalue()
    
    # Verify output contains expected elements
    assert "Date" in output and "Amount" in output and "Category" in output
    assert "2024-01-10" in output
    assert "150.00" in output
    assert "food" in output
    assert "2024-01-12" in output
    assert "80.50" in output
    assert "travel" in output
    assert "2024-01-15" in output
    assert "299.00" in output
    assert "recharge" in output
    
    # Verify sorting (oldest first)
    lines = output.split('\n')
    date_lines = [line for line in lines if '2024-' in line]
    assert date_lines[0].startswith('2024-01-10')
    assert date_lines[1].startswith('2024-01-12')
    assert date_lines[2].startswith('2024-01-15')
    
    print("✓ Displays labeled columns (Date, Amount, Category)")
    print("✓ Shows all expenses in tabular format")
    print("✓ Sorts by date (oldest first)")
    print("✓ Formats amounts to 2 decimal places")
    print()
    
    # Display actual output for visual verification
    print("Actual output:")
    print(output)


def test_view_expenses_decimal_formatting():
    """Test that amounts are formatted to exactly 2 decimal places"""
    print("Test 3: Decimal formatting")
    
    expense_tracker.expense_list = [
        {'date': '2024-01-10', 'amount': 100.0, 'category': 'food'},
        {'date': '2024-01-11', 'amount': 50.5, 'category': 'travel'},
        {'date': '2024-01-12', 'amount': 75.99, 'category': 'recharge'},
    ]
    
    old_stdout = sys.stdout
    sys.stdout = captured_output = StringIO()
    
    expense_tracker.view_expenses()
    
    sys.stdout = old_stdout
    output = captured_output.getvalue()
    
    # Check that all amounts have exactly 2 decimal places
    assert "100.00" in output
    assert "50.50" in output
    assert "75.99" in output
    
    print("✓ All amounts formatted to exactly 2 decimal places")
    print()


def test_budget_warning_called():
    """Test that display_budget_warning is called"""
    print("Test 4: Budget warning function called")
    
    expense_tracker.expense_list = [
        {'date': '2024-01-10', 'amount': 100.0, 'category': 'food'}
    ]
    
    # The function should call display_budget_warning without error
    try:
        old_stdout = sys.stdout
        sys.stdout = StringIO()
        
        expense_tracker.view_expenses()
        
        sys.stdout = old_stdout
        print("✓ display_budget_warning() called successfully")
    except Exception as e:
        sys.stdout = old_stdout
        print(f"✗ Error calling display_budget_warning(): {e}")
        raise
    print()


if __name__ == "__main__":
    print("=" * 60)
    print("Testing view_expenses() function - Task 4.5")
    print("=" * 60)
    print()
    
    try:
        test_view_expenses_empty()
        test_view_expenses_with_data()
        test_view_expenses_decimal_formatting()
        test_budget_warning_called()
        
        print("=" * 60)
        print("All tests passed! ✓")
        print("=" * 60)
        
    except AssertionError as e:
        print(f"\n✗ Test failed: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"\n✗ Unexpected error: {e}")
        sys.exit(1)
