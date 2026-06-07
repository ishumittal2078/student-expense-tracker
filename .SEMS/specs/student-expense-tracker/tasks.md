# Implementation Plan: Student Expense Tracker

## Overview

This task list implements a Python-based command-line expense tracking application. The implementation follows a procedural style with optional object-oriented support, uses in-memory storage, and includes comprehensive property-based testing using the Hypothesis library. The system validates all user inputs, provides budget monitoring, and supports expense analysis by category.

## Tasks

- [ ] 1. Set up project structure and testing infrastructure
  - Create main application file: `expense_tracker.py`
  - Create test directory structure: `tests/`
  - Set up `requirements.txt` with Hypothesis and pytest dependencies
  - Create test configuration files (pytest.ini or similar)
  - Initialize git repository if not already present
  - _Requirements: 8.1, 9.1, 9.2_

- [ ] 2. Implement core data structures and validation functions
  - [ ] 2.1 Create Expense data structure using dictionaries
    - Define expense dictionary format: `{'date': str, 'amount': float, 'category': str}`
    - Create module-level storage: `expense_list` (list) and `monthly_budget` (float or None)
    - _Requirements: 8.1, 8.3_

  - [ ] 2.2 Implement date validation function
    - Create `validate_date(date_str)` using `datetime.strptime()`
    - Accept YYYY-MM-DD format only
    - Validate against calendar dates (reject 2024-02-30, etc.)
    - Return boolean or raise ValueError with specific error message
    - _Requirements: 1.6, 1.7_

  - [ ]* 2.3 Write property test for date validation
    - **Property 4: Date Validation**
    - **Validates: Requirements 1.6, 1.7**
    - Test with valid dates (accepted), invalid formats (rejected), invalid calendar dates (rejected)

  - [ ] 2.4 Implement amount validation function
    - Create `validate_amount(amount_str)` checking numeric, range [0.01, 1000000.00]
    - Validate maximum 2 decimal places using string manipulation
    - Return float or raise ValueError with invalid value and valid range
    - _Requirements: 1.4, 1.5, 3.4_

  - [ ]* 2.5 Write property test for amount validation
    - **Property 3: Amount Validation**
    - **Validates: Requirements 1.4, 1.5, 3.4**
    - Test with valid amounts (accepted), out-of-range values (rejected), non-numeric inputs (rejected), excessive decimals (rejected)

  - [ ] 2.6 Implement category validation function
    - Create `validate_category(category_str)` checking against valid set
    - Define `VALID_CATEGORIES = {'food', 'travel', 'recharge', 'other'}`
    - Support case-insensitive matching
    - Return normalized string or raise ValueError with invalid value and valid options
    - _Requirements: 1.2, 1.3_

  - [ ]* 2.7 Write property test for category validation
    - **Property 2: Category Validation**
    - **Validates: Requirements 1.2, 1.3**
    - Test with valid categories including case variations (accepted), invalid categories (rejected)

- [ ] 3. Checkpoint - Ensure validation tests pass
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 4. Implement expense management operations
  - [ ] 4.1 Create add_expense function
    - Implement `add_expense(date, amount, category)` accepting validated inputs
    - Create expense dictionary and append to `expense_list`
    - Display confirmation message with date, amount (2 decimals), and category
    - _Requirements: 1.1, 1.8_

  - [ ]* 4.2 Write property test for expense creation
    - **Property 1: Expense Creation with Valid Inputs**
    - **Validates: Requirements 1.1, 1.2, 1.4, 1.6**
    - Generate valid inputs, verify expense added to list with correct values

  - [ ]* 4.3 Write property test for atomic validation
    - **Property 5: Atomic Input Validation**
    - **Validates: Requirements 1.9**
    - Test that invalid input in any field prevents record creation

  - [ ]* 4.4 Write property test for confirmation message
    - **Property 6: Confirmation Message Completeness**
    - **Validates: Requirements 1.8**
    - Verify confirmation contains date, amount, and category

  - [ ] 4.5 Create view_expenses function
    - Implement `view_expenses()` displaying all expenses in tabular format
    - Sort expenses by date (oldest first) using `sorted(expense_list, key=lambda x: x['date'])`
    - Display labeled columns: Date, Amount, Category
    - Format amounts to 2 decimal places using f"{amount:.2f}"
    - Handle empty list with "No expenses recorded" message
    - Call `display_budget_warning()` at the end
    - _Requirements: 2.1, 2.2, 2.3, 2.4, 2.5_

  - [ ]* 4.6 Write property test for expense display completeness
    - **Property 7: Expense Display Completeness**
    - **Validates: Requirements 2.1, 2.2, 2.4, 2.5**
    - Verify all N expenses displayed with correct formatting and chronological order

  - [ ]* 4.7 Write unit tests for empty expense list
    - Test empty list displays "No expenses recorded" message
    - _Requirements: 2.3_

  - [ ] 4.8 Create calculate_total function
    - Implement `calculate_total()` summing all expense amounts
    - Return float with 2 decimal precision
    - Return 0.00 for empty list
    - _Requirements: 3.1, 3.3_

  - [ ] 4.9 Create view_total_spending function
    - Implement `view_total_spending()` displaying total with 2 decimals
    - Call `calculate_total()` and format result
    - Call `display_budget_warning()` at the end
    - _Requirements: 3.2, 3.3_

  - [ ]* 4.10 Write property test for total calculation accuracy
    - **Property 8: Total Calculation Accuracy**
    - **Validates: Requirements 3.1, 3.2**
    - Verify total equals mathematical sum of all amounts

  - [ ]* 4.11 Write property test for decimal formatting consistency
    - **Property 21: Decimal Formatting Consistency**
    - **Validates: Requirements 2.5, 3.2**
    - Verify all amount displays use exactly 2 decimal places

