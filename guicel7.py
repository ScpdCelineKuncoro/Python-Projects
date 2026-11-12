from tkinter import *
root = Tk()

def left_click(event):
    print("You have clicked, weel done ig")

def right_click(event):
    print("Wowwwwwwww so amazing click")

right_button = Button(root, text="I'm right", command=right_click)
left_button = Button(root, text="Im left", command=left_click)


left_button.bind("<Button-1>", left_click)
right_button.bind("<Button-3>", right_click)

left_button.pack()
right_button.pack()

root.mainloop()
