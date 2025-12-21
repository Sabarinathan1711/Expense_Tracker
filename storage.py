import csv
import os
from expense import Expense
from config import DATA_FILE

class Storage:
    def load(self):
        expenses = []
        if os.path.exists(DATA_FILE):
            with open(DATA_FILE, "r", newline="") as file:
                reader = csv.reader(file)
                next(reader, None)
                for row in reader:
                    expenses.append(
                        Expense(
                            int(row[0]),
                            row[1],
                            row[2],
                            float(row[3]),
                            row[4]
                        )
                    )
        return expenses

    def save(self, expenses):
        with open(DATA_FILE, "w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(
                ["ID", "Date", "Category", "Amount", "Note"]
            )
            for expense in expenses:
                writer.writerow(expense.to_row())
