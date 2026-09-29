import csv
import os

FILE_NAME = "expenses.csv"


def initialize_file():
    """Create the CSV file with headers if it doesn't exist."""
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Category", "Description", "Amount"])


def add_expense():
    print("\n========== ADD EXPENSE ==========")

    date = input("Enter date (DD-MM-YYYY): ")
    category = input("Enter category: ").strip().title()
    description = input("Enter description: ").strip()

    while True:
        try:
            amount = float(input("Enter amount: "))

            if amount <= 0:
                print("❌ Amount must be greater than 0.")
                continue

            break

        except ValueError:
            print("❌ Please enter a valid amount.")

    with open(FILE_NAME, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([date, category, description, amount])

    print("✅ Expense added successfully!")


def view_expenses():
    print("\n========== ALL EXPENSES ==========")

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        expenses = list(reader)

        if not expenses:
            print("No expenses found.")
            return

        print("-" * 70)
        print(f"{'Date':<15}{'Category':<15}{'Description':<25}{'Amount':>10}")
        print("-" * 70)

        for expense in expenses:
            print(
                f"{expense['Date']:<15}"
                f"{expense['Category']:<15}"
                f"{expense['Description']:<25}"
                f"₹{float(expense['Amount']):>9.2f}"
            )

        print("-" * 70)


def filter_expenses():
    print("\n========== FILTER EXPENSES ==========")

    category = input("Enter category to filter: ").strip().title()

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        found = False

        print(f"\nExpenses in category: {category}")
        print("-" * 60)

        for expense in reader:
            if expense["Category"] == category:
                found = True

                print(
                    f"{expense['Date']} | "
                    f"{expense['Description']} | "
                    f"₹{float(expense['Amount']):.2f}"
                )

        if not found:
            print("No expenses found for this category.")


def category_summary():
    print("\n========== CATEGORY SUMMARY ==========")

    summary = {}

    with open(FILE_NAME, "r", newline="", encoding="utf-8") as file:
        reader = csv.DictReader(file)

        for expense in reader:
            category = expense["Category"]
            amount = float(expense["Amount"])

            if category in summary:
                summary[category] += amount
            else:
                summary[category] = amount

    if not summary:
        print("No expenses available.")
        return

    total = 0

    print("-" * 40)

    for category, amount in summary.items():
        print(f"{category:<20} ₹{amount:.2f}")
        total += amount

    print("-" * 40)
    print(f"{'Total':<20} ₹{total:.2f}")


def main():
    initialize_file()

    while True:
        print("\n====================================")
        print("       PERSONAL EXPENSE TRACKER")
        print("====================================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Filter by Category")
        print("4. Category Summary")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            filter_expenses()

        elif choice == "4":
            category_summary()

        elif choice == "5":
            print("👋 Thank you for using Expense Tracker!")
            break

        else:
            print("❌ Invalid choice. Please select 1-5.")


if __name__ == "__main__":
    main()