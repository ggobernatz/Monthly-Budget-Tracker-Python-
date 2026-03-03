import re  # Regular expressions for date validation

# File to store all budget history
HISTORY_FILE = "budget_history.txt"

# ----------------------------
# Helper Functions
# ----------------------------

def pause():
    """Pause the program so the user can read output before returning to menu."""
    input("\nPress Enter to continue...")

def validate_date(date_str):
    """Return True if date_str matches MM/DD/YYYY format."""
    return re.match(r"^(0[1-9]|1[0-2])/([0-2][0-9]|3[01])/([0-9]{4})$", date_str)

def enter_budget():
    """
    Function to enter a new monthly budget.
    Demonstrates:
        - Input validation
        - Looping until correct input
        - Dictionaries for category totals
        - Lists for storing multiple expense entries
    """
    print("\n--- Enter a New Monthly Budget ---")

    # Date input with validation
    while True:
        date = input("Enter the date for this budget (MM/DD/YYYY): ")
        if validate_date(date):
            break
        print("Invalid date format. Please use MM/DD/YYYY.")

    # Optional note for this month
    note = input("Add an optional note for this month (or press Enter to skip): ")

    # Income input with error handling
    while True:
        try:
            income = float(input("Enter your monthly income: "))
            if income < 0:
                print("Income cannot be negative. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    # Initialize lists for expenses and categories
    expenses = []
    categories = []

    while True:
        expense_input = input("Enter an expense amount (or type 'done'): ")
        if expense_input.lower() == "done":
            break

        # Validate expense input
        try:
            expense = float(expense_input)
            if expense < 0:
                print("Expense cannot be negative. Try again.")
                continue
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # Get category and store in lowercase
        category = input("Enter a category for this expense (food, rent, gas, etc.): ")
        categories.append(category.lower())
        expenses.append(expense)

    # ----------------------------
    # Calculate totals and percentages
    # ----------------------------
    total_expenses = sum(expenses)  # Sum all expenses
    balance = income - total_expenses  # Remaining balance

    # Use a dictionary to calculate totals by category
    category_totals = {}
    for i in range(len(expenses)):
        cat = categories[i]
        category_totals[cat] = category_totals.get(cat, 0) + expenses[i]

    # Calculate percentage of income spent per category
    category_percentages = {cat: (total / income) * 100 for cat, total in category_totals.items()}

    # ----------------------------
    # Display summary
    # ----------------------------
    print(f"\n------ Budget Summary for {date} ------")
    if note:
        print(f"Note: {note}")
    print(f"Monthly Income: ${income:.2f}")
    print(f"Total Expenses: ${total_expenses:.2f}")
    print(f"Remaining Balance: ${balance:.2f}")

    print("\nExpense Breakdown by Category (Highest to Lowest Spending):")
    # Sorted by spending amount descending
    for cat, total in sorted(category_totals.items(), key=lambda x: x[1], reverse=True):
        print(f"{cat.capitalize():<12} : ${total:>8.2f} ({category_percentages[cat]:>6.2f}%) of income")

    # ----------------------------
    # Save summary to file
    # ----------------------------
    with open(HISTORY_FILE, "a") as file:
        file.write(f"Date: {date}\n")
        if note:
            file.write(f"Note: {note}\n")
        file.write(f"Income: {income:.2f}\n")
        file.write(f"Total Expenses: {total_expenses:.2f}\n")
        file.write(f"Remaining Balance: {balance:.2f}\n")
        file.write("Expense Breakdown:\n")
        for cat, total in sorted(category_totals.items(), key=lambda x: x[1], reverse=True):
            file.write(f"{cat.capitalize():<12} : {total:>8.2f} ({category_percentages[cat]:.2f}%)\n")
        file.write("---END---\n")  # Separator for each month

    print("\nSummary saved to budget_history.txt!")
    pause()

# ----------------------------
# Function to view dashboard
# ----------------------------
def view_dashboard():
    """
    Reads the budget_history.txt file and prints all months.
    Demonstrates:
        - File handling
        - String manipulation
        - Splitting data into logical blocks
    """
    print("\n------ Mini Dashboard ------")
    try:
        with open(HISTORY_FILE, "r") as file:
            content = file.read()
    except FileNotFoundError:
        print("No budget history found.")
        pause()
        return

    months = content.strip().split("---END---")
    if not months or months == [""]:
        print("No budget history to display.")
        pause()
        return

    for month in months:
        month = month.strip()
        if month:
            print("\n" + month)
    pause()

# ----------------------------
# Main Program Loop
# ----------------------------
while True:
    print("\n=== Monthly Budget Tracker ===")
    print("1. Enter a new budget")
    print("2. View budget dashboard")
    print("3. Exit")

    choice = input("Select an option (1-3): ")

    # Menu logic
    if choice == "1":
        enter_budget()
    elif choice == "2":
        view_dashboard()
    elif choice == "3":
        print("\nThank you for using the Budget Tracker!")
        break
    else:
        print("Invalid choice. Please select 1, 2, or 3.")

# Final pause to prevent instant closing when double-clicked
input("\nPress Enter to exit the program...")
