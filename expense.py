class Expense:
    def __init__(self, expense_id, date, category, amount, note):
        self.expense_id = expense_id
        self.date = date
        self.category = category
        self.amount = amount
        self.note = note

    def to_row(self):
        return [
            self.expense_id,
            self.date,
            self.category,
            self.amount,
            self.note
        ]
