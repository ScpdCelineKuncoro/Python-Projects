from tkinter import *
root = Tk()

def foo(event):
    print("working just fine")

root.bind("<Enter>", foo)



root.mainloop()
