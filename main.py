from tracker import ExpenseTracker
from reports import Reports

def main():
    tracker = ExpenseTracker()

    while True:
        print("\n==== Expense Tracker Pro ====")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Delete Expense")
        print("4. Total Expense")
        print("5. Category Summary")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            tracker.add_expense()
        elif choice == "2":
            tracker.view_expenses()
        elif choice == "3":
            tracker.delete_expense()
        elif choice == "4":
            Reports(tracker.expenses).total_expense()
        elif choice == "5":
            Reports(tracker.expenses).category_summary()
        elif choice == "6":
            print("Thank you for using Expense Tracker Pro.")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
