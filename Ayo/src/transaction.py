import tkinter as tk
from tkinter import messagebox

# Define data structures
transactions = []  # List to store transactions (dictionaries)
user_balance = 0

def add_transaction(root, update_categories, balance_label, transactions_listbox):
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
        update_balance_label(balance_label)
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
    type_menu = tk.OptionMenu(
        add_window,
        transaction_type,
        "Income",
        "Expense",
        command=lambda event=None: update_categories(category_var, transaction_type.get(), category_menu)
    )
    type_menu.pack()

    tk.Label(
        add_window, text="Category:"
    ).pack()
    category_menu = tk.OptionMenu(
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

def delete_transaction(root, balance_label, transactions_listbox):
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
            update_balance_label(balance_label)
            update_transaction_list(transactions_listbox=transactions_listbox)
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

def update_transaction_list(transactions_listbox):
    transactions_listbox.delete(0, tk.END)
    for transaction in transactions:
        transactions_listbox.insert(tk.END, f"ID: {transaction['id']}, Type: {transaction['type']}, Category: {transaction['category']}, "
                                             f"Amount: {transaction['amount']}, Date: {transaction['date']}, Payee: {transaction['payee']}")

def update_balance_label(balance_label):
    global user_balance
    balance_label.config(text=f"Balance: ${user_balance:.2f}")
