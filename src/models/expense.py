"""Expense model for Student Expense Tracker."""
class Expense:
    """Represents a single expense entry.
    
    Attributes:
        date:YYYY-MM-DD format
        amount: Positive decimal value
        category: One of: 'food', 'travel', 'recharge', 'other'
    """
    
    def __init__(self, date: str, amount: float, category: str):
        self.date: str = date
        self.amount: float = amount
        self.category: str = category
    
    def to_dict(self) -> dict:
        """Convert expense to dictionary representation.
        
        Returns:
            Dictionary with keys: date, amount, category
        """
        return {
            'date': self.date,
            'amount': self.amount,
            'category': self.category
        }
    
    @staticmethod
    def from_dict(data: dict) -> 'Expense':
        """Create expense from dictionary.
        
        Args:
            data: Dictionary with keys: date, amount, category
            
        Returns:
            Expense instance created from dictionary data
        """
        return Expense(
            date=data['date'],
            amount=data['amount'],
            category=data['category']
        )
