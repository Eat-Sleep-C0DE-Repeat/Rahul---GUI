from tkinter import *
from datetime import datetime as dt

root = Tk()

root.geometry("655x333")

root.config(background = "black")


def getvals():
    print("Submitting form...;")
    print(f"{usernamevalue.get(), phonevalue.get(), emailvalue.get()}")

    with open("records1.txt", "a") as f:
        f.write(f"{usernamevalue.get(), phonevalue.get(), emailvalue.get()}\n")

Label(root, text = "Inlongs", bg = "black", fg = "yellow", font = "comicsans 16 bold", pady = 15, padx = 75, relief = RAISED).pack()
Label(root, text = "Get the fastest news on here....", font = "bold", bg = "black", fg = "white").pack()
Label(root,text=f"Date : {dt.now().date()}",font="lucida 15 bold", fg = "white", bg ="black").pack()


f1 = Frame(root, borderwidth = 6, bg = "grey", relief = SUNKEN, width = 1400 )

l = Label(f1, text = "India reports 49,310 new cases\nTotal cases stand at 12,87,945 including 4,40,135 active cases.\nIndia also reported 740 new deaths, taking the toll to 30,601.\nTotal number of cured/discharged/migrated stand at 8,17,209.", font = "Helvetica 16 bold", fg = "black", pady = 20)
l.pack()

f1.pack(anchor = "n")

f1 = Frame(root, borderwidth = 6, bg = "grey", relief = SUNKEN)

l = Label(f1, text = "Women's tennis cancels all China events in 2020 over coronavirus.", font = "Helvetica 16 bold", fg = "black", pady = 20)
l.pack()

f1.pack(anchor = "n")

f1 = Frame(root, borderwidth = 6, bg = "grey", relief = SUNKEN)

l = Label(f1, text = "Rajasthan HC Live updates: Can the Speaker disqualify Sachin Pilot? Verdict soon\nThe 19 dissident MLAs had filed a petition in the high court, challenging the disqualification notices.\nGehlot said those who went to court are the ones who were wrong and had been misguided.", font = "Helvetica 16 bold", fg = "black", pady = 20)
l.pack()

f1.pack(anchor = "n")

frame1 = Frame(root)

username = Label(frame1, text = "Username ", bg = "grey")
username.pack(side = LEFT)
usernamevalue = StringVar()
usernameentry = Entry(frame1, textvariable = usernamevalue)
usernameentry.pack(side = LEFT)

frame1.pack()

frame1 = Frame(root)

phone = Label(frame1, text = "Phone No.", bg = "grey")
phone.pack(side = LEFT)
phonevalue = StringVar()
phoneentry = Entry(frame1, textvariable = phonevalue)
phoneentry.pack(side = RIGHT)

frame1.pack()

frame1 = Frame(root)

email = Label(frame1, text = "Email-ID    ", bg = "grey")
email.pack(side = LEFT)
emailvalue= StringVar()
emailentry = Entry(frame1, textvariable = emailvalue)
emailentry.pack(side = LEFT)

frame1.pack()

frame1 = Frame(root)

Button(frame1, text = "Submit..", command = getvals).pack()

frame1.pack()

root.mainloop()