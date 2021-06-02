from tkinter import *

window = Tk()
window.config(bg="#111")
window.geometry("450x450")

list_lab = Label(window, bg="white", width=20, height=2)
list_lab.place(x=150, y=150)

list_lab2 =Label(window, bg="white", width=20, height=2, text="42, 12, 13, 89, 63, 11")
list_lab2.place(x=150, y=100)


def dort():
    Numbers = [42, 12, 13, 89, 63, 11]
    for y in range(0, 6):
        for x in range(0, 5):
            if Numbers[x] > Numbers[x + 1]:
                swap = Numbers[x]
                Numbers[x] = Numbers[x + 1]
                Numbers[x + 1] = Numbers[x]
                Numbers[x + 1] = swap
                list_lab.config(text=Numbers)


list_btn = Button(window, text="Sort", command=dort, bg="red")
list_btn.place(x=150, y=200)


def clear():
    list_lab.config(text="")


clear_btn = Button(text="Clear", bg="red", command=clear)
clear_btn.place(x=250, y=200)

window.mainloop()
