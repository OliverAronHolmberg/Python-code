from tkinter import *
from tkinter import messagebox # Import message library



def click():
    # messagebox.showinfo(title= "Infomessagebox", message= "You are a person")

    # while(True):
    #     messagebox.showwarning(title= "Warning", message= "You have a virus")

    # messagebox.showerror(title= "Error", message= "Something went wrong")

    # if messagebox.askokcancel(title="Ask ok cancel", message= "Do you want to do this"):
    #     print("You did a thing")
    # else:
    #     print("You didnt do a thing")

    # if messagebox.askretrycancel(title="Ask ok cancel", message= "Do you want to do retry"):
    #     print("You retried a this")
    # else:
    #     print("You didnt do a thing")

    # if messagebox.askyesno(title="Yes or No", message="Yes or No"):
    #     print("Yes")
    # else:
    #     print("No")

    # answer = messagebox.askquestion(title="Question", message="Do you like pie")
    # if answer == "yes":
    #     print("Yes")
    # else:
    #     print("No")

    # answer = messagebox.askyesnocancel(title="Yes no cancel", message="Do you like to code")
    # if answer==True:
    #     print("True")
    # elif answer==False:
    #     print("False")
    # else:
    #     print("Cancel")

    pass


window = Tk()

button = Button(window, command=click, text = "Click me")
button.pack()


window.mainloop()
