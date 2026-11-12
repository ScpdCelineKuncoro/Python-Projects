from tkinter import *
root = Tk()
left_counter = 0
right_counter = 0

def left_click(event):
    global left_counter
    left_counter += 1
    left_label.config(text=left_counter)

def right_click(event):
    global right_counter
    right_counter += 1
    right_label.config(text=right_counter)

left_label = Label(root, text="left click: {}".format(left_counter))
right_label = Label(root, text="right click: {}".format(right_counter))

left_button = Button(root, text="I'm left")
right_button = Button(root, text="I'm right")

left_button.bind("<Button-1>", left_click)
right_button.bind("<Button-2>", right_click)


left_label.pack()
right_label.pack()

left_button.pack()
right_button.pack()


root.mainloop()
