import tkinter
import random

balance = 0
#transaction = []
transaction = [{"ID": "1234", "type": "income", "category": "salary", "amount": 23000, "date": "2-April"}]

main_window = tkinter.Tk()
main_window.title("Personal Finance Tracker")
main_window.geometry("800x600")

name_label = tkinter.Label(main_window,text="" , font=('calibri', 14))
name_label.pack(pady=5)

money_label = tkinter.Label(main_window, text= "Balance: "+ str(balance), font=('calibri', 14))
money_label.pack(pady=2)


def organise_trans():
    out = ""
    for item in transaction:
        out += str(item)
        out += "\n"

    return out

def get_name():
    name_label.config(text="Hello " + name_entry.get() + ", Welcome to your PFT")
    name_w.destroy()

    
def see_transactions():
    trans_window = tkinter.Tk()
    trans_window.title("List of transactions")

    trans_label = tkinter.Label(trans_window, text=organise_trans(), font=('calibri',14))
    trans_label.pack()



see_trans = tkinter.Button(main_window, text="See transactions", font=('calibri',14), command=see_transactions)
see_trans.pack(pady=2)

name_w = tkinter.Tk()
name_w.title("Log-In Page")
name_w.geometry("400x150")

name_entry = tkinter.Entry(name_w)
name_entry.pack(pady=10)

#def check_pass():
 #   if (name_entry.get() == "Ayo"):
  #      print("Successful Log-In")
        



submit_btn = tkinter.Button(name_w, text="Submit", font=('calibri', 14), command=get_name)
submit_btn.pack(pady=5)


def submit_trans(type_entry, amount_entry, category_entry):
    trans_ID = random.randint(0,100)
    trans_type = type_entry.get()
    trans_amount = amount_entry.get()
    trans_category = category_entry.get()
    trans_date = "1-January"

    transaction.append({"ID": str(trans_ID), "type": trans_type,
                        "category": trans_category, "amount": float(trans_amount), "data": trans_date})
    

def add_trans():

    temp_window = tkinter.Tk()
    temp_window.title("Adding new transaction")

    type_label = tkinter.Label(temp_window, text="Type", font=('calibri',14))
    type_label.grid(row=0, column=0)

    type_entry = tkinter.Entry(temp_window)
    type_entry.grid(row=0, column=1)

    amount_label = tkinter.Label(temp_window, text="Amount", font=('calibri',14))
    amount_label.grid(row=1, column=0)

    amount_entry = tkinter.Entry(temp_window)
    amount_entry.grid(row=1, column=1)

    category_label = tkinter.Label(temp_window, text="Category", font=('calibri',14))
    category_label.grid(row=2, column=0)

    category_entry = tkinter.Entry(temp_window)
    category_entry.grid(row=2, column=1)


    date_label = tkinter.Label(temp_window,text="Data (12-January)", font=('calibri',14))
    date_label.grid(row = 3, column= 0)

    date_entry = tkinter.Entry(temp_window)
    date_entry.grid(row=3, column=1)

    submit_btn = tkinter.Button(temp_window, text="Submit Transaction", font=('calibri',14),
                                command= lambda: submit_trans(type_entry, amount_entry, category_entry))
    submit_btn.grid(row=4, column=0)



add_trans_btn = tkinter.Button(main_window, text="Add new transaction", font=('calibri',14), command=add_trans)
add_trans_btn.pack(pady=4)


main_window.mainloop()
