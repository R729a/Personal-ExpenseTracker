													
import os
import csv
import datetime

# Initialize the expense file if it doesn't exist
def initialize_file():
    if not os.path.exists('expense.csv'):
        with open('expense.csv', 'w') as file:
            file.write('Date,Amount,Category,Description\n')

# Add a new expense to the file
def add_expense(date, amount, category, description):
    with open('expense.csv', 'a') as file:
        file.write(f"{date},{amount},{category},{description}\n")
    print("Expense added")

# View all expenses
def view_expense():
    with open('expense.csv', 'r') as file:
        lines = file.readlines()
        print(lines[0])  # print the header
        for line in lines[1:]:
            print(line)

# Filter expenses by date or category
def filter_expense(filter_by, filter_value):
    with open('expense.csv', 'r') as file:
        lines = file.readlines()
        print(lines[0])  # print the header
        for line in lines[1:]:
            data = line.strip().split(',')
            if filter_by == "date" and filter_value == data[0]:
                print(line)
            elif filter_by == 'category' and filter_value == data[2]:
                print(line)

# Delete a specific expense
def delete_expense(date, amount, category, description):
    lines = []
    with open('expense.csv', 'r') as file:
        lines = file.readlines()
    with open('expense.csv', 'w') as file:
        for line in lines:
            if line.strip() != f"{date},{amount},{category},{description}":
                file.write(line)
    print("Deleted successfully")

# Generate a summary of expenses for the current month
def monthly_summary():
    current_month = datetime.datetime.now().strftime("%Y-%m")
    total_expense = 0.0
    category_expense = {}

    with open('expense.csv', 'r') as file:
        lines = file.readlines()
        for line in lines[1:]:
            data = line.strip().split(',')
            if data[0].startswith(current_month):
                amount = float(data[1])
                category = data[2]
                total_expense += amount
                if category in category_expense:
                    category_expense[category] += amount
                else:
                    category_expense[category] = amount
    print(f"Total expense for {current_month}: {total_expense}")
    for category, amount in category_expense.items():
        print(f"{category}: {amount}")

# Main function to run the expense tracker
def main():
    print("Personal Expense Tracker")
    print()

    initialize_file()
    while True:
        print("1. Add expense")
        print("2. View expense")
        print("3. Filter expense")
        print("4. Delete expense")
        print("5. Monthly summary")
        print("6. Exit")
        print()

        choice = int(input("Select the choice: "))

        if choice == 1:
            date = input("Enter the date (YYYY-MM-DD): ")
            amount = float(input("Enter the amount: "))
            category = input("Enter the category: ")
            description = input("Enter the description: ")
            add_expense(date, amount, category, description)
            print()

        elif choice == 2:
            view_expense()

        elif choice == 3:
            filter_by = input("Filter by (date/category): ")
            filter_value = input(f"Enter {filter_by}: ")
            filter_expense(filter_by, filter_value)

        elif choice == 4:
            date = input("Enter the date (YYYY-MM-DD): ")
            amount = float(input("Enter the amount: "))
            category = input("Enter the category: ")
            description = input("Enter the description: ")
            delete_expense(date, amount, category, description)
            print()

        elif choice == 5:
            monthly_summary()

        elif choice == 6:
            print("Exit the program")
            break

if __name__ == "__main__":
    main()
