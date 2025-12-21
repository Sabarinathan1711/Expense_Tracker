from storage import Storage
from expense import Expense
from utils import get_today_date, validate_amount
from config import CATEGORIES

class ExpenseTracker:
    def __init__(self):
        self.storage = Storage()
        self.expenses = self.storage.load()

    def generate_id(self):
        if not self.expenses:
            return 1
        return max(e.expense_id for e in self.expenses) + 1

    def add_expense(self):
        date = input("Enter date (DD-MM-YYYY) or press Enter: ")
        if not date.strip():
            date = get_today_date()

        print("Available Categories:", ", ".join(CATEGORIES))
        category = input("Enter category: ")

        amount = input("Enter amount: ")
        while not validate_amount(amount):
            amount = input("Invalid amount. Enter again: ")
        amount = float(amount)

        note = input("Enter note: ")

        expense = Expense(
            self.generate_id(),
            date,
            category,
            amount,
            note
        )

        self.expenses.append(expense)
        self.storage.save(self.expenses)
        print("Expense added successfully.")

    def view_expenses(self):
        if not self.expenses:
            print("No expenses recorded.")
            return

        print("\nID  Date        Category        Amount    Note")
        print("-" * 60)
        for e in self.expenses:
            print(
                f"{e.expense_id:<3} "
                f"{e.date:<11} "
                f"{e.category:<14} "
                f"{e.amount:<8.2f} "
                f"{e.note}"
            )

    def delete_expense(self):
        self.view_expenses()
        try:
            exp_id = int(input("Enter Expense ID to delete: "))
            self.expenses = [
                e for e in self.expenses if e.expense_id != exp_id
            ]
            self.storage.save(self.expenses)
            print("Expense deleted.")
        except ValueError:
            print("Invalid ID.")
