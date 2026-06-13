import re

with open('expense_tracker.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix long error messages by using regular strings instead of f-strings
# for the fixed parts, keeping f-strings only for the variable parts

# Fix amount validation messages
content = re.sub(
    r'f"Amount must be between 0\.01 and 1,000,000\.00 with at most 2 decimal places\."',
    '"Amount must be between 0.01 and 1,000,000.00 with at most 2 decimal places."',
    content
)

# Fix budget validation messages
content = re.sub(
    r'f"Budget must be between 0\.01 and 999,999,999\.99 with at most 2 decimal places\."',
    '"Budget must be between 0.01 and 999,999,999.99 with at most 2 decimal places."',
    content
)

with open('expense_tracker.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("Done fixing PEP 8 violations")