- [ ] 5. Checkpoint - Ensure core expense operations work
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 6. Implement category analysis functionality
  - [ ] 6.1 Create calculate_category_totals function
    - Implement `calculate_category_totals()` grouping expenses by category
    - Return dictionary mapping category to total amount
    - Handle empty list by returning empty dictionary
    - _Requirements: 4.1_

  - [ ]* 6.2 Write property test for category grouping accuracy
    - **Property 9: Category Grouping Accuracy**
    - **Validates: Requirements 4.1**
    - Verify sum for each category equals mathematical sum of matching expenses

  - [ ] 6.3 Create find_highest_category function
    - Implement `find_highest_category()` identifying max spending category
    - Return tuple (category, amount) or None for empty list
    - Handle ties by returning any one winner
    - _Requirements: 4.2, 4.4, 4.5_

  - [ ]* 6.4 Write property test for highest category identification
    - **Property 10: Highest Category Identification**
    - **Validates: Requirements 4.2, 4.3**
    - Verify identified category has total >= all other categories

  - [ ]* 6.5 Write property test for tie-breaking
    - **Property 11: Tie-Breaking in Category Analysis**
    - **Validates: Requirements 4.5**
    - Test that one of tied categories is returned when multiple have equal max

  - [ ] 6.6 Create view_highest_category function
    - Implement `view_highest_category()` displaying highest category and amount
    - Handle empty list with "No data available" message
    - Format amount to 2 decimal places
    - _Requirements: 4.3, 4.4_

  - [ ]* 6.7 Write unit tests for category edge cases
    - Test empty list returns appropriate message
    - Test single category
    - Test all expenses with 0.00 amount
    - _Requirements: 4.4, 4.6_

- [ ] 7. Implement budget management functionality
  - [ ] 7.1 Create set_monthly_budget function
    - Implement `set_monthly_budget(budget_str)` validating and storing budget
    - Validate numeric, range [0.01, 999999999.99], max 2 decimals
    - Update global `monthly_budget` variable
    - Display confirmation message with formatted budget value
    - _Requirements: 5.1, 5.2, 5.3, 5.7_

  - [ ]* 7.2 Write property test for budget validation
    - **Property 13: Budget Validation**
    - **Validates: Requirements 5.2, 5.3**
    - Test valid budgets (accepted), invalid budgets (rejected with error message)

  - [ ]* 7.3 Write property test for budget storage and retrieval
    - **Property 12: Budget Storage and Retrieval**
    - **Validates: Requirements 5.1, 5.2, 5.7**
    - Verify set budget value is stored and used in subsequent checks

  - [ ] 7.4 Create check_budget_warning function
    - Implement `check_budget_warning()` comparing current month spending to budget
    - Get current month/year using `datetime.now()`
    - Filter expenses by current calendar month (match YYYY-MM prefix)
    - Return True if month total >= budget, False otherwise
    - Return False if budget not set
    - _Requirements: 5.4, 5.6, 5.8_

  - [ ]* 7.5 Write property test for budget warning trigger
    - **Property 14: Budget Warning Trigger**
    - **Validates: Requirements 5.4, 5.5**
    - Verify warning displayed when current month spending >= budget

  - [ ]* 7.6 Write property test for budget warning absence
    - **Property 15: Budget Warning Absence Without Budget**
    - **Validates: Requirements 5.6**
    - Verify no warning when budget not set regardless of spending

  - [ ] 7.7 Create display_budget_warning function
    - Implement `display_budget_warning()` showing warning message
    - Call `check_budget_warning()` and conditionally display
    - Format message with budget value to 2 decimals
    - _Requirements: 5.5_

  - [ ]* 7.8 Write unit tests for budget edge cases
    - Test budget warning at exact threshold
    - Test warning disappears when spending falls below budget
    - Test month boundary crossing

