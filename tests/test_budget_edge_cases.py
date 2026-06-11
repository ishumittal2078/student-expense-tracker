"""
Unit tests for budget management edge cases.

Testing framework: pytest
Feature: student-expense-tracker
"""

import pytest
from datetime import datetime
import expense_tracker


def test_budget_warning_at_exact_threshold():
    """Test budget warning triggers when spending exactly equals budget."""
    # Clear expense list and set budget
    expense_tracker.expense_list.clear()
    expense_tracker.monthly_budget = None
    expense_tracker.set_monthly_budget('500.00')
    
    # Add expenses totaling exactly 500.00 in current month
    now = datetime.now()
    date1 = f"{now.year:04d}-{now.month:02d}-10"
    date2 = f"{now.year:04d}-{now.month:02d}-15"
    
    expense_tracker.add_expense(date1, 300.00, 'food')
    expense_tracker.add_expense(date2, 200.00, 'travel')
    
    # Verify warning is triggered at exact threshold
    result = expense_tracker.check_budget_warning()
    assert result is True


def test_budget_warning_just_below_threshold():
    """Test budget warning not triggered when spending is just below budget."""
    # Clear expense list and set budget
    expense_tracker.expense_list.clear()
    expense_tracker.monthly_budget = None
    expense_tracker.set_monthly_budget('500.00')
    
    # Add expenses totaling 499.99 (just below budget)
    now = datetime.now()
    date = f"{now.year:04d}-{now.month:02d}-10"
    
    expense_tracker.add_expense(date, 499.99, 'food')
    
    # Verify warning is not triggered
    result = expense_tracker.check_budget_warning()
    assert result is False


def test_budget_warning_disappears_when_below_budget():
    """Test warning state is recalculated each time (warning disappears when spending falls below)."""
    # Note: In the current implementation, expenses are only added, not removed.
    # This test verifies that check_budget_warning() recalculates each time.
    
    # Clear expense list and set budget
    expense_tracker.expense_list.clear()
    expense_tracker.monthly_budget = None
    expense_tracker.set_monthly_budget('500.00')
    
    # Add expense below budget
    now = datetime.now()
    date = f"{now.year:04d}-{now.month:02d}-10"
    expense_tracker.add_expense(date, 100.00, 'food')
    
    # Verify no warning
    assert expense_tracker.check_budget_warning() is False
    
    # Add more expenses to exceed budget
    date2 = f"{now.year:04d}-{now.month:02d}-15"
    expense_tracker.add_expense(date2, 450.00, 'travel')
    
    # Verify warning appears
    assert expense_tracker.check_budget_warning() is True
    
    # Simulate month change by clearing current month expenses
    # (In real app, month change would naturally reset the warning)
    expense_tracker.expense_list.clear()
    
    # Verify warning disappears with no current month expenses
    assert expense_tracker.check_budget_warning() is False


def test_month_boundary_crossing():
    """Test budget warning only considers current calendar month."""
    # Clear expense list and set budget
    expense_tracker.expense_list.clear()
    expense_tracker.monthly_budget = None
    expense_tracker.set_monthly_budget('100.00')
    
    # Get current month
    now = datetime.now()
    current_month = now.month
    current_year = now.year
    
    # Calculate previous month
    if current_month == 1:
        prev_month = 12
        prev_year = current_year - 1
    else:
        prev_month = current_month - 1
        prev_year = current_year
    
    # Add large expense from previous month
    prev_date = f"{prev_year:04d}-{prev_month:02d}-15"
    expense_tracker.expense_list.append({
        'date': prev_date,
        'amount': 500.00,
        'category': 'food'
    })
    
    # Add small expense from current month (below budget)
    current_date = f"{current_year:04d}-{current_month:02d}-15"
    expense_tracker.add_expense(current_date, 50.00, 'travel')
    
    # Verify warning is not triggered (only current month counts)
    result = expense_tracker.check_budget_warning()
    assert result is False
    
    # Add more to current month to exceed budget
    current_date2 = f"{current_year:04d}-{current_month:02d}-20"
    expense_tracker.add_expense(current_date2, 60.00, 'other')
    
    # Now warning should trigger (current month total is 110.00)
    result = expense_tracker.check_budget_warning()
    assert result is True


