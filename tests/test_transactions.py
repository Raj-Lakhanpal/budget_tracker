import pytest
from tracker import BudgetTracker

def test_add_income_transaction():
    tracker = BudgetTracker()
    tracker.add_transaction(
        amount = 500,
        category = "Salary",
        tx_type = "income",
        date = "2025-07-13"
    )
    assert len(tracker.transactions) == 1
    assert tracker.transactions[0]['amount'] == 500

def test_invalid_transaction_type():
    tracker = BudgetTracker()
    with pytest.raises(ValueError):
        tracker.add_transaction(
            amount = 100,
            category = "Gift",
            tx_type="invalid_type",
            date="2025-07-13"
        )
def test_negative_amount():
    tracker = BudgetTracker()
    with pytest.raises(ValueError):
        tracker.add_transaction(
            amount = -50,
            category = "Food",
            tx_type="expense",
            date="2025-07-13"
        )

def test_bad_date_format():
    tracker = BudgetTracker()
    with pytest.raises(ValueError):
        tracker.add_transaction(200, "Rent", "expense", "13-07-2025")

def test_get_all_transactions_returns_all():
    tracker = BudgetTracker()
    tracker.add_transaction(100, "Salary", "income", "2025-07-01")
    tracker.add_transaction(50, "Groceries", "expense", "2025-07-02")

    all_tx = tracker.get_all_transactions()
    assert len(all_tx) == 2
    assert all_tx[0]['category'] == "Salary"
    assert all_tx[1]['category'] == "Groceries"

def test_get_all_transactions_emtpy():
    tracker = BudgetTracker()
    all_tx = tracker.get_all_transactions()
    assert all_tx == []
