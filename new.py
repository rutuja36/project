
from tkinter import *
from tkinter import messagebox

tk = Tk()
tk.title("Login System")
tk.geometry("400x250")  # Corrected the typo in the geometry size
tk.resizable(False, False)
tk.configure(bg="white")                #blue

def login():
    username = entry1.get()
    password = entry2.get()

    if username == "" and password == "":
        messagebox.showerror("Error", "Blank not allowed")
    elif username == "":
        messagebox.showinfo("Error", "Please enter username")
    elif password == "":
        messagebox.showinfo("Error", "Please enter password")
    elif username == "ditiss" and password == "iacsd@123":
        messagebox.showinfo("Success", "Login successful")
    else:
        messagebox.showerror("Oops", "Invalid username/password")

# Label
Label(tk, text="welcome to iacsd", font="impact 20 bold", bg="black", fg="red").pack(fill=X)

Label(tk, text="Username").place(x=50, y=73)
Label(tk, text="Password").place(x=50, y=120)

# Entry
entry1 = Entry(tk, bd=4)
entry1.place(x=130, y=70)
entry2 = Entry(tk, bd=4, show="*")
entry2.place(x=130, y=120)

# Button
Button(tk, text="Login", bg="green", command=login).place(x=150, y=160)

tk.mainloop()

