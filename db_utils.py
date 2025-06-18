import sqlite3

def create_db():
    conn = sqlite3.connect('db/expenses.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        amount REAL,
        category TEXT,
        note TEXT,
        date TEXT
    )''')
    conn.commit()
    conn.close()

def add_expense(amount, category, note, date):
    conn = sqlite3.connect('db/expenses.db')
    c = conn.cursor()
    c.execute("INSERT INTO expenses (amount, category, note, date) VALUES (?, ?, ?, ?)",
              (amount, category, note, date))
    conn.commit()
    conn.close()
    print("Expense added.")

def view_expenses():
    conn = sqlite3.connect('db/expenses.db')
    c = conn.cursor()
    c.execute("SELECT * FROM expenses")
    rows = c.fetchall()
    print("\n All Expenses:")
    for row in rows:
        print(row)
    conn.close()

def filter_by_month(month):
    conn = sqlite3.connect('db/expenses.db')
    c = conn.cursor()
    c.execute("SELECT * FROM expenses WHERE strftime('%Y-%m', date) = ?", (month,))
    rows = c.fetchall()
    print(f"\n Expenses for {month}:")
    for row in rows:
        print(row)
    conn.close()
