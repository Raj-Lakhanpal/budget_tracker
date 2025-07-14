from datetime import datetime

class BudgetTracker:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, amount, category, tx_type, date):
        if amount <= 0:
            raise ValueError("Amount must be greater than 0")
        if tx_type not in ("income", "expense"):
            raise ValueError("Transaction type must be 'income' or 'expense'")
        try:
            datetime.strptime(date, "%Y-%m-%d")
        except ValueError:
            raise ValueError("Invalid Date Format. Expected YYYY-MM-DD")
        self.transactions.append({
            "amount": amount,
            "category": category,
            "type": tx_type,
            "date": date
        })