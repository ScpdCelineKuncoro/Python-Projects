from tkinter import *

root = Tk()

def foo():
    print("Gneiss")

def doo():
    print("Nice")

my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New Notebook", command=doo)
file_menu.add_command(label="Open...", command=doo)
file_menu.add_separator()
file_menu.add_command(label="Make a copy", command=doo)

edit_menu = Menu(my_menu)

edit_menu.add_command(label="Cut cells", command=foo)
edit_menu.add_command(label="Copy cells", command=foo)
edit_menu.add_separator()
edit_menu.add_command(label="Paste cells above", command=foo)

my_menu.add_cascade(label="Edit", menu=edit_menu)

root.mainloop()
