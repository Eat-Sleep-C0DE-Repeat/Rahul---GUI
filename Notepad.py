#GUI Notepad
from tkinter import *
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

def newFile():
    global file
    root.title("Untitled - Notepad")
    file = None
    TextArea.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension = ".txt", filetypes = [("All files", "*.*", ("Text Documents", "*.txt"))])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file) + " - Notepad")
        TextArea.delete(1.0,END)

        f = open(file, "r")
        TextArea.insert(1.0, f.read())

        f.close()

def saveFile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = "Untitled.txt", defaultextension = ".txt", filetypes = [("All files", "*.*", ("Text Documents", "*.txt"))])
        
        if file == "":
            file = None
        else:
            #Save it as a New File
            f = open(file, "w")
            f.write(TextArea.get(1.0, END))
            f.close()

            root.title(os.path.basename(file) + " - Notepad")

def quitApp():
    root.destroy()
def cut():
    TextArea.event_generate(("<<Cut>>"))
def copy():
    TextArea.event_generate(("<<Copy>>"))
def paste():
    TextArea.event_generate(("<<Paste>>"))
def about():
    showinfo("Notepad", "Notepad created by me.")

if __name__ == "__main__":
    #Basic Tkinter Setup

    root = Tk()
    root.title("Untitled - Notepad")
    #root.wm_iconbitmap("")
    root.geometry("644x788")

    TextArea = Text(root, font = "lucida 14")
    file = None
    TextArea.pack(expand = True, fill = BOTH)

    #Creating a menubar
    Menubar = Menu(root)
    fileMenu = Menu(Menubar, tearoff = 0)
    
    #To open a new file
    fileMenu.add_command(label = "New", command = newFile)

    #To open an already existing file 
    fileMenu.add_command(label = "Open", command = openFile)

    #To save the current file
    fileMenu.add_command(label = "Save", command = saveFile)
    fileMenu.add_separator()
    fileMenu.add_command(label = "Exit", command = quitApp)

    Menubar.add_cascade(label = "File", menu = fileMenu)

    editMenu = Menu(Menubar, tearoff = 0)
    #To give a feature of Cut, Copy and Paste
    editMenu.add_command(label = "Cut", command = cut)
    editMenu.add_command(label = "Copy", command = copy)
    editMenu.add_command(label = "Paste", command = paste)

    Menubar.add_cascade(label = "Edit", menu = editMenu)

    helpMenu = Menu(Menubar, tearoff = 0)
    helpMenu.add_command(label = "About Notepad", command = about)

    Menubar.add_cascade(label = "Help", menu = helpMenu)

    root.config(menu = Menubar)

    statusbar = Frame(root, bd=1, relief=SUNKEN)
    statusbar.pack(side=BOTTOM, fill=X)

    Label(statusbar,text="READY", width=20).pack(side=LEFT)
    Label(statusbar, text="Ln: Col: ", width=20).pack(side=RIGHT)

    #Adding Scrollbar using rules
    scroll = Scrollbar(TextArea)
    scroll.pack(side = RIGHT, fill = Y)
    scroll.config(command = TextArea.yview)
    TextArea.config(yscrollcommand = scroll.set)

    root.mainloop()

