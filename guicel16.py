from tkinter import *

root = Tk()

color_list = ["green", "red", "orange", "blue", "brown", "yellow"]
country_list = ["UK", "Spaim", "France", "Portugal", "Germany", "Finland"]

for i in range(6):
    button = Button(root, text=country_list[i], bg=color_list[i])
    button.pack(side=LEFT)

root.mainloop()
