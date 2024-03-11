import random
import tkinter
from tkinter import messagebox , ttk

print("Welcome to the Personal Finance Tracker")

main_window = tkinter.Tk()
main_window.geometry("400x300")
main_window.title("Log-in page")
notebook = ttk.Notebook(main_window)
notebook.pack(pady=5, expand= True, fill= "both")
greeting_page=ttk.Frame(notebook, width=1200, height=720)
notebook.add(greeting_page, text= "Home")

greeting = tkinter.Label(greeting_page, text="Welcome to our website", font=("calibri", 14))
greeting.grid(row = 0, column = 0)


greeting = tkinter.Label(greeting_page, text="Username", font=("calibri", 14))
greeting.grid(row = 1, column = 0)


greeting = tkinter.Label(greeting_page, text="Password", font=("calibri", 14))
greeting.grid(row = 2, column = 0)


user_entry = tkinter.Entry(greeting_page, font=("calibri", 14))
user_entry.grid(row= 1 , column= 1)

pass_entry = tkinter.Entry(greeting_page, font=("calibri", 14))
pass_entry.grid(row= 2 , column= 1)

class PersonalFinanceTracker:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Tracker")
        self.username = self.prompt_user_name()
        self.account_balance = 0.00
        self.transactions = []

  #      # Main window setup
 #       self.setup_main_window()

   # def prompt_user_name(self):
  #      # This method will prompt for the user's name. Implement as needed.
 #       return "User"
#
    #def setup_main_window(self):
   #     # Display a personalized greeting
  #      greeting_label = tkinter.Label(self.root, text=f"Welcome, {self.username}!")
 #       greeting_label.pack()
#
   #     # Display the current account balance
  #      balance_label = tkinter.Label(self.root, text=f"Current Balance: ${self.account_balance:,.2f}")
 #       balance_label.pack()
#
   #     # Placeholder for last transaction summary
  #      self.last_transaction_label = tkinter.Label(self.root, text="Last Transaction: None")
 #       self.last_transaction_label.pack()
#
   #     # Add transaction management buttons
  #      add_transaction_button = tkinter.Button(self.root, text="Add Transaction", command=self.add_transaction)
 #       add_transaction_button.pack()
#
 #       summary_button = tkinter.Button(self.root, text="Summary", command=self.show_summary)
    #    summary_button.pack()
#
  #      delete_transaction_button = tkinter.Button(self.root, text="Delete Transaction", command=self.delete_transaction)
 #       delete_transaction_button.pack()
#
    #    
   # def add_transaction(self):
  #      # Placeholder for add transaction functionality
 #       pass
#
   # def show_summary(self):
  #      # Placeholder for showing transaction summary
 #       pass
#
  #  def delete_transaction(self):
 #       # Placeholder for delete transaction functionality
#        pass

# Main application execution
#if __name__ == "__main__":
#    root = tkinter.Tk()
#    app = PersonalFinanceTracker(root)
#    root.mainloop()


def check_pass():
    if (user_entry.get() == "Ayo112") & (pass_entry.get() == "123456"):
        print("log in successful")
        greeting_page()
    else:
        print("Invalid username or password")
    


submit_btn = tkinter.Button(greeting_page, text="Submit", font=("calibri", 14) , command=check_pass)
submit_btn.grid(row= 3, column= 0)


def clear_all():
    user_entry.delete(0, "end")
    pass_entry.delete(0, tkinter.END)

clear_btn = tkinter.Button(greeting_page, text="Clear", font=("calibri", 14),command= clear_all)
clear_btn.grid(row= 3, column= 1)





main_window.mainloop()
