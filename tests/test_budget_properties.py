"""
Property-based tests for budget management functionality.

Testing framework: hypothesis
Feature: student-expense-tracker
"""

import pytest
from hypothesis import given, strategies as st, settings
from datetime import datetime
import expense_tracker


# Helper strategies
def valid_budget_strategy():
    """Generate valid budget strings in range [0.01, 999999999.99] with max 2 decimals."""
    return st.floats(
        min_value=0.01,
        max_value=999_999_999.99,
        allow_nan=False,
        allow_infinity=False
    ).map(lambda x: f"{x:.2f}")


def invalid_budget_range_strategy():
    """Generate budgets outside valid range."""
    return st.one_of(
        st.floats(min_value=-1000.0, max_value=0.00).map(str),
        st.floats(min_value=999_999_999.99 + 0.01, max_value=2_000_000_000.0).map(str),
        st.just('0.00'),
        st.just('-10.00'),
    )


def non_numeric_budget_strategy():
    """Generate non-numeric strings."""
    return st.one_of(
        st.text(min_size=1).filter(lambda s: not s.replace('.', '', 1).replace('-', '', 1).isdigit()),
        st.just('abc'),
        st.just('12.34.56'),
        st.just(''),
    )


def excessive_decimal_budget_strategy():
    """Generate budgets with more than 2 decimal places."""
    return st.floats(
        min_value=0.01,
        max_value=10000.0
    ).map(lambda x: f"{x:.3f}")


def current_month_date_strategy():
    """Generate dates from the current calendar month."""
    now = datetime.now()
    year = now.year
    month = now.month
    
    # Generate days for current month
    return st.integers(min_value=1, max_value=28).map(
        lambda day: f"{year:04d}-{month:02d}-{day:02d}"
    )


def past_month_date_strategy():
    """Generate dates from previous months."""
    now = datetime.now()
    current_year = now.year
    current_month = now.month
    
    # Generate dates that are not from current month
    return st.one_of(
        st.integers(min_value=1, max_value=12).filter(
            lambda m: m != current_month
        ).map(lambda m: f"{current_year:04d}-{m:02d}-15"),
        st.just(f"{current_year - 1:04d}-12-15"),  # Last year
    )


# Property 13: Budget Validation
# **Validates: Requirements 5.2, 5.3**

@given(budget_str=valid_budget_strategy())
@settings(max_examples=100)
def test_property_budget_validation_accepts_valid_budgets(budget_str):
    """Property 13: Budget validation accepts valid budgets."""
    # Clear any existing budget
    expense_tracker.monthly_budget = None
    
    # Valid budgets should set without raising an exception
    expense_tracker.set_monthly_budget(budget_str)
    
    # Verify budget was set correctly
    expected = float(budget_str)
    assert expense_tracker.monthly_budget == expected
    assert 0.01 <= expense_tracker.monthly_budget <= 999_999_999.99


@given(budget_str=invalid_budget_range_strategy())
@settings(max_examples=100)
def test_property_budget_validation_rejects_out_of_range(budget_str):
    """Property 13: Budget validation rejects out-of-range budgets."""
    with pytest.raises(ValueError) as exc_info:
        expense_tracker.set_monthly_budget(budget_str)
    
    error_msg = str(exc_info.value)
    assert budget_str in error_msg
    assert '0.01' in error_msg and '999,999,999.99' in error_msg


@given(budget_str=non_numeric_budget_strategy())
@settings(max_examples=100)
def test_property_budget_validation_rejects_non_numeric(budget_str):
    """Property 13: Budget validation rejects non-numeric budgets."""
    with pytest.raises(ValueError) as exc_info:
        expense_tracker.set_monthly_budget(budget_str)
    
    error_msg = str(exc_info.value)
    assert budget_str in error_msg


@given(budget_str=excessive_decimal_budget_strategy())
@settings(max_examples=100)
def test_property_budget_validation_rejects_excessive_decimals(budget_str):
    """Property 13: Budget validation rejects budgets with more than 2 decimal places."""
    # Only test if the string actually has 3 decimal places
    if '.' in budget_str and len(budget_str.split('.')[1]) > 2:
        with pytest.raises(ValueError) as exc_info:
            expense_tracker.set_monthly_budget(budget_str)
        
        error_msg = str(exc_info.value)
        assert budget_str in error_msg


# Property 12: Budget Storage and Retrieval
# **Validates: Requirements 5.1, 5.2, 5.7**

