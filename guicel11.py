from tkinter import *
root = Tk()

def change_temperature():
    temp = thermostat.get()

    if temp<10:
        print("Cold")
    elif temp>50 and temp<90:
        print("Hot")
    elif temp>90:
        print("Dead")

thermostat = Scale(root)
thermostat.pack()

warning = Label(root, text="This is your thermostat")
warning.pack()
button1 = Button(root, text="Change temp", command=change_temperature)
button1.pack()

root.mainloop()