def test_budget_replacement():
    """Test setting a new budget replaces the previous budget."""
    # Clear and set initial budget
    expense_tracker.expense_list.clear()
    expense_tracker.monthly_budget = None
    
    expense_tracker.set_monthly_budget('100.00')
    assert expense_tracker.monthly_budget == 100.00
    
    # Replace with new budget
    expense_tracker.set_monthly_budget('500.00')
    assert expense_tracker.monthly_budget == 500.00
    
    # Add expenses and verify new budget is used
    now = datetime.now()
    date = f"{now.year:04d}-{now.month:02d}-10"
    expense_tracker.add_expense(date, 450.00, 'food')
    
    # Should not trigger warning (450 < 500)
    assert expense_tracker.check_budget_warning() is False
    
    # Add more to exceed new budget
    date2 = f"{now.year:04d}-{now.month:02d}-15"
    expense_tracker.add_expense(date2, 100.00, 'travel')
    
    # Now should trigger (550 >= 500)
    assert expense_tracker.check_budget_warning() is True


def test_budget_with_no_expenses():
    """Test budget warning with budget set but no expenses."""
    # Clear expense list and set budget
    expense_tracker.expense_list.clear()
    expense_tracker.monthly_budget = None
    expense_tracker.set_monthly_budget('100.00')
    
    # With no expenses, warning should not trigger
    result = expense_tracker.check_budget_warning()
    assert result is False


def test_budget_with_only_past_month_expenses():
    """Test budget warning with expenses only from past months."""
    # Clear expense list and set budget
    expense_tracker.expense_list.clear()
    expense_tracker.monthly_budget = None
    expense_tracker.set_monthly_budget('100.00')
    
    # Add expenses only from past months
    expense_tracker.expense_list.append({
        'date': '2023-01-15',
        'amount': 500.00,
        'category': 'food'
    })
    expense_tracker.expense_list.append({
        'date': '2023-02-20',
        'amount': 300.00,
        'category': 'travel'
    })
    
    # Warning should not trigger (no current month expenses)
    result = expense_tracker.check_budget_warning()
    assert result is False


def test_minimum_budget_value():
    """Test setting minimum valid budget (0.01)."""
    expense_tracker.monthly_budget = None
    expense_tracker.set_monthly_budget('0.01')
    assert expense_tracker.monthly_budget == 0.01


def test_maximum_budget_value():
    """Test setting maximum valid budget (999,999,999.99)."""
    expense_tracker.monthly_budget = None
    expense_tracker.set_monthly_budget('999999999.99')
    assert expense_tracker.monthly_budget == 999_999_999.99


def test_budget_confirmation_message(capsys):
    """Test that setting budget displays confirmation message."""
    expense_tracker.monthly_budget = None
    expense_tracker.set_monthly_budget('250.50')
    
    captured = capsys.readouterr()
    assert 'Monthly budget set to: $250.50' in captured.out


def test_display_budget_warning_message(capsys):
    """Test that display_budget_warning shows correct message."""
    # Set up conditions for warning
    expense_tracker.expense_list.clear()
    expense_tracker.monthly_budget = None
    expense_tracker.set_monthly_budget('100.00')
    
    # Add expense to trigger warning
    now = datetime.now()
    date = f"{now.year:04d}-{now.month:02d}-10"
    expense_tracker.add_expense(date, 100.00, 'food')
    
    # Clear previous output
    capsys.readouterr()
    
    # Call display_budget_warning
    expense_tracker.display_budget_warning()
    
    captured = capsys.readouterr()
    assert 'WARNING' in captured.out
    assert '100.00' in captured.out


def test_display_budget_warning_no_message_when_below(capsys):
    """Test that display_budget_warning shows nothing when below budget."""
    # Set up conditions without warning
    expense_tracker.expense_list.clear()
    expense_tracker.monthly_budget = None
    expense_tracker.set_monthly_budget('100.00')
    
    # Add expense below budget
    now = datetime.now()
    date = f"{now.year:04d}-{now.month:02d}-10"
    expense_tracker.add_expense(date, 50.00, 'food')
    
    # Clear previous output
    capsys.readouterr()
    
    # Call display_budget_warning
    expense_tracker.display_budget_warning()
    
    captured = capsys.readouterr()
    # Should not output warning
    assert 'WARNING' not in captured.out or captured.out.strip() == ''
