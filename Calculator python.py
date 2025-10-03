from tkinter import *

def click(event):
    global screenvalue
    text = event.widget.cget("text")
    if text == "=":
        try:
            value = eval(screenvalue.get())
            screenvalue.set(value)
            screen.update()
        except Exception:
            screenvalue.set("error")
            screen.update()
    elif text == "C":
        screenvalue.set("0")
        screen.update()
    else:
        if screenvalue.get() == "0":
            screenvalue.set("")
        screenvalue.set(screenvalue.get() + text)
        screen.update()

window = Tk()
window.geometry("500x500")
window.title("BASIC CALCULATOR")

screenvalue = StringVar()
screenvalue.set("0")
screen = Entry(window, textvariable=screenvalue, font="Arial 20 bold")
screen.pack(fill=X, ipadx=8, pady=10, padx=10)

frame1 = Frame(window, bg="black")
for text in ["9", "8", "7"]:
    b = Button(frame1, text=text, padx=20, pady=20, font="Arial 15 bold")
    b.pack(side=LEFT, padx=10, pady=10)
    b.bind("<Button-1>", click)
frame1.pack()

frame1 = Frame(window, bg="black")
for text in ["6", "5", "4"]:
    b = Button(frame1, text=text, padx=20, pady=20, font="Arial 15 bold")
    b.pack(side=LEFT, padx=10, pady=10)
    b.bind("<Button-1>", click)
frame1.pack()

frame1 = Frame(window, bg="black")
for text in ["3", "2", "1"]:
    b = Button(frame1, text=text, padx=20, pady=20, font="Arial 15 bold")
    b.pack(side=LEFT, padx=10, pady=10)
    b.bind("<Button-1>", click)
frame1.pack()

frame1 = Frame(window, bg="black")
for text in ["0", "-", "+"]:
    b = Button(frame1, text=text, padx=20, pady=20, font="Arial 15 bold")
    b.pack(side=LEFT, padx=10, pady=10)
    b.bind("<Button-1>", click)
frame1.pack()

frame1 = Frame(window, bg="black")
for text in ["*", "/", "%"]:
    b = Button(frame1, text=text, padx=20, pady=20, font="Arial 15 bold")
    b.pack(side=LEFT, padx=10, pady=10)
    b.bind("<Button-1>", click)
frame1.pack()

frame1 = Frame(window, bg="black")
for text in ["C", "=", "."]:
    b = Button(frame1, text=text, padx=20, pady=20, font="Arial 15 bold")
    b.pack(side=LEFT, padx=10, pady=10)
    b.bind("<Button-1>", click)
frame1.pack()

window.mainloop()
