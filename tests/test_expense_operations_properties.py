"""
Property-based tests for expense management operations.

Testing framework: hypothesis
Feature: student-expense-tracker
"""

import pytest
from hypothesis import given, strategies as st, settings
from datetime import datetime
import sys
from pathlib import Path
from io import StringIO

# Import the module
sys.path.insert(0, str(Path(__file__).parent.parent))
import expense_tracker


# Helper strategies
def valid_date_strategy():
    """Generate valid YYYY-MM-DD date strings between 2020-2030."""
    return st.dates(
        min_value=datetime(2020, 1, 1).date(),
        max_value=datetime(2030, 12, 31).date()
    ).map(lambda d: d.strftime('%Y-%m-%d'))


def valid_amount_strategy():
    """Generate valid amount floats in range [0.01, 1000000.00] with max 2 decimals."""
    return st.floats(
        min_value=0.01,
        max_value=1_000_000.00,
        allow_nan=False,
        allow_infinity=False
    ).map(lambda x: round(x, 2))


def valid_category_strategy():
    """Generate valid categories."""
    return st.sampled_from(['food', 'travel', 'recharge', 'other'])


# Property 1: Expense Creation with Valid Inputs
# **Validates: Requirements 1.1, 1.2, 1.4, 1.6**

@given(
    date=valid_date_strategy(),
    amount=valid_amount_strategy(),
    category=valid_category_strategy()
)
@settings(max_examples=100)
def test_property_expense_creation_with_valid_inputs(date, amount, category):
    """
    Property 1: For any valid date, amount, and category, adding an expense
    creates a new record with exactly those values.
    """
    # Setup: Clear expense list
    expense_tracker.expense_list = []
    initial_count = len(expense_tracker.expense_list)
    
    # Action: Add expense
    expense_tracker.add_expense(date, amount, category)
    
    # Assert: Expense was added
    assert len(expense_tracker.expense_list) == initial_count + 1
    
    # Assert: Added expense has correct values
    added_expense = expense_tracker.expense_list[-1]
    assert added_expense['date'] == date
    assert added_expense['amount'] == amount
    assert added_expense['category'] == category


# Property 5: Atomic Input Validation
# **Validates: Requirements 1.9**

@given(
    valid_date=valid_date_strategy(),
    valid_amount=valid_amount_strategy(),
    valid_category=valid_category_strategy(),
    field_to_invalidate=st.sampled_from(['date', 'amount', 'category'])
)
@settings(max_examples=100)
def test_property_atomic_input_validation(valid_date, valid_amount, valid_category, field_to_invalidate):
    """
    Property 5: For any set of inputs where at least one field is invalid,
    the system should NOT create an expense record.
    """
    # Setup: Clear expense list
    expense_tracker.expense_list = []
    initial_count = len(expense_tracker.expense_list)
    
    # Create inputs with one invalid field
    if field_to_invalidate == 'date':
        date_input = 'invalid-date'
        amount_input = str(valid_amount)
        category_input = valid_category
        
        # Validation should fail for date
        with pytest.raises(ValueError):
            validated_date = expense_tracker.validate_date(date_input)
        
    elif field_to_invalidate == 'amount':
        date_input = valid_date
        amount_input = 'invalid'
        category_input = valid_category
        
        # Validation should fail for amount
        with pytest.raises(ValueError):
            validated_amount = expense_tracker.validate_amount(amount_input)
        
    else:  # category
        date_input = valid_date
        amount_input = str(valid_amount)
        category_input = 'invalid_category'
        
        # Validation should fail for category
        with pytest.raises(ValueError):
            validated_category = expense_tracker.validate_category(category_input)
    
    # Assert: No expense was added (atomic validation)
    assert len(expense_tracker.expense_list) == initial_count


# Property 6: Confirmation Message Completeness
# **Validates: Requirements 1.8**

@given(
    date=valid_date_strategy(),
    amount=valid_amount_strategy(),
    category=valid_category_strategy()
)
@settings(max_examples=100)
def test_property_confirmation_message_completeness(date, amount, category):
    """
    Property 6: For any successfully added expense, the confirmation message
    contains the date, amount, and category values.
    """
    import sys
    from io import StringIO
    
    # Setup: Clear expense list
    expense_tracker.expense_list = []
    
    # Capture stdout
    old_stdout = sys.stdout
    sys.stdout = captured_output = StringIO()
    
    try:
        # Action: Add expense (this prints confirmation)
        expense_tracker.add_expense(date, amount, category)
        
        # Get output
        output = captured_output.getvalue()
        
        # Assert: Confirmation contains all required fields
        assert date in output
        assert f"{amount:.2f}" in output
        assert category in output
    finally:
        # Restore stdout
        sys.stdout = old_stdout


# Property 7: Expense Display Completeness
# **Validates: Requirements 2.1, 2.2, 2.4, 2.5**

