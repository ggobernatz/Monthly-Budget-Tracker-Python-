Monthly Budget Tracker (Python)
Project Overview

The Monthly Budget Tracker is a Python console application that helps users track their monthly income and expenses. Users can categorize spending, calculate remaining balances, and view a mini dashboard to compare historical budgets.

This project demonstrates practical Python skills including functions, loops, dictionaries, file handling, input validation, and formatted output.

Features

- Enter monthly income and multiple expenses with categories.

- Calculate total expenses, remaining balance, and category percentages.

- Optional notes for each month (e.g., “Vacation month”).

- Expenses displayed from highest to lowest spending for easy insight.

- Save and load budgets using budget_history.txt.

- Mini dashboard to view all previous months at a glance.

- Menu-based navigation: New Budget, View Dashboard, Exit.

Python Concepts Used

- Functions & Modular Code – enter_budget() and view_dashboard()

- Lists & Dictionaries – Track multiple expenses and categories

- Loops & Input Validation – Ensures valid income, expense, and date inputs

- File Handling – Persistent history saved to a text file

- Sorting & Formatting – Clean console output using f-strings

- Regex – Validate date input in MM/DD/YYYY format

How to Run
Using Terminal / PowerShell (Recommended)
cd "path_to_your_script"
python first_program.py
Using Double-Click (Windows)

Optional: Create a run_budget.bat file with:

@echo off
python "first_program.py"
pause

Double-click run_budget.bat to run safely and keep the console open.

Example Output
--- Budget Summary for 03/02/2026 ---
Note: Vacation month
Monthly Income: $3000.00
Total Expenses: $1150.00
Remaining Balance: $1850.00

Expense Breakdown by Category:
Rent         : $800.00 (26.67%) of income
Food         : $350.00 (11.67%) of income
Potential Upgrades

Track statistics across months (average expenses per category, month with highest savings)

Graphical dashboard using matplotlib or seaborn

Convert to executable (.exe) using PyInstaller
