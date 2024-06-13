from tkinter import *
import re
import math


window = Tk()

window.geometry("500x630")

window.title("Calculator")
window.config(bg="#c2c2c2")

texten = ""
number = StringVar(value="")
number = ""
tallista = []



def add_number(new_c):
    global number

    number = number + new_c
    text.config( text=str(number))

    # number += new_c
    # print(number)
    # text.config( text=str(number))
    
# def minusop():
#     global number
#     tallista.append(number)
#     tallista.append("-")
#     number = re.sub(r'\d+', '', str(number))
#     print(tallista)
#     text.config( text=str("-"))
   
# def plusop():
#     global number
#     tallista.append(number)
#     tallista.append("+")
#     number = re.sub(r'\d+', '', str(number))
#     print(tallista)
#     text.config( text=str("+"))
    
# def timesop():
#     global number
#     tallista.append(number)
#     tallista.append("*")
#     number = re.sub(r'\d+', '', str(number))
#     print(tallista)
#     text.config( text=str("*"))

# def divideop():
#     global number
#     tallista.append(number)
#     tallista.append("/")
#     number = re.sub(r'\d+', '', str(number))
#     print(tallista)
#     text.config( text=str("/"))

def clearentry():
    global number
    number = number[:-1]
    text.config( text=str(number))


def clear():
    global number
        
    number = ""
    text.config( text=str(""))
    

def calculate():
    global number
    try:
        total = str(eval(number))
        text.config(text=str(total))
        number = total

    except ZeroDivisionError:
        text.config(text=str("Math error"))
        number = ""

    except SyntaxError:
        text.config(text=str("Math error"))
        number = ""
    except:
        text.config(text=str("Math error"))
        number = ""

def sqrt():
    global total
    global number
    try:
        total = str(eval(number))
        total = math.sqrt(int(total))
        text.config(text=str(total))
        number = ""
        
    except:
        text.config(text=str("Math error"))





    # global tallista
    # tallista.append(number)
    # number = ""
    # print(len(tallista))
    # print(len(tallista))
    # resultat = 0
    # tal1 = int(tallista[0])
    # tal2 = int(tallista[2])
    # if tallista[1] == "+":
    #     resultat = tal1 + tal2
    # if tallista[1] == "-":
    #     resultat = tal1 - tal2
    # if tallista[1] == "*":
    #     resultat = tal1 * tal2
    # if tallista[1] == "/":
    #     resultat = tal1 / tal2
    # print(resultat)
    # tallista = []
    # text.config( text=str(resultat))
    
    # for index in tallista:
    #     if index == "+":
    #         print("Katt")
    #     elif index == "-":
    #         print("Katt")
    #     elif index == "*":
    #         print("Katt")
    #     elif index == "/":
    #         print("Katt")
    #     else:
    #         print("Musse")
           

# Over row


pibutton = Button(window, text="Pi", padx= 20, pady=3, font=("Arial", 15), command=lambda: add_number("3.14159265359"))
pibutton.place(x = 30, y = 10)

rootbutton = Button(window, text=" √ ", padx= 17, pady=3, font=("Arial", 15), command = sqrt)
rootbutton.place(x = 110, y = 10)


# Upper row


minus = Button(window, text="-", padx= 33, pady=5, font=("Arial", 20), command=lambda: add_number("-"))
minus.place(x = 380, y = 220)

cbutton = Button(window, text="C", padx= 28, pady=5, font=("Arial", 20), command=clear)
cbutton.place(x = 250, y = 220)

cebutton = Button(window, text="CE", padx= 20, pady=5, font=("Arial", 20), command=clearentry)
cebutton.place(x = 140, y = 220)

dotbutton = Button(window, text=" . ", padx= 25, pady=5, font=("Arial", 20), command=lambda: add_number("."))
dotbutton.place(x = 30, y = 220)


#Middle Upper row

one = Button(window, text="1", padx= 30, pady=5, font=("Arial", 20), command=lambda: add_number("1"))
one.place(x=30, y=300)


two = Button(window, text="2", padx= 30, pady=5, font=("Arial", 20), command=lambda: add_number("2"))
two.place(x = 140, y = 300)

three = Button(window, text="3", padx= 30, pady=5, font=("Arial", 20), command=lambda: add_number("3"))
three.place(x = 250, y = 300)

plus = Button(window, text="+", padx= 30, pady=5, font=("Arial", 20), command=lambda: add_number("+"))
plus.place(x = 380, y = 300)


#Midde row

four = Button(window, text="4", padx= 30, pady=5, font=("Arial", 20), command=lambda: add_number("4"))
four.place(x=30, y=380)

five = Button(window, text="5", padx= 30, pady=5, font=("Arial", 20), command=lambda: add_number("5"))
five.place(x=140, y=380)

six = Button(window, text="6", padx= 30, pady=5, font=("Arial", 20), command=lambda: add_number("6"))
six.place(x=250, y=380)

times = Button(window, text="x", padx= 32, pady=5, font=("Arial", 20), command=lambda: add_number("*"))
times.place(x = 380, y = 380)

#Last - down Row
seven = Button(window, text="7", padx= 30, pady=5, font=("Arial", 20), command=lambda: add_number("7"))
seven.place(x=30, y=460)

eight = Button(window, text="8", padx= 30, pady=5, font=("Arial", 20), command=lambda: add_number("8"))
eight.place(x=140, y=460)

nine = Button(window, text="9", padx= 30, pady=5, font=("Arial", 20), command=lambda: add_number("9"))
nine.place(x=250, y=460)

division = Button(window, text="÷", padx= 30, pady=5, font=("Arial", 20), command=lambda: add_number("/"))
division.place(x=380, y = 460)




#Last row
zero = Button(window, text="0", padx= 30, pady=5, font=("Arial", 20), command=lambda: add_number("0"))
zero.place(x= 140, y=540)

Equels = Button(window, text="=", padx= 30, pady=5, font=("Arial", 20), command= calculate)
Equels.place(x=380, y = 540)

parentheses1 = Button(window, text =" ( ", padx= 25, pady=5, font=("Arial", 20), command=lambda: add_number("("))
parentheses1.place(x=30, y=540)

parentheses2 = Button(window, text= " ) ", padx= 25, pady=5, font=("Arial", 20), command=lambda: add_number(")"))
parentheses2.place(x=250, y=540)


text = Label(window, width=29, height= 2, bg = "#d4d4d4", text= texten,relief=SOLID, anchor=W, font=("Arial", 19))
text.place(x = 30, y=140)



window.mainloop()



