class Reports:
    def __init__(self, expenses):
        self.expenses = expenses

    def total_expense(self):
        total = sum(e.amount for e in self.expenses)
        print(f"Total Expense: {total:.2f}")

    def category_summary(self):
        summary = {}
        for e in self.expenses:
            summary[e.category] = summary.get(e.category, 0) + e.amount

        print("\nCategory Summary")
        print("-" * 30)
        for cat, amt in summary.items():
            print(f"{cat:<15} {amt:.2f}")
