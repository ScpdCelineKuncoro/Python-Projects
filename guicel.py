from tkinter import *

root = Tk()

frame1 = Frame(root)
frame2 = Frame(root)

label1 = Label(frame1, text="I am in frame one")
button1 = Button(frame1, text="Im frame 1 too")
                 
label2 = Label(frame2, text="I am in frame 2222222")
button2 = Button(frame2, text="Im frame 2 too")

label1.pack(side=LEFT)
label2.pack(side=RIGHT)
button1.pack()
button2.pack()
frame1.pack()
frame2.pack(side=BOTTOM)

root.mainloop()
