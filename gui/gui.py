#Måste import tkniter: from tkinter import *


from tkinter import *



# Widgets = GUI elements: buttons, textboxes, lebels, images
# Windows = serves as a container to hold or contain these widgets


window = Tk() # Instanciaye an instance of a window
window.geometry("1280x720") # Sätter storleken på förstret
window.title("First GUI program") # Sätter namnet på fönstret

icon = PhotoImage(file= 'gui\\elements\\images.png') # Konverterar iconen till en PhotoImage /// måsta vara en png och vara det när man skapar bilden / laddar ner den
window.iconphoto(True, icon) #Sätter iconen på window

window.config(background="#b3fff2") # Kan användas varje gång man vill ändra något i fönstret


# Labels


# label = an area widget that holds text and/or an imahe within a window

label = Label(window, text="Hello World", 
              font=("Arial", 40, "bold"), 
              fg="#308a7a", 
              bg= "#b3fff2", 
              relief=RAISED, 
              bd = 10,
              padx = 20,
              pady = 5,
              image=icon, 
              compound="bottom") # Man kan ändra text, font, färg, bakgrunds färg, border, borderstorlek, bilder, padding mm
# label.pack()
label.place(x = 100 , y = 200)


#Buttons


# button = you click it, action happen

count = 1
def click():
    global count
    print("Clicked")
    print(count)
    count = count + 1
    

button = Button(window, # Samma som Label bara att det finns ett click command, active forground och background och state
                text="Click me",
                font=("Arial", 40, "bold"),
                command=click,
                bg = "#b3fff2",
                fg = "#308a7a",
                activeforeground="#308a7a",
                activebackground="#b3fff2",
                state=ACTIVE)
button.place(x = 600, y= 200)



#Entry Box


# entry widget = textbox tjay accepts a single line of user input



def submit():
    username = entry.get()
    print(username)
    entry.delete(0, END)


    entry.config(state=DISABLED)

entry = Entry(window, font=("Arial", 50), show="*")
entry.insert(0, "Hej")
entry.pack()


summitbutton = Button(window, text="Submitt",
                      command= submit)
summitbutton.pack(side=RIGHT)


# Checkboxes


def display():
    if(x.get() == 1):
        print("Agreed")
    else:
        print("Not agreed")


x = IntVar()
print(x)





checkbox = Checkbutton(window, text="I agree to the terms of condition", # Checkboxes storas 1 och 0 och normalvis är dom på 0 man kan ändra vad som är i variabeln med onvalue= och offvalue=
                       variable = x,
                       onvalue=1,
                       offvalue=0,
                       command= display)

checkbox.pack()





#RadioButtons


#Radiobutton = similar to checkbox nut you can only select one from a group



food = ["pizza", "hamburger", "hotdog"]

def order():
    if(x.get() == 0):
        print("Pizza")
    elif(x.get() == 1):
        print("Hamburger")
    elif(x.get() == 2):
        print("Hotdog")
    else:
        print("Huh")


x = IntVar()

for idnex in range(len(food)):
    radio = Radiobutton(window, text= food[idnex], variable=x, value= idnex, padx= 25, command= order)
    radio.pack(side= BOTTOM, anchor="w")



#Scale


def summit():
    print("the tempreture is: "+ str(scale.get())+ " degrees celcius")


scale = Scale(window, from_=100, to=0, length= 300, width= 30, orient=HORIZONTAL, tickinterval= 10, showvalue= 0, troughcolor="grey", bg= "black", activebackground="black")
scale.pack(side = BOTTOM)

scale.set(((scale["from"]-scale["to"])/2+scale["to"])) # Bra formel för att få den i mitten om man ska ändra på values

button3 = Button(window, text="Sumbit", command= summit)
button3.pack(side= BOTTOM)




def createWindow():
    new_window = Toplevel() # TopLevel() = new window "on top" of other windows, linked to a "bottom" window
    new_window2 = Tk() # Tk() = New independant window



button4 = Button(window, text="Create new window", command= createWindow)
button4.pack(side=LEFT)





window.mainloop() # Place window on computar screen, listen for events'