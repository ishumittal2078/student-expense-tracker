"""
Test the real application with simulated inputs using monkey patching.
This demonstrates the actual main_loop() running as it would with real user input.
"""

import expense_tracker as et
from unittest.mock import patch
from io import StringIO
import sys

def test_real_application():
    """Test the actual application with simulated user inputs."""
    
    print("=" * 70)
    print("TESTING REAL APPLICATION WITH SIMULATED USER INPUTS")
    print("=" * 70)
    
    # Clear any existing data
    et.expense_list.clear()
    et.monthly_budget = None
    
    # Simulate user inputs: 
    # 2 (View Expenses), 3 (View Total), 4 (View Highest), 
    # 5 (Set Budget), 400.00, 1 (Add Expense), 2024-01-20, 75.50, food,
    # 2 (View Expenses again), 6 (Exit)
    simulated_inputs = [
        '2',              # View All Expenses
        '3',              # View Total Spending
        '4',              # View Highest Spending Category
        '5', '400.00',    # Set Monthly Budget
        '1', '2024-01-20', '75.50', 'food',  # Add Expense
        '2',              # View All Expenses again
        '6'               # Exit
    ]
    
    # Create an iterator for inputs
    input_iterator = iter(simulated_inputs)
    
    # Capture output
    captured_output = StringIO()
    
    # Monkey patch input() and redirect stdout
    with patch('builtins.input', side_effect=lambda prompt: next(input_iterator)):
        with patch('sys.stdout', new=captured_output):
            try:
                et.main()
            except StopIteration:
                pass  # Expected when we run out of inputs
    
    # Get the output
    output = captured_output.getvalue()
    
    # Display the captured output
    print("\n" + "=" * 70)
    print("APPLICATION OUTPUT:")
    print("=" * 70)
    print(output)
    
    # Verify key elements
    print("\n" + "=" * 70)
    print("VERIFICATION CHECKS:")
    print("=" * 70)
    
    checks = [
        ("Welcome message displayed", "Welcome to Student Expense Tracker" in output),
        ("Sample data loaded", "Sample data has been loaded" in output),
        ("Menu displayed", "STUDENT EXPENSE TRACKER" in output),
        ("Sample expenses shown", "2024-01-10" in output and "150.00" in output),
        ("Total spending calculated", "Total Spending:" in output and "529.50" in output),
        ("Highest category identified", "Highest Spending Category: recharge" in output),
        ("Budget set successfully", "Monthly budget set to: $400.00" in output),
        ("New expense added", "Expense added: 2024-01-20, $75.50, food" in output),
        ("Exit message displayed", "Thank you for using" in output),
    ]
    
    all_passed = True
    for check_name, result in checks:
        status = "✓" if result else "✗"
        print(f"{status} {check_name}")
        if not result:
            all_passed = False
    
    print("\n" + "=" * 70)
    if all_passed:
        print("✓ ALL CHECKS PASSED - Application works correctly!")
    else:
        print("✗ Some checks failed - review output above")
    print("=" * 70)
    
    # Show final state
    print("\nFinal application state:")
    print(f"  Total expenses: {len(et.expense_list)}")
    print(f"  Monthly budget: ${et.monthly_budget:.2f}" if et.monthly_budget else "  Monthly budget: Not set")
    
    return all_passed

if __name__ == "__main__":
    success = test_real_application()
    sys.exit(0 if success else 1)
