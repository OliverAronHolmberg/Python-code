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

def savefile():
    file = filedialog.asksaveasfile(defaultextension=".txt", 
                                    filetypes=[
                                        ("Text file", ".txt")
                                    ,   ("HTML file", ".html") 
                                    ,    ("All files", ".*")])
    filetext = str(text.get(1.0, END))
    file.write(filetext)
    file.close()

button = Button(text= "Save", command=savefile)
button.pack()
text = Text(window)
text.pack()


window.mainloop()