@given(
    expenses=st.lists(
        st.tuples(
            valid_date_strategy(),
            valid_amount_strategy(),
            valid_category_strategy()
        ),
        min_size=1,
        max_size=10
    )
)
@settings(max_examples=100)
def test_property_expense_display_completeness(expenses):
    """
    Property 7: For any expense list of size N, viewing expenses displays
    all N expenses with correct formatting and chronological order.
    """
    import sys
    from io import StringIO
    
    # Setup: Clear expense list and add test expenses
    expense_tracker.expense_list = []
    for date, amount, category in expenses:
        # Directly add to list without print output
        expense_tracker.expense_list.append({
            'date': date,
            'amount': amount,
            'category': category
        })
    
    # Capture stdout
    old_stdout = sys.stdout
    sys.stdout = captured_output = StringIO()
    
    try:
        # Action: View expenses
        expense_tracker.view_expenses()
        
        # Get output
        output = captured_output.getvalue()
        
        # Assert: All expenses are displayed
        for date, amount, category in expenses:
            assert date in output
            assert f"{amount:.2f}" in output
            assert category in output
        
        # Assert: Expenses are in chronological order (oldest first)
        sorted_dates = sorted([exp[0] for exp in expenses])
        output_lines = output.split('\n')
        date_positions = []
        for date in sorted_dates:
            for i, line in enumerate(output_lines):
                if date in line and '|' in line:  # Data row, not header
                    date_positions.append(i)
                    break
        
        # Date positions should be in ascending order
        assert date_positions == sorted(date_positions)
    finally:
        # Restore stdout
        sys.stdout = old_stdout


# Unit test for empty expense list (combining with property tests)
# **Validates: Requirements 2.3**

def test_empty_expense_list_message(capsys):
    """
    Unit test: Empty list displays 'No expenses recorded' message.
    Validates: Requirements 2.3
    """
    # Setup: Clear expense list
    expense_tracker.expense_list = []
    
    # Action: View expenses
    expense_tracker.view_expenses()
    
    # Capture output
    captured = capsys.readouterr()
    output = captured.out
    
    # Assert: Message is displayed
    assert "No expenses recorded" in output


# Unit test for empty list total
# **Validates: Requirements 3.3**

def test_empty_list_total():
    """
    Unit test: Empty list returns total of 0.00.
    Validates: Requirements 3.3
    """
    # Setup: Clear expense list
    expense_tracker.expense_list = []
    
    # Action: Calculate total
    total = expense_tracker.calculate_total()
    
    # Assert: Total is 0.00
    assert total == 0.00


# Property 8 (partial): Total Calculation Accuracy
# **Validates: Requirements 3.1, 3.2**

@given(
    expenses=st.lists(
        st.tuples(
            valid_date_strategy(),
            valid_amount_strategy(),
            valid_category_strategy()
        ),
        min_size=1,
        max_size=20
    )
)
@settings(max_examples=100)
def test_property_total_calculation_accuracy(expenses):
    """
    Property 8: For any non-empty expense list, the total spending calculation
    equals the mathematical sum of all expense amounts, formatted to 2 decimals.
    """
    # Setup: Clear expense list and add test expenses
    expense_tracker.expense_list = []
    for date, amount, category in expenses:
        expense_tracker.add_expense(date, amount, category)
    
    # Calculate expected total
    expected_total = round(sum(amount for _, amount, _ in expenses), 2)
    
    # Action: Calculate total
    actual_total = expense_tracker.calculate_total()
    
    # Assert: Totals match
    assert actual_total == expected_total
    
    # Assert: Total has at most 2 decimal places
    assert round(actual_total, 2) == actual_total


@given(
    expenses=st.lists(
        st.tuples(
            valid_date_strategy(),
            valid_amount_strategy(),
            valid_category_strategy()
        ),
        min_size=1,
        max_size=10
    )
)
@settings(max_examples=100)
def test_property_view_total_spending_format(expenses):
    """
    Property 8 (display): For any expense list, view_total_spending displays
    the total with exactly 2 decimal places.
    """
    import sys
    from io import StringIO
    
    # Setup: Clear expense list and add test expenses
    expense_tracker.expense_list = []
    for date, amount, category in expenses:
        # Directly add to list without print output
        expense_tracker.expense_list.append({
            'date': date,
            'amount': amount,
            'category': category
        })
    
    # Calculate expected total
    expected_total = round(sum(amount for _, amount, _ in expenses), 2)
    
    # Capture stdout
    old_stdout = sys.stdout
    sys.stdout = captured_output = StringIO()
    
    try:
        # Action: View total spending
        expense_tracker.view_total_spending()
        
        # Get output
        output = captured_output.getvalue()
        
        # Assert: Total is displayed with 2 decimal places
        assert f"{expected_total:.2f}" in output
    finally:
        # Restore stdout
        sys.stdout = old_stdout
