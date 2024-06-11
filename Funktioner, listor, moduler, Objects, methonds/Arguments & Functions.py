#Function = a block of code which is only executed wehn it is called

# Return = statement used to end a function and send a result back to the caller

# def add(x, y):
#     z = x + y
#     return z

# print(add(1, 2))




#_____________________________________________________


# Default arguments = A default value for certain parameters
#                     default is used when argument is omitted
#                     make your functions more flexible, reduces # of arguments
#                     1. Positional, 2. DEFAULT, 3. Keyword, 4. Arbitrary

#                                    I              I
# def net_price(list_price, discount=0, sales_tax=0.05):
#     return list_price * (1 - discount) * (1 + sales_tax)

# print(net_price(500))
# print(net_price(500, 0.1, 0))





# import time

# def count(end, start=0):
#     for x in range(start, end+1):
#         print(x)
#         time.sleep(1)
#     print("Done")


# count(10, 2)



#___________________________________________________________________________


# Keyword Arguments = an agrument preceded by an identifier
#                     helps whith readability
#                     order of arguments doens't matter
#                     1. Positional, 2. Default, 3. KEYWORD, 4. Arbitrary



# def hello(greeting, title, first, last):
#     print(f"{greeting} {title} {first} {last}")


# hello(last="Kenobi", greeting="Hello there",  first="Obi Wan" , title="General")





# for x in range(1, 11):
#     print(x, end=" ") /// end= är ett keyword argument




# print("1", "2", "3", "4", "5" , sep="-") /// sep= är ett keyword argument /// sep= == seperate


# def get_phone(country, area, first, last):
#     return f"+{country}-{area}-{first}-{last}"

# phone_num = get_phone(country=46, first=8232,area=123, last=3312)

# print(phone_num)

#____________________________________________________________________________________________________________


# *args     = allows you to pass multiple non-key arguments // gör det till en Tuple
# **kwargs  = allows you to pass multiple keyword arguments // gör det till en Dictionary
#             * unpacking operator
#             1. Positional, 2. Default, 3. Keyword, 4. ARBITRARY



# *args
# def add(*args): Kan namnge args i *args vad som helst så länge * finns där så funkar det, forlk brukar bara namnge det args för simplicity sake
#     total = 0
#     for arg in args:
#         total += arg
#     return total


# print(add(1, 5, 3))

# def add(*num): 
#     total = 0
#     for arg in num:
#         total += arg
#     return total


# print(add(1, 5, 3))


# def display_name(*args):
#     total_name = ""
#     for name in args:
#         total_name += name + " "
#     return total_name

# print(display_name("filip", "linus", "idioti"))



# kwargs

# def print_address(**kwargs): // kwargs är en dictionary så man ska använda kommands eller vad de nu heter som funkar för dictionarys för att affecta dom
#     for keys, value in kwargs.items():
#         print(f"{keys}:{value}")


# print_address(street="Blåklockans väg 8", 
#               city="Stockholm", 
#               province="Uppland", 
#               zip="13245")



#_______________________________________________________________________________





# Variable Scope = where a variable is visible and accessible
# scope resolution = (LEGB) Local -> Enclosed -> Global -> Built-in




#Local

# def mitt_hus(): # I detta fall kan jag se hur många mjölkpaket jag har, grannes kan se hur många mjölkpaket hn har, men vi kan inte se varandras mjölkpaket.
#     Mjölkpaket = 1
#     print(Mjölkpaket)

# def grannes_hus():
#     grannemjölkpajket = 2
#     print(grannemjölkpajket)

#RÄTT




# def mitt_hus(): # Därför blir detta fel eftersom jag inte vet grannens mjölkpaket och grannes kan inte se mina
#     Mjölkpaket = 1
#     print(grannemjölkpajket)

# def grannes_hus():
#     grannemjölkpajket = 2
#     print(Mjölkpaket)


#FEL

#Därför i dessa exempel är scope resolution local för både funktionerna




#Enclosed



# def func1():
#     x = 1
#     def func2():
#         print(x)
#     func2()

# func1()
# ifall det inte finns en variabel kollar funktuionen om det finns en annan frunktion i funktionen och om det finns det kollar den ifall det finns en annan variabel x, 
# om det gör det används den

#Locala går före Enclosed


#Complicerat, covera mer sen







#Global

# def func1():
#     print(x)

# def func2():
#     print(x)

# x = 3

# 3
# 3


#Lokala och enclosed går före globala 








# from math import e

# def func1():
#     print(e)

# e = 3
# func1()

# lokala, enclosed och globala går alla föra Built-in 


#_________________________________________________________________

# if __name__ == "__main__": (this script can be imported OR run standalone)
#                             Functions and classes in this module can re reused
#                             without the main bklock of code executing

# ex. library = Import library for functionality
#               When running library directly, display a help page

# def main():
#     pass

# if __name__ == "__main__":
#     main()


#__main__ är lika med __name__ 
# // testa: print(__name__)



#Man har koden för att inte scripts ska köras när man inte kör det scriptet utan ett annat, alltså måste man köra scrípt1 för att executa koden i script1 
# man kan alltså inte köra script2 och executa koden i script1, alltså ifall man importat ett script helt, allting med : *
# Man kan också vilja låna script från script1 men inte köra koden direkt, då kan man också använda if __name__ == __main__: funktionen











#____________________________________________________________________________________________________________________
#Också * betyder allting så man kan ex. skriva: from examplemodule import * // för att importa allt i det scriptet
#____________________________________________________________________________________________________________________

# Assign functions to variables

def hello():
    print("Hello")

hello()

print(hello)
hi = hello
hi() #Den har två namn nu


say = print

print("Musse")

say("Musse")


#__________________________________________________________________________________

# Higher Order Function = a finction that either:
#                         1. accepts a function as an argument
#                           or
#                         2. returns a function
#                         (In python, functions are also treated as objects)



def loud(text):
    return text.upper()

def quiet(text):
    return text.lower()

def hello(func): # Higher order function // accepts a function as an argument
    text = func("hello")
    print(text)


hello(loud)
hello(quiet)




def divisor(x): # Är en higher order function för den: returns a function
    def dividend(y):
        return y / x
    return dividend


divide = divisor(2)
print(divide(10))



#______________________________________________________________________________________________________

# lambda function = function written in 1 line using lambda keyword
#                   accepts any number of arguments, but only has one expression
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time)
#
# lambda parameters:expressions


#Normal fuction
# def double(x):
#     return x * 2

# print(double(5))


# lambda function

double = lambda x: x * 2
print(double(5))

print("")


muiltiply = lambda x, y: x * y
print(muiltiply(5, 2))


add = lambda x, y, z: x + y + z
print(add(5, 2, 9))

full_name = lambda x, y: x + " " + y
print(full_name("Oliver", "Holmberg"))

agecheck = lambda age: True if age >= 18 else False
print(agecheck(18))

#____________________________________________________________________________________________________

# sort() method = used with lists
# sort() function = used with iterables (tuples, disctionarys, sets, lists)

# sort() method

students = ["Musse", "Nusse", "Tusse", "Busse", "Lusse"]

students.sort() # sort with list kan acceptera 2 keyword arguments: key=, reverse= /// Sorterar dom i aflabetisk ordning
for i in students:
    print(i)

print("")

# sort() function

sorted_students = sorted(students, reverse=True)
for i in sorted_students:
    print(i)


#-----------------------

students2 = [("Musse", "F", 20),
             ("Tusse", "A", 100)]


grade = lambda grades:grades[1]
students2.sort(key=grade)

for i in students2:
    print(i)



#______________________________________________________________________________________