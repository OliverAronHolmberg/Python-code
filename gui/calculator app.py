from tkinter import *



window = Tk()

window.geometry("500x630")

window.title("Calculator")

texten = "bla"
number = StringVar(value="")
number = ""
mode = 0 # 1 för +, 2 för -, 3 för *, 4 för /
tallista = []

def add_number(new_c):
    global number
    number1 += new_c
    print(number)

    
def operator():
    


def calculate():
    global number1
    
    


    float(number)
    print(number)




# Upper row


minus = Button(window, text="-", padx= 33, pady=5, font=("Arial", 20), command=lambda: add_number("-"))
minus.place(x = 380, y = 220)


#Middle Upper row

one = Button(window, text="1", padx= 30, pady=5, font=("Arial", 20), command=lambda: add_number("1"))
one.place(x=30, y=300)


two = Button(window, text="2", padx= 30, pady=5, font=("Arial", 20), command=lambda: add_number("2"))
two.place(x = 140, y = 300)

three = Button(window, text="3", padx= 30, pady=5, font=("Arial", 20), command=lambda: add_number("3"))
three.place(x = 250, y = 300)

plus = Button(window, text="+", padx= 30, pady=5, font=("Arial", 20))
plus.place(x = 380, y = 300)


#Midde row

four = Button(window, text="4", padx= 30, pady=5, font=("Arial", 20), command=lambda: add_number("4"))
four.place(x=30, y=380)

five = Button(window, text="5", padx= 30, pady=5, font=("Arial", 20), command=lambda: add_number("5"))
five.place(x=140, y=380)

six = Button(window, text="6", padx= 30, pady=5, font=("Arial", 20), command=lambda: add_number("6"))
six.place(x=250, y=380)

times = Button(window, text="x", padx= 32, pady=5, font=("Arial", 20))
times.place(x = 380, y = 380)

#Last - down Row
seven = Button(window, text="7", padx= 30, pady=5, font=("Arial", 20), command=lambda: add_number("7"))
seven.place(x=30, y=460)

eight = Button(window, text="8", padx= 30, pady=5, font=("Arial", 20), command=lambda: add_number("8"))
eight.place(x=140, y=460)

nine = Button(window, text="9", padx= 30, pady=5, font=("Arial", 20), command=lambda: add_number("9"))
nine.place(x=250, y=460)

division = Button(window, text="÷", padx= 30, pady=5, font=("Arial", 20))
division.place(x=380, y = 460)




#Last row
zero = Button(window, text="0", padx= 30, pady=5, font=("Arial", 20), command=lambda: add_number("0"))
zero.place(x= 140, y=540)

Equels = Button(window, text="=", padx= 30, pady=5, font=("Arial", 20), command= calculate)
Equels.place(x=380, y = 540)



text = Label(window, width=63, height= 4, bg = "#d4d4d4", text= texten,relief=SOLID, anchor=W)
text.place(x = 30, y=140)



window.mainloop()