- [ ] 8. Implement CLI menu system
  - [ ] 8.1 Create display_menu function
    - Implement `display_menu()` printing 6 menu options
    - Include visual separator and clear labeling
    - Options: Add Expense, View All Expenses, View Total Spending, View Highest Spending Category, Set Monthly Budget, Exit
    - _Requirements: 7.1_

  - [ ]* 8.2 Write unit test for menu display structure
    - Verify menu contains all 6 required options
    - _Requirements: 7.1_

  - [ ] 8.3 Create get_menu_choice function
    - Implement `get_menu_choice()` reading and validating menu input
    - Accept integers 1-6 or corresponding strings
    - Display error message with invalid input for non-matching input
    - Re-prompt until valid choice received
    - _Requirements: 7.2, 7.3_

  - [ ]* 8.4 Write property test for menu input validation
    - **Property 16: Menu Input Validation**
    - **Validates: Requirements 7.2, 7.3**
    - Test valid inputs (accepted), invalid inputs (rejected with error and re-prompt)

  - [ ] 8.5 Create prompt_add_expense function
    - Implement `prompt_add_expense()` gathering expense inputs
    - Prompt for date with format hint (YYYY-MM-DD)
    - Prompt for amount with range hint (0.01 to 1,000,000.00)
    - Prompt for category with valid options listed
    - Call validation functions and display specific error messages
    - Only call `add_expense()` if all validations pass
    - _Requirements: 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.9_

  - [ ] 8.6 Create prompt_set_budget function
    - Implement `prompt_set_budget()` gathering budget input
    - Prompt for budget amount with range hint
    - Call `set_monthly_budget()` or display error
    - _Requirements: 5.1, 5.2, 5.3_

  - [ ] 8.7 Create main_loop function
    - Implement `main_loop()` orchestrating menu flow
    - Initialize sample data at start
    - Display menu, get choice, execute action
    - Display separator after each action
    - Loop until exit option selected
    - _Requirements: 7.4, 7.5, 7.7_

  - [ ]* 8.8 Write property test for action loop continuation
    - **Property 17: Action Loop Continuation**
    - **Validates: Requirements 7.5, 7.7**
    - Verify menu redisplays after actions until exit selected

  - [ ] 8.9 Add error recovery to main_loop
    - Wrap operations in try-except blocks
    - Catch unexpected exceptions and display user-friendly message
    - Return to menu on errors without terminating
    - _Requirements: 7.6_

  - [ ]* 8.10 Write property test for error recovery
    - **Property 18: Error Recovery**
    - **Validates: Requirements 7.6**
    - Verify system returns to menu after runtime errors

  - [ ]* 8.11 Write unit test for exit functionality
    - Verify exit option terminates the application loop
    - _Requirements: 7.4_

- [ ] 9. Implement sample data initialization
  - [ ] 9.1 Create initialize_sample_data function
    - Implement `initialize_sample_data()` adding 3 sample expenses
    - Add expenses covering at least 3 categories (food, travel, recharge)
    - Use valid dates, amounts, and categories
    - Sample: `[{'date': '2024-01-10', 'amount': 150.00, 'category': 'food'}, ...]`
    - _Requirements: 6.1, 6.2_

  - [ ]* 9.2 Write unit tests for sample data
    - Test exactly 3 sample expenses added on initialization
    - Test sample expenses span at least 3 categories
    - Test view expenses displays sample data without user additions
    - _Requirements: 6.1, 6.2, 6.3_

- [ ] 10. Checkpoint - Ensure full application works end-to-end
  - Ensure all tests pass, ask the user if questions arise.

