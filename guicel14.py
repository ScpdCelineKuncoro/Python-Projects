from tkinter import *
from tkinter import messagebox
root = Tk()

def error_message():
    messagebox.showinfo("This is an error")

button1 = Button(root, text="Do not click", command=error_message)
button1.pack()

root.mainloop()
