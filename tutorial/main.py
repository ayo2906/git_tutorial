import random
import tkinter

print("Welcome to the Personal Finance Tracker")

main_window = tkinter.Tk()
main_window.geometry("400x300")
main_window.title("Log-in page")

greeting = tkinter.Label(main_window, text="Welcome to our website", font=("calibri", 14))
greeting.grid(row = 0, column = 0)


greeting = tkinter.Label(main_window, text="Username", font=("calibri", 14))
greeting.grid(row = 1, column = 0)


greeting = tkinter.Label(main_window, text="Password", font=("calibri", 14))
greeting.grid(row = 2, column = 0)


user_entry = tkinter.Entry(main_window, font=("calibri", 14))
user_entry.grid(row= 1 , column= 1)

pass_entry = tkinter.Entry(main_window, font=("calibri", 14))
pass_entry.grid(row= 2 , column= 1)

def check_pass():
    if (user_entry.get() == "Ayo112") & (pass_entry.get() == "123456"):
        print("log in successful")
        main_window()
    else:
        print("Invalid username or password")
    


submit_btn = tkinter.Button(main_window, text="Submit", font=("calibri", 14))
submit_btn.grid(row= 3, column= 0)


def clear_all():
    user_entry.delete(0, "end")
    pass_entry.delete(0, tkinter.END)

clear_btn = tkinter.Button(main_window, text="Clear", font=("calibri", 14),command= clear_all)
clear_btn.grid(row= 3, column= 1)





main_window.mainloop()
