from tkinter import *
root = Tk()

def paint_func(event):
    canvas.create_oval(event.x, event.y, event.x+1, event.y+1)

welcome = Label(root, text="Click and hold the left button and drag to draw", fg="brown", bg="white")
welcome.pack()
canvas = Canvas(root, width=200, height=200)
canvas.bind("<B1-Motion>", paint_func)
canvas.pack()

root.mainloop()
