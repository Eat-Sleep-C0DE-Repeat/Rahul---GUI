#CREATING A CALCULATOR
from tkinter import *
root = Tk()
root.title("Calculator")
root.geometry("375x600")
root.configure(background="black") 

def click(event):
    global scvalue
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scvalue.get().isdigit():
            value = int(scvalue.get())
        else:
            value = eval(screen.get())
        scvalue.set(value)
        screen.update()
    elif text == "C":
        scvalue.set("")
        screen.update()
    else:
        scvalue.set(scvalue.get() + text)
        screen.update()

scvalue = StringVar()
scvalue.set("")

Label(root, text = "CALCULATOR", bg = "black",fg = "white", font = "times 38 bold underline").pack()

f = Frame(root, bg = "grey")

screen = Entry(root, textvar = scvalue, font = "lucida 35 bold")
screen.pack(fill = X, padx = 30, pady = 15)

f.pack()

f = Frame(root, bg = "grey")

b = Button(f, text ="9", padx = 20, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>",click)

b = Button(f, text ="8", padx = 20, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>",click)

b = Button(f, text ="7", padx = 20, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>",click)

f.pack()

f = Frame(root, bg = "grey")

b = Button(f, text ="6", padx = 20, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>",click)

b = Button(f, text ="5", padx = 20, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>",click)

b = Button(f, text ="4", padx = 20, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>",click)

f.pack()

f = Frame(root, bg = "grey")

b = Button(f, text ="3", padx = 20, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>",click)

b = Button(f, text ="2", padx = 20, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>",click)

b = Button(f, text ="1", padx = 20, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>",click)

f.pack()

f = Frame(root, bg = "grey")

b = Button(f, text ="+", padx = 20, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>",click)

b = Button(f, text ="0", padx = 20, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>",click)

b = Button(f, text ="-", padx = 23, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>",click)

f.pack()

f = Frame(root, bg = "grey")

b = Button(f, text ="=", padx = 21, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>",click)

b = Button(f, text ="C", padx = 20, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>",click)

b = Button(f, text ="/", padx = 20, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>",click)

f.pack()

f = Frame(root, bg = "grey")

b = Button(f, text =".", padx = 23, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>",click)

b = Button(f, text ="*", padx = 24, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>",click)

b = Button(f, text ="00", padx = 11, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>",click)

f.pack()

root.mainloop()