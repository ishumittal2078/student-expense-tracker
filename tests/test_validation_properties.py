"""
Property-based tests for validation functions.

Testing framework: hypothesis
Feature: student-expense-tracker
"""

import pytest
from hypothesis import given, strategies as st, settings
from datetime import datetime, timedelta
import expense_tracker


# Helper strategies
def valid_date_strategy():
    """Generate valid YYYY-MM-DD date strings between 2020-2030."""
    return st.dates(
        min_value=datetime(2020, 1, 1).date(),
        max_value=datetime(2030, 12, 31).date()
    ).map(lambda d: d.strftime('%Y-%m-%d'))


def invalid_date_format_strategy():
    """Generate strings that are not in YYYY-MM-DD format."""
    return st.one_of(
        st.text(min_size=1, max_size=20).filter(
            lambda s: not (len(s) == 10 and s[4] == '-' and s[7] == '-')
        ),
        st.from_regex(r'\d{4}/\d{2}/\d{2}', fullmatch=True),  # Wrong separator
        st.from_regex(r'\d{2}-\d{2}-\d{4}', fullmatch=True),  # Wrong order
    )


def invalid_calendar_date_strategy():
    """Generate strings in YYYY-MM-DD format but invalid calendar dates."""
    return st.sampled_from([
        '2024-02-30',  # February 30th doesn't exist
        '2024-04-31',  # April has only 30 days
        '2024-13-01',  # Month 13 doesn't exist
        '2024-00-15',  # Month 0 doesn't exist
        '2024-06-00',  # Day 0 doesn't exist
        '2023-02-29',  # Not a leap year
    ])


def valid_amount_strategy():
    """Generate valid amount strings in range [0.01, 1000000.00] with max 2 decimals."""
    return st.floats(
        min_value=0.01,
        max_value=1_000_000.00,
        allow_nan=False,
        allow_infinity=False
    ).map(lambda x: f"{x:.2f}")


def out_of_range_amount_strategy():
    """Generate amounts outside valid range."""
    return st.one_of(
        st.floats(min_value=-1000.0, max_value=0.00).map(str),
        st.floats(min_value=1_000_000.01, max_value=10_000_000.0).map(str),
        st.just('0.00'),
        st.just('-5.50'),
    )


def non_numeric_amount_strategy():
    """Generate non-numeric strings."""
    return st.one_of(
        st.text(min_size=1).filter(lambda s: not s.replace('.', '', 1).replace('-', '', 1).isdigit()),
        st.just('abc'),
        st.just('12.34.56'),
        st.just(''),
    )


def excessive_decimal_amount_strategy():
    """Generate amounts with more than 2 decimal places."""
    return st.floats(
        min_value=0.01,
        max_value=1000.0
    ).map(lambda x: f"{x:.3f}")


def valid_category_strategy():
    """Generate valid categories with various casings."""
    base_categories = ['food', 'travel', 'recharge', 'other']
    return st.sampled_from(base_categories).flatmap(
        lambda cat: st.sampled_from([
            cat.lower(),
            cat.upper(),
            cat.capitalize(),
            cat[:1].upper() + cat[1:].lower()
        ])
    )


def invalid_category_strategy():
    """Generate invalid category strings."""
    return st.one_of(
        st.text(min_size=1).filter(
            lambda s: s.lower() not in {'food', 'travel', 'recharge', 'other'}
        ),
        st.sampled_from(['shopping', 'entertainment', 'bills', 'misc', '']),
    )


# Property 4: Date Validation
# **Validates: Requirements 1.6, 1.7**

@given(date_str=valid_date_strategy())
@settings(max_examples=100)
def test_property_date_validation_accepts_valid_dates(date_str):
    """Property 4: Date validation accepts valid YYYY-MM-DD dates."""
    # Valid dates should pass without raising an exception
    result = expense_tracker.validate_date(date_str)
    assert result is True


@given(date_str=invalid_date_format_strategy())
@settings(max_examples=100)
def test_property_date_validation_rejects_invalid_formats(date_str):
    """Property 4: Date validation rejects invalid date formats."""
    with pytest.raises(ValueError) as exc_info:
        expense_tracker.validate_date(date_str)
    
    error_msg = str(exc_info.value)
    assert date_str in error_msg
    assert 'YYYY-MM-DD' in error_msg


@given(date_str=invalid_calendar_date_strategy())
@settings(max_examples=100)
def test_property_date_validation_rejects_invalid_calendar_dates(date_str):
    """Property 4: Date validation rejects invalid calendar dates."""
    with pytest.raises(ValueError) as exc_info:
        expense_tracker.validate_date(date_str)
    
    error_msg = str(exc_info.value)
    assert date_str in error_msg


# Property 3: Amount Validation
# **Validates: Requirements 1.4, 1.5, 3.4**

@given(amount_str=valid_amount_strategy())
@settings(max_examples=100)
def test_property_amount_validation_accepts_valid_amounts(amount_str):
    """Property 3: Amount validation accepts valid amounts."""
    result = expense_tracker.validate_amount(amount_str)
    assert isinstance(result, float)
    assert 0.01 <= result <= 1_000_000.00


@given(amount_str=out_of_range_amount_strategy())
@settings(max_examples=100)
def test_property_amount_validation_rejects_out_of_range(amount_str):
    """Property 3: Amount validation rejects out-of-range values."""
    with pytest.raises(ValueError) as exc_info:
        expense_tracker.validate_amount(amount_str)
    
    error_msg = str(exc_info.value)
    assert amount_str in error_msg
    assert '0.01' in error_msg and '1,000,000.00' in error_msg


@given(amount_str=non_numeric_amount_strategy())
@settings(max_examples=100)
def test_property_amount_validation_rejects_non_numeric(amount_str):
    """Property 3: Amount validation rejects non-numeric inputs."""
    with pytest.raises(ValueError) as exc_info:
        expense_tracker.validate_amount(amount_str)
    
    error_msg = str(exc_info.value)
    assert amount_str in error_msg


@given(amount_str=excessive_decimal_amount_strategy())
@settings(max_examples=100)
def test_property_amount_validation_rejects_excessive_decimals(amount_str):
    """Property 3: Amount validation rejects amounts with more than 2 decimal places."""
    # Only test if the string actually has 3 decimal places
    if '.' in amount_str and len(amount_str.split('.')[1]) > 2:
        with pytest.raises(ValueError) as exc_info:
            expense_tracker.validate_amount(amount_str)
        
        error_msg = str(exc_info.value)
        assert amount_str in error_msg


# Property 2: Category Validation
# **Validates: Requirements 1.2, 1.3**

@given(category_str=valid_category_strategy())
@settings(max_examples=100)
def test_property_category_validation_accepts_valid_categories(category_str):
    """Property 2: Category validation accepts valid categories (case-insensitive)."""
    result = expense_tracker.validate_category(category_str)
    assert result in {'food', 'travel', 'recharge', 'other'}
    assert result == category_str.lower()


@given(category_str=invalid_category_strategy())
@settings(max_examples=100)
def test_property_category_validation_rejects_invalid_categories(category_str):
    """Property 2: Category validation rejects invalid categories."""
    with pytest.raises(ValueError) as exc_info:
        expense_tracker.validate_category(category_str)
    
    error_msg = str(exc_info.value)
    assert category_str in error_msg
    # Check that valid categories are mentioned
    assert any(cat in error_msg for cat in ['food', 'travel', 'recharge', 'other'])
