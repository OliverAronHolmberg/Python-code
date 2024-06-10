import os # rekomenderas av Bro Code för importering av filer

# path = "C:\\Users\\Olive\\Desktop\\test.txt"


# if os.path.exists(path):
#     print("that locations exists")
#     if os.path.isfile(path):
#         print("That is a file")
# else: 
#     print("That location doesn't exist")

# print("")

# #_________________________________________________________________

#Read a file /// With open(), file.read()

# try:
#     with open("testbla") as file:
#         print(file.read())
# except FileNotFoundError:
#     print("That file was not found")

# print(file.closed) # Om man gör, with open, så stängs filen automatiskt


#_________________________________________________________________________

#Write a file # Man kan lägga till ett andra argument i, with open, 
# "r" för read 
# "w" för write
# "a" för append

#Om man har det i write skriver den över förra texten om man ändrar "text" i detta fall till ngt annat

#Om man har den i append lägger den till text istället

# text = "Var fär musse nusse\n Inte mat för han är fet"

# try:
#     with open("testbla2", "a") as file:
#         file.write(text)
# except:
#     pass

# Den har svårt med å, ä, ö och blir ett frågetecken, det borde därför inte skrivas ijalla fall inte i visual studio

#__________________________________________________________________________

# copyfile() = copies contents of a file
# copy() = copyfile() + permission mode + destination can be a directory
# copy2() = copy() + copies metadata (file's creation and modification times)


# import shutil # Finns andra sätt också men Bro Code brukar använda "Shutil"


# shutil.copyfile("testbla2", "copy") # 2 arguments,   source, destination
# #shutil.copy() samme argument
# #shutil.copy2() samme argument









#__________________________________________________________________________

#Move a file

# source = "C:\\Users\\Olive\\Python\\Info\\testbla.txt"

# destinations = "C:\\Users\\Olive\\Desktop\\testbla.txt"


# try:
#     if os.path.exists(destinations):
#         print("There is already a file there")
    
#     else:
#         os.replace(source, destinations)
#         print(source+" was moved")


# except FileNotFoundError:
#     print(source+" hittades inte")



#__________________________________________________________________

# Delete a file


import os # Rekomenderas för att delete filer
import shutil

# try:
#     os.remove("copy")
# except FileNotFoundError:
#     print("Filen hittades inte")
# except PermissionError:
#     print("You do not have permission to delete this file")
# else:
#     print("Something unexpected happend, file was not deleted")



#Man kan också sätta in en variabel som heter path i paranteserna
# path = "copy"
# os.remove(path)


#Remove tar inte bort tomma filer

#För att göra det använd, rmdir som står för remove directory


# try:
#     os.rmdir("empty") 
# except FileNotFoundError:
#     print("File not found")
# except PermissionError:
#     print("You do not have permission to delete that folder")
# except OSError: # här blir det fel
#     print("You cannot delete that using that function")
# else:
#     print("Something unexpected happend")


#Om man försöker ta bort en fil med ngt i den får man exception error.

#För att ta bort en fil med något i behöver man "import shutil" 



#!!!!!!!!Man kan använda shutil.rmtree för att ta bort alla filer samt foldern men det är farligt så använd helst inte!!!!!!!!!!!

# try:
#     shutil.rmtree("empty")  # !!!!!!!!!!!Var försiktig med denna funktion, den deletar folder och alla filer i den så den är farlig!!!!!!!!!!!!!
# except FileNotFoundError:
#     print("File not found")
# except PermissionError:
#     print("You do not have permission to delete that folder")
# except OSError: # här blir det fel
#     print("You cannot delete that using that function")
# else:
#     print("Something unexpected happend")
