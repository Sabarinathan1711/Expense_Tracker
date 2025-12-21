
ExpenseTrackerPro is a Python-based console application designed to help users record, manage, and analyze their daily expenses.
The project follows a modular and structured approach, where each file has a clear responsibility. This makes the application easy to understand, maintain, and extend.

The main goal of this project is to demonstrate practical usage of Python programming concepts, including Object-Oriented Programming, file handling, and data processing.

Features

Add daily expenses with date, category, amount, and notes

View all recorded expenses in a clean tabular format

Delete unwanted expense records

Automatically store data using a CSV file

Calculate total expenses

Generate category-wise expense summary

Modular multi-file architecture

Simple and user-friendly menu-driven interface

Project Structure
ExpenseTrackerPro/
│
├── main.py        # Application entry point
├── config.py      # Configuration values and categories
├── utils.py       # Helper and validation functions
├── expense.py     # Expense data model
├── storage.py     # File handling and persistence logic
├── tracker.py     # Core expense management logic
├── reports.py     # Expense analysis and summaries
├── expenses.csv   # Stored expense records
└── README.md      # Project documentation

Technologies Used

Programming Language: Python

Concepts:

Object-Oriented Programming (OOP)

File Handling (CSV)

Modular Programming

Data Validation

Platform: Console / Terminal

How the Application Works

The user interacts with the program through a menu-driven interface.

Expenses are stored as objects and managed in memory.

Data is saved to a CSV file to ensure persistence.

Reports are generated dynamically based on stored data.

The program continues running until the user chooses to exit.

How to Run the Project

Make sure Python is installed on your system.

Download or clone this repository.

Navigate to the project folder.

Run the following command:

python main.py

Sample Menu
==== Expense Tracker Pro ====
1. Add Expense
2. View Expenses
3. Delete Expense
4. Total Expense
5. Category Summary
6. Exit

Use Cases

Students managing daily expenses

Beginners learning Python project structure

Academic mini or final year projects

Personal finance tracking

Future Enhancements

Monthly and yearly expense reports

Graphical charts for expense analysis

User authentication

GUI-based interface

Database integration

Conclusion

ExpenseTrackerPro is a simple yet powerful Python project that demonstrates real-world application of programming concepts. Its clean architecture and modular design make it suitable for learning, academic evaluation, and further enhancements.

Author

Developed as a Python learning and academic project.
