# Exeption handeling 


#Exeptions = events detected during execution that interupt the flow of a program


# num1 = int(input("Skriv ett nummer"))

# num2 = int(input("Skriv ett nummer"))

# result = num1/num2
# print(result)



# om num1 är 5 och num 2 är 0 frå vi en exeption för det går inte att dela på 0


#num 1 = 5
#num2 = 0

#result = 5/0

#print(result)




# Exception has occurred: ZeroDivisionError
# division by zero
#   File "C:\Users\Olive\Python\Info\Funktioner, listor, moduler, Objects\Exemptions.py", line 11, in <module>
#     result = num1/num2
#              ~~~~^~~~~
# ZeroDivisionError: division by zero





#Man kan göra try: för kod som är farlig/stor risk för exeptions
#Ifall man ska göra en try måste det finnas en except: 


# try:
#     num1 = int(input("Skriv ett nummer"))

#     num2 = int(input("Skriv ett nummer"))

#     result = num1/num2
#     print(result)
# except Exception:
#     print("Fel")


#Man ska generelt inta använda Exception i en except, alltså: except Exeption: 
#Man ska försöka hantera specifika problem istället
#För att göra detta kan man skiva mer except-block


try:
    num1 = int(input("Skriv ett nummer"))

    num2 = int(input("Skriv ett nummer"))

    result = num1/num2
    print(result)
except ZeroDivisionError as e:
      print(e)
      print("You cant divide by zero")
except ValueError as e:
     print(e)
     print("Det måste vara ett nummer")
except Exception as e:
     print(e)
     print("Det måste vara ett nummer")
else:
     print(result)

finally:
    print("This will always execute") #finally är ett bra sätt att hantera kod som alltid måste hanteras i slutet av koden, det används oftast för att stänga öppnade filer
