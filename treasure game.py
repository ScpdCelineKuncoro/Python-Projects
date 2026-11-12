from tkinter import *
import random

root = Tk()

root.title("Yar or Nar")

x_coord = random.randint(0, 200)
y_coord = random.randint(0, 200)
button_counter = 1
counter = 0

def guess(event):
    global counter
    counter += 1
    if counter >= 10:
        global button_counter
        if button_counter == 1:
            button1 = Button(root, text = "Use parrot")
            button1.bind("<Button-1>", parrot)
            button1.pack()
    
    print("You clicked at x:{} y:{}. You are {}away from x and {} fron y"
         .format(event.x, event.y, abs(event.x-x_coord), abs(event.y-y_coord)))
    if abs(event.x-x_coord) < 5 and abs(event.y-y_coord) <5:
        print("YOU FOUND THE TR3A5UR3")
        welcome_label.config(text="You have won! Guesses: ()".format(counter))

def parrot(event):
    print("Parrot search")
    global button_counter
    button_counter -= 1
    print("You clicked at x:{} y:{}. You are {}away from x and {} fron y"
        .format(event.x, event.y, abs(event.x-x_coord), abs(event.y-y_coord)))
    if abs(event.x-x_coord) < 10 and abs(event.y-y_coord) <10:
        print("YOU FOUND THE TR3A5UR3")
        welcome_label.config(text="You have won! Guesses: ()".format(counter))
    
welcome_label = Label(root, text="Click on the map to search for treasure")
myframe = Frame(root, bg="yellow", height=200, width=200)


myframe.bind("<Button-1>", guess)

welcome_label.pack()
myframe.pack()

root.mainloop()
