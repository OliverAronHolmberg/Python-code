from tkinter import *
from tkinter import colorchooser # "submodule" måste importeras separat


def click():
    color = colorchooser.askcolor() # opens the colorchooser /// window.config(bg = colorchooser.askcolor()[1])
    colorHex = color[1]
    window.config(bg = colorHex)


window = Tk()
window.geometry("420x420")
button = Button(text="Click me", command= click, )
button.pack()



window.mainloop()




