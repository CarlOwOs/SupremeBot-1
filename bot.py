from tkinter import *

def clicked():
    print(txt.get())

window = Tk()
window.title("SupremeBot")
window.geometry('350x200')
lbl = Label(window, text="Hello", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)
btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=1)
txt = Entry(window,width=10)
txt.grid(column=1, row=0)


window.mainloop()
