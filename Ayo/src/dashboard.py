# import tkinter as tk
# from tkinter import messagebox
# import matplotlib.pyplot as plt

# def show_dashboard():
#     def generate_summary():
#         incomes = {}
#         expenses = {}
#         for transaction in transactions:
#             if transaction["type"] == "Income":
#                 incomes[transaction["category"]] = incomes.get(transaction["category"], 0) + transaction["amount"]
#             else:
#                 expenses[transaction["category"]] = expenses.get(transaction["category"], 0) + transaction["amount"]

#         plt.figure(figsize=(8, 6))

#         plt.subplot(1, 2, 1)
#         plt.barh(list(incomes.keys()), list(incomes.values()), color='skyblue')
#         plt.xlabel('Amount')
#         plt.title('Income Summary')

#         plt.subplot(1, 2, 2)
#         plt.pie(list(expenses.values()), labels=list(expenses.keys()), autopct='%1.1f%%', startangle=140)
#         plt.title('Expense Summary')

#         plt.tight_layout()
#         plt.show()

#     def export_to_txt():
#         with open("transaction_summary.txt", "w") as file:
#             for transaction in transactions:
#                 file.write(f"ID: {transaction['id']}, Type: {transaction['type']}, Category: {transaction['category']}, "
#                            f"Amount: {transaction['amount']}, Date: {transaction['date']}, Payee: {transaction['payee']}\n")

#     dashboard_window = tk.Toplevel(root)
#     dashboard_window.title("Dashboard")

#     generate_summary_button = tk.Button(dashboard_window, text="Generate Summary", command=generate_summary)
#     generate_summary_button.pack()

#     export_button = tk.Button(dashboard_window, text="Export to Text", command=export_to_txt)
#     export_button.pack()

import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import messagebox
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from transaction import transactions

def show_dashboard(root, balance_label):
    def generate_summary():
        incomes = {}
        expenses = {}
        for transaction in transactions:
            if transaction["type"] == "Income":
                incomes[transaction["category"]] = incomes.get(transaction["category"], 0) + transaction["amount"]
            else:
                expenses[transaction["category"]] = expenses.get(transaction["category"], 0) + transaction["amount"]

        # Create figure and subplots
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

        # Plot income summary
        ax1.barh(list(incomes.keys()), list(incomes.values()), color='skyblue')
        ax1.set_xlabel('Amount')
        ax1.set_title('Income Summary')

        # Plot expense summary
        ax2.pie(list(expenses.values()), labels=list(expenses.keys()), autopct='%1.1f%%', startangle=140)
        ax2.set_title('Expense Summary')

        # Adjust layout
        plt.tight_layout()

        # Display the plot in a Tkinter window
        canvas = FigureCanvasTkAgg(fig, master=root)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def export_to_txt():
        with open("../data/transaction_summary.txt", "w") as file:
            for transaction in transactions:
                file.write(f"ID: {transaction['id']}, Type: {transaction['type']}, Category: {transaction['category']}, "
                           f"Amount: {transaction['amount']}, Date: {transaction['date']}, Payee: {transaction['payee']}\n")

    # Create dashboard window
    dashboard_window = tk.Toplevel(root)
    dashboard_window.title("Dashboard")

    # Generate summary button
    generate_summary_button = tk.Button(dashboard_window, text="Generate Summary", command=generate_summary)
    generate_summary_button.pack()

    # Export to text button
    export_button = tk.Button(dashboard_window, text="Export to Text", command=export_to_txt)
    export_button.pack()

