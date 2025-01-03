#Importing the metplotlib for pie chart functionality, So make sure that you have already installed it i your system.
import os
from datetime import datetime
import matplotlib.pyplot as plt

def add_expense():
    category = input("Enter category (e.g., Food, Travel): ").strip()
    try:
        amount = float(input("Enter amount: ").strip())  # Ensure the amount is numeric.
    except ValueError:
        print("Invalid amount. Please enter a numeric value.")
        return
    date = input("Enter date (YYYY-MM-DD): ").strip()
    try:
        datetime.strptime(date, "%Y-%m-%d")  # Validate date format.
    except ValueError:
        print("Invalid date format. Please enter date as YYYY-MM-DD.")
        return

    with open("expenses.txt", "a") as file:
        file.write(f"{category},{amount},{date}\n")  # Append expense to the file.
    print("Expense added successfully!")

def view_expenses():
    if not os.path.exists("expenses.txt"):  # Check if the file exists.
        print("No expenses recorded.")
        return

    expenses = {}
    with open("expenses.txt", "r") as file:
        for line in file:
            category, amount, date = line.strip().split(",")  # Split each line into parts.
            if category not in expenses:
                expenses[category] = []
            expenses[category].append((float(amount), date))

    print("Expenses:")
    for category, records in expenses.items():
        print(f"{category}:")
        if not records:
            print("No expenses recorded.")
        else:
            for i, (amount, date) in enumerate(records, start=1):
                print(f"{i}. Amount: {amount} - Date: {date}")

def monthly_summary():
    if not os.path.exists("expenses.txt"):  # Check if the file exists.
        print("No expenses recorded.")
        return

    month_year = input("Enter month and year (YYYY-MM): ").strip()

  #Performing the Exceptional Handling using try and expect.
    try:
        datetime.strptime(month_year, "%Y-%m")  # Validate month-year format.
    except ValueError:
        print("Invalid format. Please enter as YYYY-MM.")
        return

    total_expenses = 0
    category_summary = {}

    with open("expenses.txt", "r") as file: #File handling
        for line in file:
            category, amount, date = line.strip().split(",")  # Split each line into parts.
            if date.startswith(month_year):  # Filter by the specified month.
                total_expenses += float(amount)
                if category not in category_summary:
                    category_summary[category] = 0
                category_summary[category] += float(amount)

    if not category_summary:
        print(f"No expenses recorded for {month_year}.")
        return

    print(f"Monthly Summary ({month_year}):")
    print(f"Total Expenses: {total_expenses}")
    print("By Category:")
    for category, total in category_summary.items():
        print(f"{category}: {total}")

    labels = category_summary.keys()
    sizes = category_summary.values()
    plt.figure(figsize=(8, 6))
    plt.pie(sizes, labels=labels, autopct="%1.1f%%", startangle=140)  # Create a pie chart.
    plt.title(f"Expense Distribution ({month_year})")
    plt.axis("equal")  # Ensure the pie chart is circular.
    plt.show()

def main(): #Created a main function where based on the if and else option the Expense tracker option can be used by the user.
    while True:
        print("Welcome to Personal Expense Tracker!")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Monthly Summary")
        print("4. Exit")
        choice = input("Enter your choice: ").strip()

        if choice == "1":
            add_expense()
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            monthly_summary()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
