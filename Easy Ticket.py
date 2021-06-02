from tkinter import *
from tkinter import ttk


root = Tk()
root.title("TicketSales")
root.geometry("400x450")
root.config(bg="#111")


class Tickets:
    amount_ans = StringVar()
    category_ans = StringVar()
    ticket_amount = StringVar()
    Contact = StringVar()

    socer = 40.00
    film = 75.00
    theeter = 100.00

    def __init__(self):
        self.cellphone_lab = Label(root, text="Enter CellNumber:")
        self.cellphone_lab.place(x=10, y=10)

        self.cellphone_entry = Entry(root, width=20)
        self.cellphone_entry.place(x=150, y=10)

        self.Category_lab = Label(root, text="Select Ticket Category:")
        self.Category_lab.place(x=10, y=50)

        self.n = StringVar
        self.comboBox = ttk.Combobox(root, textvariable=self.n)
        self.comboBox['values'] = ('Soccer', 'Movies', 'Theatre')
        self.comboBox.place(x=180, y=50)

        self.Ticket_number = Label(root, text="Number of Tickets Bought")
        self.Ticket_number.place(x=10, y=100)

        self.Ticket_spinbox = Spinbox(root, from_=0, to=10, width=3, textvariable=self.ticket_amount)
        self.Ticket_spinbox.place(x=200, y=100)

        self.Calculate_btn = Button(root, text="Calculate Ticket", command=self.calculate)
        self.Calculate_btn.place(x=10, y=150)

        self.Clear_btn = Button(root, text="Clear Entries", command=self.clear)
        self.Clear_btn.place(x=150, y=150)

        self.X_lab = Label(root, text="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", bg="#111", fg="white")
        self.X_lab.place(x=10, y=200)

        self.Amount_lab = Label(root, text="Amount Payable:")
        self.Amount_lab.place(x=10, y=250)

        self.Amount = Label(root, width=10, height=1, textvariable=self.amount_ans)
        self.Amount.place(x=150, y=250)

        self.Answer_lab = Label(root, width=10, height=1, textvariable=self.category_ans)
        self.Answer_lab.place(x=100, y=300)

        self.Res_lab = Label(root, text="Reservation for")
        self.Res_lab.place(x=10, y=300)

        self.X_lab = Label(root, text="xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", bg="#111", fg="white" )
        self.X_lab.place(x=10, y=400)

        self.for_lab = Label(root, text="for")
        self.for_lab.place(x=180, y=300)

        self.num_lab = Label(root, width=5, height=1, textvariable=self.ticket_amount)
        self.num_lab.place(x=200, y=300)

        self.was_lab = Label(root, text="was done by")
        self.was_lab.place(x=10, y=330)

        self.cell_lab = Label(root, width=20, height=1, textvariable=self.Contact)
        self.cell_lab.place(x=100, y=330)

    def clear(self):
        self.cellphone_entry.delete(0, END)
        self.comboBox.delete(0, END)

    def calculate(self):
        if self.comboBox.get() == "Soccer":
            result = float(self.Ticket_spinbox.get()) * 40.00 + (0.14*40)
            self.amount_ans.set(round(result))
        elif self.comboBox.get() == "Movies":
            result = float(self.Ticket_spinbox.get()) * 75.00 + (0.14*75)
            self.amount_ans.set(round(result))
        elif self.comboBox.get() == "Theatre":
            result = float(self.Ticket_spinbox.get()) * 100.00 + (0.14*100)
            self.amount_ans.set(round(result))

        self.category()
        self.num_tickets()
        self.who()

    def category(self):
        if self.comboBox.get() == "Soccer":
            result = (self.comboBox.get())
            self.category_ans.set(result)
        elif self.comboBox.get() == "Movies":
            result = (self.comboBox.get())
            self.category_ans.set(result)
        elif self.comboBox.get() == "Theatre":
            result = (self.comboBox.get())
            self.category_ans.set(result)

    def num_tickets(self):
        result = self.Ticket_spinbox.get()
        self.ticket_amount.set(result)

    def who(self):
        result = self.cellphone_entry.get()
        self.Contact.set(result)


Tickets = Tickets()
root.mainloop()
