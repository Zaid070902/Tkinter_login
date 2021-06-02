from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("500x200")
root.config(bg="#111")

name_lab = Label(root, text="Username:", fg="white", bg="#111")
name_lab.place(x=10, y=10)

name_entry = Entry(root)
name_entry.place(x=100, y=10)

code_lab = Label(text="Password:", bg="#111", fg="white")
code_lab.place(x=10, y=50)

code_entry = Entry(root)
code_entry.place(x=100, y=50)

Username = ["Cassiem", "Gary", "Zaid", "Aaliyah", "Uthmaan"]
Password = ["666", "777", "999", "888", "333"]


def log():
    found = False
    for x in range(len(Username)):
        if name_entry.get() == Username[x] and code_entry.get() == Password[x]:
            found = True
    if found == True:
        messagebox.showinfo("STATUS", "Access granted")
    else:
        messagebox.showinfo("STATUS", "Access denied")

    import Next


button = Button(root, text="Login", command=log, bg="cyan")
button.place(x=100, y=100)


def clear():
    code_entry.delete(0, END)
    name_entry.delete(0, END)


clear = Button(root, text="Clear", bg="cyan", command=clear)
clear.place(x=200, y=100)


def destroy():
    return root.destroy()


exit_btn = Button(root, text="Exit", command=destroy)
exit_btn.place(x=150, y=150)

root.mainloop()
