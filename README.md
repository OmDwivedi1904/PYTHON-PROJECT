# Personal Expense Tracker

## Overview
The Personal Expense Tracker is a Python-based system that allows users to:

1. Add expenses categorized by type (e.g., Food, Travel).
2. View all recorded expenses.
3. Get a monthly summary of expenses, including a pie chart visualization.

## Features
- **Add Expense:** Input category, amount, and date to record an expense.
- **View Expenses:** List expenses grouped by categories.
- **Monthly Summary:** Display total and categorized expenses for a specific month, along with a pie chart.
- **File Handling:** All data is stored persistently in a text file (`expenses.txt`).

## Prerequisites
- Python 3.6 or higher
- Matplotlib library

To install Matplotlib, run:
```bash
pip install matplotlib
```

## How to Run
1. Save the code into a Python file, e.g., `expense_tracker.py`.
2. Run the program:
   ```bash
   python expense_tracker.py
   ```

## User Flow

### Main Menu
Upon running the program, you will see:
```
Welcome to Personal Expense Tracker!
1. Add Expense
2. View Expenses
3. Monthly Summary
4. Exit
```
Enter the number corresponding to your desired option.

### Adding an Expense
You will be prompted to enter:
1. **Category** (e.g., Food, Travel).
2. **Amount** (numeric value).
3. **Date** (in `YYYY-MM-DD` format).

The expense is then stored in `expenses.txt`.

### Viewing Expenses
Displays a list of all expenses grouped by category, formatted as:
```
Expenses:
Food:
1. Amount: 200 - Date: 2024-12-23
Travel:
No expenses recorded.
```

### Monthly Summary
Enter the month and year (e.g., `2024-12`).
Displays:
- Total expenses for the month.
- Categorized breakdown of expenses.
- A pie chart showing expense distribution.

### Exiting
Select option `4` to exit the program.

## File Handling
- All expense data is stored in `expenses.txt` in the format:
  ```
  Category,Amount,Date
  ```
  Example:
  ```
  Food,200,2024-12-23
  Travel,150,2024-12-24
  ```

## Pie Chart Example
When viewing the monthly summary, a pie chart is generated showing the distribution of expenses by category.

Example:
If the data for December 2024 is:
```
Food,200,2024-12-23
Travel,150,2024-12-24
```
The pie chart will display:
- **Food:** 57.1%
- **Travel:** 42.9%

## Notes
- Ensure the `expenses.txt` file is in the same directory as the script.
- If the file does not exist, it will be created automatically.
- Invalid inputs are handled gracefully with appropriate error messages.

## Future Enhancements
- Add search functionality for specific dates or amounts.
- Export summary reports to a CSV file.
- Integrate a GUI for a more user-friendly experience.

