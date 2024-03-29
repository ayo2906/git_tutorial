import tkinter as tk
from tkinter import OptionMenu, messagebox, ttk
from tkinter.simpledialog import askstring
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# Define data structures
transactions = []  # List to store transactions (dictionaries)
user_balance = 0
balance_label = None  # Define balance_label here

def add_transaction():
    def update_categories():
        category_menu['menu'].delete(0, 'end')
        categories = income_categories if transaction_type.get() == "Income" else expense_categories
        for category in categories:
            category_menu['menu'].add_command(label=category, command=tk._setit(category_var, category))

    def save_transaction():
        global user_balance
        transaction_data = {
            "id": len(transactions) + 1,
            "type": transaction_type.get(),
            "category": category_var.get(),
            "amount": float(amount_var.get()),
            "date": date_var.get(),
            "payee": payee_var.get(),
        }
        transactions.append(transaction_data)
        if transaction_data["type"] == "Income":
            user_balance += transaction_data["amount"]
        else:
            user_balance -= transaction_data["amount"]
        messagebox.showinfo("Success", "Transaction added successfully!")
        update_balance_label()
        add_window.destroy()

    add_window = tk.Toplevel(root)
    add_window.title("Add Transaction")

    transaction_type = tk.StringVar(value="Income")
    income_categories = ["Salary", "Pension", "Interest", "Others"]
    expense_categories = ["Food", "Rent", "Clothing", "Car", "Health", "Others"]
    category_var = tk.StringVar()

    tk.Label(
        add_window, text="Transaction Type:"
    ).pack()
    type_menu = OptionMenu(
        add_window,
        transaction_type,
        "Income",
        "Expense",
        command=lambda event=None: update_categories()
    )
    type_menu.pack()

    tk.Label(
        add_window, text="Category:"
    ).pack()
    category_menu = OptionMenu(
        add_window,
        category_var,
        *income_categories
    )
    category_menu.pack()

    amount_var = tk.StringVar()
    tk.Label(
        add_window, text="Amount:"
    ).pack()
    tk.Entry(add_window, textvariable=amount_var).pack()

    date_var = tk.StringVar()
    tk.Label(
        add_window, text="Date (YYYY-MM-DD):"
    ).pack()
    tk.Entry(add_window, textvariable=date_var).pack()

    payee_var = tk.StringVar()
    tk.Label(
        add_window, text="Payee (Expense) / Source (Income):"
    ).pack()
    tk.Entry(add_window, textvariable=payee_var).pack()

    tk.Button(
        add_window, text="Save", command=save_transaction
    ).pack()

def update_balance_label():
    global balance_label
    balance_label.config(text=f"Balance: ${user_balance:.2f}")

def show_dashboard():
    def generate_summary():
        incomes = {}
        expenses = {}
        for transaction in transactions:
            if transaction["type"] == "Income":
                incomes[transaction["category"]] = incomes.get(transaction["category"], 0) + transaction["amount"]
            else:
                expenses[transaction["category"]] = expenses.get(transaction["category"], 0) + transaction["amount"]

        plt.figure(figsize=(8, 6))

        plt.subplot(1, 2, 1)
        plt.barh(list(incomes.keys()), list(incomes.values()), color='skyblue')
        plt.xlabel('Amount')
        plt.title('Income Summary')

        plt.subplot(1, 2, 2)
        plt.pie(list(expenses.values()), labels=list(expenses.keys()), autopct='%1.1f%%', startangle=140)
        plt.title('Expense Summary')

        plt.tight_layout()
        plt.show()

    def export_to_txt():
        with open("transaction_summary.txt", "w") as file:
            for transaction in transactions:
                file.write(f"ID: {transaction['id']}, Type: {transaction['type']}, Category: {transaction['category']}, "
                           f"Amount: {transaction['amount']}, Date: {transaction['date']}, Payee: {transaction['payee']}\n")

    dashboard_window = tk.Toplevel(root)
    dashboard_window.title("Dashboard")

    generate_summary_button = tk.Button(dashboard_window, text="Generate Summary", command=generate_summary)
    generate_summary_button.pack()

    export_button = tk.Button(dashboard_window, text="Export to Text", command=export_to_txt)
    export_button.pack()

def delete_transaction():
    def delete_selected():
        global user_balance
        selection = transactions_listbox.curselection()
        if selection:
            idx = selection[0]
            transaction = transactions[idx]
            if transaction["type"] == "Income":
                user_balance -= transaction["amount"]
            else:
                user_balance += transaction["amount"]
            transactions.pop(idx)
            update_balance_label()
            update_transaction_list()
            messagebox.showinfo("Success", "Transaction deleted successfully!")
        else:
            messagebox.showwarning("Warning", "Please select a transaction to delete.")

    delete_window = tk.Toplevel(root)
    delete_window.title("Delete Transaction")

    transactions_listbox = tk.Listbox(delete_window, selectmode=tk.SINGLE)
    transactions_listbox.pack()

    for transaction in transactions:
        transactions_listbox.insert(tk.END, f"ID: {transaction['id']}, Type: {transaction['type']}, Category: {transaction['category']}, "
                                             f"Amount: {transaction['amount']}, Date: {transaction['date']}, Payee: {transaction['payee']}")

    delete_button = tk.Button(delete_window, text="Delete Selected", command=delete_selected)
    delete_button.pack()

def update_transaction_list():
    transactions_listbox.delete(0, tk.END)
    for transaction in transactions:
        transactions_listbox.insert(tk.END, f"ID: {transaction['id']}, Type: {transaction['type']}, Category: {transaction['category']}, "
                                             f"Amount: {transaction['amount']}, Date: {transaction['date']}, Payee: {transaction['payee']}")

def get_username_and_open_window():
    global root
    global user_balance
    global balance_label
    username = askstring("Username", "Please enter your username:")
    if username:
        root = tk.Tk()
        root.title("Personal Finance Tracker")
        root.geometry("800x600")
        balance_label = tk.Label(root, text="Balance: $0.00")
        balance_label.pack()
        update_balance_label()
        messagebox.showinfo("Welcome", f"Welcome, {username}!")

        add_transaction_button = tk.Button(root, text="Add Transaction", command=add_transaction)
        add_transaction_button.pack()

        show_dashboard_button = tk.Button(root, text="Show Dashboard", command=show_dashboard)
        show_dashboard_button.pack()

        delete_transaction_button = tk.Button(root, text="Delete Transaction", command=delete_transaction)
        delete_transaction_button.pack()

        # Start the GUI event loop
        root.mainloop()

# Prompt for username and open main window
get_username_and_open_window()
