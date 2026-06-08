"""
Infrastructure verification test

This test verifies that the testing infrastructure is properly configured.
"""

import pytest
from hypothesis import given, strategies as st


def test_pytest_working():
    """Verify pytest is working correctly."""
    assert True


@pytest.mark.property
@given(x=st.integers())
def test_hypothesis_working(x):
    """Verify hypothesis is working correctly."""
    assert isinstance(x, int)


def test_can_import_expense_tracker(fresh_expense_tracker):
    """Verify we can import the expense_tracker module."""
    assert fresh_expense_tracker is not None
    assert hasattr(fresh_expense_tracker, 'expense_list')
    assert hasattr(fresh_expense_tracker, 'monthly_budget')
    assert hasattr(fresh_expense_tracker, 'VALID_CATEGORIES')
