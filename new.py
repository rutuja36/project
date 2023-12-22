
from tkinter import *
from tkinter import messagebox

tk = Tk()
tk.title("Login System")
tk.geometry("400x250")  # Corrected the typo in the geometry size
tk.resizable(False, False)
<<<<<<< HEAD
tk.configure(bg="white")                #blue

def login():
=======
tk.configure(bg="cadetblue")                #blue

# for database
def login_data():
    import mysql.connector

    mydb = mysql.connector.connect(host='localhost',port=3306,user='root',password='Admin@123',database='login_db')

    mycursor = mydb.cursor()

    username = entry1.get()
    password = entry2.get()


    mycursor.execute("insert into login values (%s,%s)",(username,password))
    mydb.commit()

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


def login():
    '''
>>>>>>> 4fdf8c5 (new1)
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
<<<<<<< HEAD

=======
    '''
>>>>>>> 4fdf8c5 (new1)
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
<<<<<<< HEAD
Button(tk, text="Login", bg="green", command=login).place(x=150, y=160)
=======
Button(tk, text="Login", bg="green", command=login_data).place(x=150, y=160)
>>>>>>> 4fdf8c5 (new1)

tk.mainloop()

