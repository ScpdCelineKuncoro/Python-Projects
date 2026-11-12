from tkinter import *

root = Tk()

email_label = Label(root, text="Email: ")
password_label = Label(root, text="Password: ")

email_entry = Entry(root)
password_entry = Entry(root)

email_label.grid(row=0, column=0)
password_label.grid(row=1, column=0)
email_entry.grid(row=0, column=1)
password_entry.grid(row=1, column=1)

root.mainloop()
