from tkinter import *
root = Tk()

def button_clicked(event):
    print("Wow you are the best clicker i have ever seen")

def key_pressed(event):
    print("I see you typing lil bro")

root.bind("<Key>", key_pressed)


button1 = Button(root, text="Click me")
button1.bind("<Button-1>", button_clicked)
button1.pack()
root.mainloop()
