import tkinter as tk
from tkinter.simpledialog import askstring
from transaction import add_transaction, delete_transaction, update_balance_label, update_transaction_list
from dashboard import show_dashboard

def get_username_and_open_window():
    global root
    global user_balance
    global balance_label
    global transactions_listbox  # Define transactions_listbox globally
    
    def update_categories(category_var, transaction_type, category_menu):
        income_categories = ["Salary", "Pension", "Interest", "Others"]
        expense_categories = ["Food", "Rent", "Clothing", "Car", "Health", "Others"]
        categories = income_categories if transaction_type == "Income" else expense_categories
        category_var.set(categories[0])  # Set default category
        menu = category_menu['menu']
        menu.delete(0, 'end')
        for category in categories:
            menu.add_command(label=category, command=lambda cat=category: category_var.set(cat))
    
    username = askstring("Username", "Please enter your username:")
    if username:
        root = tk.Tk()
        root.title("Personal Finance Tracker")
        root.geometry("800x600")
        balance_label = tk.Label(root, text="Balance: $0.00")
        balance_label.pack()
        update_balance_label(balance_label)
        tk.messagebox.showinfo("Welcome", f"Welcome, {username}!")
        
        # Create transactions_listbox
        transactions_listbox = tk.Listbox(root)
        #transactions_listbox.pack()

        add_transaction_button = tk.Button(root, text="Add Transaction", command=lambda: add_transaction(root, update_categories, balance_label, transactions_listbox))
        add_transaction_button.pack()

        show_dashboard_button = tk.Button(root, text="Show Dashboard", command=lambda: show_dashboard(root, balance_label))  # Pass root and balance_label
        show_dashboard_button.pack()

        delete_transaction_button = tk.Button(root, text="Delete Transaction", command=lambda: delete_transaction(root, balance_label, transactions_listbox))
        delete_transaction_button.pack()

        # Start the GUI event loop
        root.mainloop()

# Prompt for username and open main window
get_username_and_open_window()




