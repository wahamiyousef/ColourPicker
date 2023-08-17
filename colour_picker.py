from tkinter import *
from tkinter import colorchooser

root = Tk()
root.title("Colours")
root.geometry("300x400")
#root.iconbitmap('')

def color():
    my_color = colorchooser.askcolor()
    my_label = Label(root, text=my_color).pack(pady=10)

my_button = Button(root, text="Pick A Colour", command=color).pack()

root.mainloop()