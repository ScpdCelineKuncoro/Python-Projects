from tkinter import *

root = Tk()

canvas = Canvas(width=300, height=200)
canvas.pack()

canvas.create_oval(50, 50, 200, 100, fill="purple", outline="blue", width=30)


root.mainloop()
 