- [ ] 11. Implement remaining property-based tests
  - [ ]* 11.1 Write property test for expense persistence
    - **Property 19: Expense Persistence During Session**
    - **Validates: Requirements 8.4**
    - Verify expenses remain unchanged throughout session operations

  - [ ]* 11.2 Write property test for storage capacity
    - **Property 20: Storage Capacity**
    - **Validates: Requirements 8.6**
    - Test system can store and retrieve up to 1000 expenses without data loss

- [ ] 12. Add code quality improvements
  - [ ] 12.1 Apply PEP 8 formatting
    - Run flake8 validation and fix all errors
    - Ensure maximum line length of 79 characters
    - Verify snake_case for functions/variables, PascalCase for classes
    - _Requirements: 10.1, 10.3, 10.5_

  - [ ] 12.2 Add documentation and comments
    - Add docstrings for functions longer than 10 lines
    - Comment complex logic with nesting depth > 2
    - Ensure function/variable names are descriptive (2-50 characters)
    - _Requirements: 10.1, 10.2_

  - [ ] 12.3 Verify function complexity constraints
    - Ensure no function exceeds 50 lines
    - Ensure maximum nesting depth of 3 levels
    - Refactor if necessary
    - _Requirements: 10.4_

- [ ] 13. Create project documentation
  - Create README.md with usage instructions
  - Document how to run the application
  - Document how to run tests
  - Include example usage scenarios
  - List dependencies in requirements.txt

- [ ] 14. Final integration testing and validation
  - [ ]* 14.1 Run complete test suite
    - Execute all property-based tests with 100+ iterations
    - Execute all unit tests
    - Verify 100% of properties pass
    - Generate test coverage report

  - [ ]* 14.2 Manual CLI testing
    - Test complete user flow: add → view → analyze → budget → exit
    - Verify error messages display correctly for all invalid inputs
    - Test budget warning appears correctly
    - Verify sample data loads on startup

  - [ ] 14.3 Verify all requirements covered
    - Cross-reference task list against requirements document
    - Ensure each requirement has corresponding implementation
    - Ensure each design property has corresponding test

- [ ] 15. Final checkpoint - Ensure all tests pass
  - Ensure all tests pass, ask the user if questions arise.

## Notes

- Tasks marked with `*` are optional test tasks and can be skipped for faster MVP delivery
- Each implementation task references specific requirements for traceability
- Property-based tests validate the 21 correctness properties defined in the design document
- Unit tests validate specific examples, edge cases, and integration points
- The implementation uses Python 3.6+ with only standard library modules plus Hypothesis for testing
- Checkpoints ensure incremental validation throughout development
- All validation functions should provide specific error messages including the invalid value and valid format/range
- The application maintains in-memory storage only; data is discarded on termination
- Budget warnings check current calendar month expenses against the set monthly budget

## Task Dependency Graph

```json
{
  "waves": [
    { "id": 0, "tasks": ["1"] },
    { "id": 1, "tasks": ["2.1"] },
    { "id": 2, "tasks": ["2.2", "2.4", "2.6"] },
    { "id": 3, "tasks": ["2.3", "2.5", "2.7"] },
    { "id": 4, "tasks": ["4.1", "4.5", "4.8", "4.9"] },
    { "id": 5, "tasks": ["4.2", "4.3", "4.4", "4.6", "4.7", "4.10", "4.11"] },
    { "id": 6, "tasks": ["6.1", "6.3", "6.6"] },
    { "id": 7, "tasks": ["6.2", "6.4", "6.5", "6.7"] },
    { "id": 8, "tasks": ["7.1", "7.4", "7.7"] },
    { "id": 9, "tasks": ["7.2", "7.3", "7.5", "7.6", "7.8"] },
    { "id": 10, "tasks": ["8.1", "8.3", "8.5", "8.6", "9.1"] },
    { "id": 11, "tasks": ["8.2", "8.4", "8.7", "9.2"] },
    { "id": 12, "tasks": ["8.9"] },
    { "id": 13, "tasks": ["8.8", "8.10", "8.11"] },
    { "id": 14, "tasks": ["11.1", "11.2"] },
    { "id": 15, "tasks": ["12.1", "12.2", "12.3"] },
    { "id": 16, "tasks": ["13"] },
    { "id": 17, "tasks": ["14.1", "14.2", "14.3"] }
  ]
}
```
