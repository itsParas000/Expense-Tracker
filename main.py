from db_utils import create_db, add_expense, view_expenses, filter_by_month
from reports import plot_category_summary

def show_menu():
    print("\n Expense Tracker")
    print("1. Add Expense")
    print("2. View All Expenses")
    print("3. View Monthly Summary")
    print("4. Plot Category Chart")
    print("5. Exit")

def main():
    create_db()
    while True:
        show_menu()
        choice = input("Enter choice (1-5): ")

        if choice == '1':
            amount = float(input("Amount: ₹"))
            category = input("Category (food, travel, etc.): ")
            note = input("Note (optional): ")
            date = input("Date (YYYY-MM-DD): ")
            add_expense(amount, category, note, date)

        elif choice == '2':
            view_expenses()

        elif choice == '3':
            month = input("Enter month (YYYY-MM): ")
            filter_by_month(month)

        elif choice == '4':
            month = input("Enter month (YYYY-MM): ")
            plot_category_summary(month)

        elif choice == '5':
            print(" Exiting. Goodbye!")
            break

        else:
            print(" Invalid choice. Try again.")

if __name__ == "__main__":
    main()
