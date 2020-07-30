#CREATING A CALCULATOR
from tkinter import *
root = Tk()
root.title("Calculator")
root.geometry("350x630")
root.maxsize(350, 630)
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

Label(root, text = "CALCULATOR", bg = "black",fg = "white", font = "times 32 bold underline").pack()

f = Frame(root, bg = "grey")

screen = Entry(root, font=("arial 20 bold"), textvariable = scvalue, bd = 15, insertwidth = 4, bg = "grey", justify= 'right')
screen.pack(fill = X, padx = 30, pady = 15)

f.pack()

f = Frame(root, bg = "black")

b = Button(f, bd = 8, text ="9", padx = 20, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>",click)

b = Button(f, bd = 8, text ="8", padx = 20, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>",click)

b = Button(f, bd = 8, text ="7", padx = 20, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>",click)

f.pack()

f = Frame(root, bg = "black")

b = Button(f, bd = 8, text ="6", padx = 20, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>",click)

b = Button(f, bd = 8, text ="5", padx = 20, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>",click)

b = Button(f, bd = 8, text ="4", padx = 20, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>",click)

f.pack()

f = Frame(root, bg = "black")

b = Button(f, bd = 8, text ="3", padx = 20, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>",click)

b = Button(f, bd = 8, text ="2", padx = 20, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>",click)

b = Button(f, bd = 8, text ="1", padx = 20, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>",click)

f.pack()

f = Frame(root, bg = "black")

b = Button(f, bd = 8, text ="+", padx = 19, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>",click)

b = Button(f, bd = 8, text ="0", padx = 20, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>",click)

b = Button(f, bd = 8, text ="-", padx = 24, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>",click)

f.pack()

f = Frame(root, bg = "black")

b = Button(f, bd = 8, text = "=", padx = 20, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>",click)

b = Button(f, bd = 8, text ="C", padx = 18, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>",click)

b = Button(f, bd = 8, text ="/", padx = 22, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>",click)

f.pack()

f = Frame(root, bg = "black")

b = Button(f, bd = 8, text = ".", padx = 23, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>",click)

b = Button(f, bd = 8, text = "*", padx = 24, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>",click)

b = Button(f, bd = 8, text = "%", padx = 11, font = "lucida 20 bold")
b.pack(side = LEFT, padx = 5, pady = 5)
b.bind("<Button-1>",click)

f.pack()

root.mainloop()