@given(
    budget1=valid_budget_strategy(),
    budget2=valid_budget_strategy()
)
@settings(max_examples=100)
def test_property_budget_storage_and_retrieval(budget1, budget2):
    """Property 12: Budget storage stores value and subsequent operations use most recent value."""
    # Clear expense list and budget
    expense_tracker.expense_list.clear()
    expense_tracker.monthly_budget = None
    
    # Set first budget
    expense_tracker.set_monthly_budget(budget1)
    assert expense_tracker.monthly_budget == float(budget1)
    
    # Set second budget (should replace first)
    expense_tracker.set_monthly_budget(budget2)
    assert expense_tracker.monthly_budget == float(budget2)
    
    # Verify the most recent budget is used
    stored_budget = expense_tracker.monthly_budget
    assert stored_budget == float(budget2)


# Property 14: Budget Warning Trigger
# **Validates: Requirements 5.4, 5.5**

@given(
    budget=st.floats(min_value=100.0, max_value=1000.0).map(lambda x: f"{x:.2f}"),
    num_expenses=st.integers(min_value=1, max_value=5),
)
@settings(max_examples=100)
def test_property_budget_warning_trigger_when_exceeded(budget, num_expenses):
    """Property 14: Budget warning triggers when current month spending >= budget."""
    # Clear expense list and set budget
    expense_tracker.expense_list.clear()
    expense_tracker.monthly_budget = None
    expense_tracker.set_monthly_budget(budget)
    
    budget_value = float(budget)
    
    # Add expenses in current month that total >= budget
    # Distribute budget across expenses to ensure total exceeds budget
    amount_per_expense = (budget_value / num_expenses) + 1.0
    
    for i in range(num_expenses):
        now = datetime.now()
        date = f"{now.year:04d}-{now.month:02d}-{(i % 28) + 1:02d}"
        expense_tracker.add_expense(date, amount_per_expense, 'food')
    
    # Verify warning is triggered
    result = expense_tracker.check_budget_warning()
    assert result is True


@given(
    budget=st.floats(min_value=500.0, max_value=1000.0).map(lambda x: f"{x:.2f}"),
    num_expenses=st.integers(min_value=1, max_value=3),
)
@settings(max_examples=100)
def test_property_budget_warning_not_triggered_when_below(budget, num_expenses):
    """Property 14: Budget warning not triggered when spending < budget."""
    # Clear expense list and set budget
    expense_tracker.expense_list.clear()
    expense_tracker.monthly_budget = None
    expense_tracker.set_monthly_budget(budget)
    
    budget_value = float(budget)
    
    # Add expenses in current month that total < budget
    # Use small amounts to ensure total is below budget
    amount_per_expense = (budget_value / (num_expenses * 2))  # Half of distributed budget
    
    for i in range(num_expenses):
        now = datetime.now()
        date = f"{now.year:04d}-{now.month:02d}-{(i % 28) + 1:02d}"
        expense_tracker.add_expense(date, amount_per_expense, 'travel')
    
    # Verify warning is not triggered
    result = expense_tracker.check_budget_warning()
    assert result is False


# Property 15: Budget Warning Absence Without Budget
# **Validates: Requirements 5.6**

@given(
    num_expenses=st.integers(min_value=1, max_value=10),
    amount=st.floats(min_value=100.0, max_value=10000.0).map(lambda x: round(x, 2))
)
@settings(max_examples=100)
def test_property_budget_warning_absence_without_budget(num_expenses, amount):
    """Property 15: No budget warning when budget not set, regardless of spending."""
    # Clear expense list and ensure no budget is set
    expense_tracker.expense_list.clear()
    expense_tracker.monthly_budget = None
    
    # Add expenses in current month
    for i in range(num_expenses):
        now = datetime.now()
        date = f"{now.year:04d}-{now.month:02d}-{(i % 28) + 1:02d}"
        expense_tracker.add_expense(date, amount, 'other')
    
    # Verify no warning is triggered (returns False)
    result = expense_tracker.check_budget_warning()
    assert result is False


# Additional property: Budget warning only considers current month expenses

@given(
    budget=st.floats(min_value=100.0, max_value=500.0).map(lambda x: f"{x:.2f}"),
)
@settings(max_examples=100)
def test_property_budget_warning_ignores_past_months(budget):
    """Budget warning only considers expenses from current calendar month."""
    # Clear expense list and set budget
    expense_tracker.expense_list.clear()
    expense_tracker.monthly_budget = None
    expense_tracker.set_monthly_budget(budget)
    
    budget_value = float(budget)
    
    # Add large expense from previous month (should be ignored)
    expense_tracker.expense_list.append({
        'date': '2023-01-15',
        'amount': budget_value * 10,  # Way over budget
        'category': 'food'
    })
    
    # Add small expense from current month (below budget)
    now = datetime.now()
    current_date = f"{now.year:04d}-{now.month:02d}-15"
    expense_tracker.add_expense(current_date, budget_value / 10, 'travel')
    
    # Verify warning is not triggered (only current month counts)
    result = expense_tracker.check_budget_warning()
    assert result is False
