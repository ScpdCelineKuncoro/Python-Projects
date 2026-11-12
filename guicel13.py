from tkinter import *

root = Tk()

my_menu = Menu(root)
root.config(menu=my_menu)

file_menu = Menu(my_menu)
my_menu.add_cascade(label='file', menu=file_menu)

file.menu.add_command(label='new notebook', command=)

edit_menu = Menu(my_menu)
my_menu.add_cascade(label='edit', menu=edit_menu)


root.mainloop()
