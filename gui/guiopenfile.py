from tkinter import *
from tkinter import filedialog


window = Tk()

# def openfile():
#     filepath = filedialog.askopenfilename()
#     file = open(filepath, "r")
#     print(file.read())
#     file.close()
    
# button = Button(text= "Open", command=openfile)
# button.pack()

# def savefile():
#     file = filedialog.asksaveasfile(defaultextension=".txt", 
#                                     filetypes=[
#                                         ("Text file", ".txt")
#                                     ,   ("HTML file", ".html") 
#                                     ,    ("All files", ".*")])
#     filetext = str(text.get(1.0, END))
#     file.write(filetext)
#     file.close()

def openFile():
    print("File Opened")

def saveFile():
    print("File Saved")



def cut():
    print("Cut")

def copy():
    print("Copied")

def paste():
    print("Pasted")


menubar = Menu(window)
window.config(menu=menubar)
window.config(bg="grey")
fileMenu = Menu(menubar, tearoff=0) #Tearoff // Removes annoying line at top

menubar.add_cascade(label="File", menu=fileMenu)
fileMenu.add_command(label="Open", command=openFile)
fileMenu.add_command(label="Save", command=saveFile)
fileMenu.add_separator() # Adds line to seperate sections of dropdown
fileMenu.add_command(label="Exit", command=quit)


editMenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Edit", menu=editMenu)
editMenu.add_command(label="Cut", command=cut)
editMenu.add_command(label="Copy", command=copy)
editMenu.add_command(label="Paste", command=paste)

window.mainloop()

