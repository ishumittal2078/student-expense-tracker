"""
Pytest configuration and shared fixtures for test suite
"""

import pytest
import sys
from pathlib import Path

# Add parent directory to path to import expense_tracker module
sys.path.insert(0, str(Path(__file__).parent.parent))


@pytest.fixture
def fresh_expense_tracker():
    """
    Fixture that provides a clean expense tracker state for each test.
    Resets global state to ensure test isolation.
    """
    import expense_tracker
    
    # Store original state
    original_expenses = expense_tracker.expense_list.copy()
    original_budget = expense_tracker.monthly_budget
    
    # Reset to clean state
    expense_tracker.expense_list = []
    expense_tracker.monthly_budget = None
    
    yield expense_tracker
    
    # Restore original state after test
    expense_tracker.expense_list = original_expenses
    expense_tracker.monthly_budget = original_budget


@pytest.fixture
def sample_expenses():
    """Fixture providing sample expense data for testing."""
    return [
        {'date': '2024-01-10', 'amount': 150.00, 'category': 'food'},
        {'date': '2024-01-12', 'amount': 80.50, 'category': 'travel'},
        {'date': '2024-01-15', 'amount': 299.00, 'category': 'recharge'}
    ]
