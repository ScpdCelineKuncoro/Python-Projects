from tkinter import *
root = Tk()

def left_click(event):
    print("You have left clicked, well done!")

def right_click(event):
    print("You have right clicked, well done!")


left_button = Button(root, text="Im left")
right_button = Button(root, text="Im right")

left_button.bind("<Button-1>", left_click)
right_button.bind("<Button-1>", right_click)

left_button.pack()
right_button.pack()


root.mainloop()
