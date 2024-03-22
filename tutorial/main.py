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
#notebook.add(text= "Main") (new tab to be cretated for account details and balance)

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

#class PersonalFinanceTracker:
#    def __init__(self, root):
 #       self.root = root
  #      self.root.title("Personal Finance Tracker")
   #     self.username = self.prompt_user_name()
    #    self.account_balance = 0.00
     #   self.transactions = []

  #      # Main window setup
 #       self.setup_main_window()

   # def prompt_user_name(self):
  #      # This method will prompt for the user's name. Implement as needed.
 #       return "User"

    #def setup_main_window(self):
   #     # Display a personalized greeting
  #      greeting_label = tkinter.Label(self.root, text=f"Welcome, {self.username}!")
 #       greeting_label.pack()

   #     # Display the current account balance
  #      balance_label = tkinter.Label(self.root, text=f"Current Balance: ${self.account_balance:,.2f}")
 #       balance_label.pack()

   #     # Placeholder for last transaction summary
  #      self.last_transaction_label = tkinter.Label(self.root, text="Last Transaction: None")
 #       self.last_transaction_label.pack()

   #     # Add transaction management buttons
  #      add_transaction_button = tkinter.Button(self.root, text="Add Transaction", command=self.add_transaction)
 #       add_transaction_button.pack()

 #       summary_button = tkinter.Button(self.root, text="Summary", command=self.show_summary)
    #    summary_button.pack()

  #      delete_transaction_button = tkinter.Button(self.root, text="Delete Transaction", command=self.delete_transaction)
 #       delete_transaction_button.pack()

    #    
   # def add_transaction(self):
  #      # Placeholder for add transaction functionality
 #       pass

   # def show_summary(self):
  #      # Placeholder for showing transaction summary
 #       pass

  #  def delete_transaction(self):
 #       # Placeholder for delete transaction functionality
#        pass

# Main application execution
#if __name__ == "__main__":
#    root = tkinter.Tk()
#    app = PersonalFinanceTracker(root)
#    root.mainloop()

def main_page_setup():
    main_page = ttk.Frame(notebook, width=1200, height=720)
    notebook.add(main_page, text="Main")

    add_transaction_btn = tkinter.Button(main_page, text="Add transaction", font=('calibri', 14), command=add_transaction_window)
    add_transaction_btn.pack()

    summary_btn = tkinter.Button(main_page, text="Summary", font=('calibri',14),command=show_summary_window)
    summary_btn.pack()


def add_transaction_window():
    add_transactin_window = tkinter.Toplevel(main_window)
    add_transactin_window.geometry("300x200")
    add_transactin_window.title("Add Transaction")

def show_summary_window():
    summary_window = tkinter.Toplevel(main_window)
    summary_window.geometry("400x300")
    summary_window.title("Summary")



def add_trans():

    temp_window = tkinter.Tk()
    temp_window.title("Adding new transaction")

    type_label = tkinter.Label(temp_window, text="Type", font=('calibri',14))
    type_label.grid(row= 0, column= 0 )

    type_entry = tkinter.Entry(temp_window)
    type_label.grid(row= 0, column= 1 )

    amount_label = tkinter.Label(temp_window, text="Amount", font=('calibri',14))
    amount_label.grid(row= 1, column= 0 )

    amount_entry = tkinter.Entry(temp_window)
    amount_label.grid(row= 1, column= 1 )

    submit_btn = tkinter.Button(temp_window,text="Submit transaction", font=('calibri', 14))
    submit_btn.grid(row=2, column=0)


def check_pass():
    if (user_entry.get() == "Ayo112") & (pass_entry.get() == "123456"):
        print("log in successful")
        main_page_setup()
        
        
        
    else:
        print("Invalid username or password")
    


submit_btn = tkinter.Button(greeting_page, text="Submit", font=("calibri", 14) , command=check_pass)
submit_btn.grid(row= 3, column= 0)


def clear_all():
    user_entry.delete(0, "end")
    pass_entry.delete(0, tkinter.END)



clear_btn = tkinter.Button(greeting_page, text="Clear", font=("calibri", 14),command= clear_all)
clear_btn.grid(row= 4, column= 0)




add_transaction_btn = tkinter.Button(add_transaction_window, text="Add new transaction", font=('calibri',14), command=add_trans)
add_transaction_btn.pack(pady=4)


main_window.mainloop()
