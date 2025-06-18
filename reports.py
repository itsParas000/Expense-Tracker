import sqlite3
import matplotlib.pyplot as plt

def plot_category_summary(month):
    conn = sqlite3.connect('db/expenses.db')
    c = conn.cursor()
    c.execute("SELECT category, SUM(amount) FROM expenses WHERE strftime('%Y-%m', date) = ? GROUP BY category", (month,))
    data = c.fetchall()
    conn.close()

    if not data:
        print("No data for this month.")
        return

    categories = [row[0] for row in data]
    amounts = [row[1] for row in data]

    plt.figure(figsize=(8, 5))
    plt.bar(categories, amounts, color='skyblue')
    plt.title(f"Expense Summary for {month}")
    plt.xlabel("Category")
    plt.ylabel("Total Spent (₹)")
    plt.tight_layout()
    plt.show()
