from tkinter import *

root = Tk()

canvas = Canvas(width=300, height=200)
canvas.pack()

canvas.add_ine(0, 100, 300, 200, fill="red")

root.mainloop()
