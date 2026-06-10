"""
Property-based tests for category analysis operations.

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


# Property 9: Category Grouping Accuracy
# **Validates: Requirements 4.1**

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
def test_property_category_grouping_accuracy(expenses):
    """
    Property 9: For any expense list, the category analysis computes the sum
    of expenses for each category correctly.
    """
    # Setup: Clear expense list and add test expenses
    expense_tracker.expense_list = []
    for date, amount, category in expenses:
        expense_tracker.expense_list.append({
            'date': date,
            'amount': amount,
            'category': category
        })
    
    # Calculate expected totals manually
    expected_totals = {}
    for date, amount, category in expenses:
        if category in expected_totals:
            expected_totals[category] += amount
        else:
            expected_totals[category] = amount
    
    # Round expected totals to 2 decimal places
    expected_totals = {cat: round(amt, 2) for cat, amt in expected_totals.items()}
    
    # Action: Calculate category totals
    actual_totals = expense_tracker.calculate_category_totals()
    
    # Assert: All categories match
    assert set(actual_totals.keys()) == set(expected_totals.keys())
    
    # Assert: Each category total is correct
    for category in expected_totals:
        assert abs(actual_totals[category] - expected_totals[category]) < 0.01


# Property 10: Highest Category Identification
# **Validates: Requirements 4.2, 4.3**

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
def test_property_highest_category_identification(expenses):
    """
    Property 10: For any non-empty expense list, the system identifies a category
    with the maximum total spending, and that category's total is >= all other
    categories' totals.
    """
    # Setup: Clear expense list and add test expenses
    expense_tracker.expense_list = []
    for date, amount, category in expenses:
        expense_tracker.expense_list.append({
            'date': date,
            'amount': amount,
            'category': category
        })
    
    # Calculate expected totals
    expected_totals = {}
    for date, amount, category in expenses:
        if category in expected_totals:
            expected_totals[category] += amount
        else:
            expected_totals[category] = amount
    
    # Find expected maximum
    expected_max_amount = max(expected_totals.values())
    
    # Action: Find highest category
    result = expense_tracker.find_highest_category()
    
    # Assert: Result is not None
    assert result is not None
    
    # Assert: Result is a tuple with category and amount
    highest_category, highest_amount = result
    
    # Assert: The returned amount is indeed the maximum (or very close due to floating point)
    assert abs(highest_amount - expected_max_amount) < 0.01
    
    # Assert: The returned category's total is >= all other categories
    for category, total in expected_totals.items():
        assert highest_amount >= total - 0.01  # Allow small floating point difference


# Property 11: Tie-Breaking in Category Analysis
# **Validates: Requirements 4.5**

@given(
    tied_amount=valid_amount_strategy(),
    tied_categories=st.lists(
        valid_category_strategy(),
        min_size=2,
        max_size=4,
        unique=True
    ),
    date=valid_date_strategy()
)
@settings(max_examples=100)
def test_property_tie_breaking(tied_amount, tied_categories, date):
    """
    Property 11: For any expense list where multiple categories have equal
    maximum spending, the system returns one of those tied categories.
    """
    # Setup: Clear expense list and create tied scenario
    expense_tracker.expense_list = []
    
    # Add one expense with tied_amount for each tied category
    for category in tied_categories:
        expense_tracker.expense_list.append({
            'date': date,
            'amount': tied_amount,
            'category': category
        })
    
    # Action: Find highest category
    result = expense_tracker.find_highest_category()
    
    # Assert: Result is not None
    assert result is not None
    
    # Assert: Result is one of the tied categories
    highest_category, highest_amount = result
    assert highest_category in tied_categories
    
    # Assert: Amount matches the tied amount
    assert abs(highest_amount - tied_amount) < 0.01


# Unit tests for category edge cases
# **Validates: Requirements 4.4, 4.6**

def test_empty_list_highest_category():
    """
    Unit test: Empty list returns None from find_highest_category.
    Validates: Requirements 4.4
    """
    # Setup: Clear expense list
    expense_tracker.expense_list = []
    
    # Action: Find highest category
    result = expense_tracker.find_highest_category()
    
    # Assert: Result is None
    assert result is None


def test_empty_list_view_highest_category(capsys):
    """
    Unit test: Empty list displays 'No data available' message.
    Validates: Requirements 4.4
    """
    # Setup: Clear expense list
    expense_tracker.expense_list = []
    
    # Action: View highest category
    expense_tracker.view_highest_category()
    
    # Capture output
    captured = capsys.readouterr()
    output = captured.out
    
    # Assert: Message is displayed
    assert "No data available" in output


def test_single_category():
    """
    Unit test: Single category is returned as highest.
    """
    # Setup: Clear expense list and add expenses from one category
    expense_tracker.expense_list = [
        {'date': '2024-01-10', 'amount': 100.00, 'category': 'food'},
        {'date': '2024-01-11', 'amount': 50.00, 'category': 'food'}
    ]
    
    # Action: Find highest category
    result = expense_tracker.find_highest_category()
    
    # Assert: Result is the single category
    assert result is not None
    category, amount = result
    assert category == 'food'
    assert abs(amount - 150.00) < 0.01


def test_all_zero_amounts():
    """
    Unit test: All expenses with 0.00 amount still identifies a category.
    Note: 0.00 is not a valid amount per requirements (min 0.01), but testing
    the logic if such data existed.
    """
    # Setup: Clear expense list and add expenses with minimum valid amounts
    expense_tracker.expense_list = [
        {'date': '2024-01-10', 'amount': 0.01, 'category': 'food'},
        {'date': '2024-01-11', 'amount': 0.01, 'category': 'travel'}
    ]
    
    # Action: Find highest category
    result = expense_tracker.find_highest_category()
    
    # Assert: Result is not None (one of the categories is returned)
    assert result is not None
    category, amount = result
    assert category in ['food', 'travel']
    assert abs(amount - 0.01) < 0.01


def test_view_highest_category_format(capsys):
    """
    Unit test: view_highest_category displays category and amount with 2 decimals.
    """
    # Setup: Clear expense list and add test expenses
    expense_tracker.expense_list = [
        {'date': '2024-01-10', 'amount': 100.50, 'category': 'food'},
        {'date': '2024-01-11', 'amount': 50.25, 'category': 'travel'}
    ]
    
    # Action: View highest category
    expense_tracker.view_highest_category()
    
    # Capture output
    captured = capsys.readouterr()
    output = captured.out
    
    # Assert: Category and amount are displayed
    assert 'food' in output
    assert '100.50' in output
