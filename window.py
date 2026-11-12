from tkinter import *
root = Tk()

def button():
    button1.config(text="Was clicked")

button1 = Button(root, text="Click me", command=button, fg="black", bg="green")
button1.pack() 

root.mainloop()
