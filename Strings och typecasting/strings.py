#Funktioner


# string = "Musse"


# len() /// Längden på stringen, hur många bokstäver, mellanslag och special tecken det är
# print(len(string)) = 5



#___________________________________________________________________


#Methods

# name = "musse"



# name.find("s") /// Hittar den första tecknet av en special typ och ger dess plats på tecknet som output, alltså i detta fall 2

# name.rfind("s") /// Reverse Find //// Hittar den sista tecknet av en special typ och ger dess plats på tecknet som output, alltså i detta fall 3


# Om den inte kan hitta ett tecken i .find eller .rfind funktionen get den output av -1



# name.capitalize() /// Ger en string som output, den byter den första bokstaven till en stor bokstav

# name.upper() /// gör alla bokstäver till stora bokstäver

# name.lower() /// gör alla bokstäver till små bokstäver

# name.isdigit() /// Ger outputen True om stringen bara innehåller nummer, ger false annars

# name.isalpha() /// Ger outputen True om stringen bara innehåller bokstäver, ger false annars

# name.count() /// Placera ett tecken i paranterserna, den kommer räkna hur många gånger det tecknet finns där, om det inte finns det tecknet ger den 0

# name.replace() /// Byt ur vissa tecken man sätter i parantesen mot ett annat tecken, .replace("s", "l")




# mer metoder kan man få reda på om man skriver: print(help(str))







#_________________________________________________________________


#Operators

# Indexing = accening elements of a sequence using [] (indexing operator)
#           [start : end : step]


# credit = "1234-5678-9012-1229"



#Start
# print(credit[5])

#End
# print(credit[0 : 4])
# print(credit[5 : 9])
# print(credit[5 : ]) 
# print(credit[-2 ])

#Step
# print(credit[:: 2]) /// Skippar varje andra tecken
# print(credit[:: 3]) /// Skippar varje tredje tecken
# print(credit[:: -1]) /// En negativ step gör så att stringen vänder, alltså svaret skulle vara: 9221-2109-8765-4321




# last_digits = credit[-4 : ]
# print(last_digits)






#_______________________________________________________

# F strings /// gör så man kan inserta variabler i strings, skriv f före stringen


#humör = "Arg"
# print(f"musse är {humör}) 

# musse är Arg





#Format specifiers = {value:flags} format a value based on what flags are inserted


# .(number)f = round to that many decimal pacer (fixed point)
# :(number) = allocate tat many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = rught justify
# :+ = use a plus sign to indicate a positive value
# := = place sign to leftmost position
# :  = insert a space before positive numbers
# :, = comma seperator



# pris1 = 3.14159
# pris2 = -292.32222
# pris3 = 12.112


# print(f"Pris 1 är {pris1:.2f}") # : .(för att visa att det ska vara decimaltal) 2(för att visa hur många decimaler) f(för att visa att det är en float)

# print(f"Pris 2 är {pris2:.4f}") # : .(för att visa att det ska vara decimaltal) 4(för att visa hur många decimaler) f(för att visa att det är en float)

# print(f"Pris 3 är {pris3:.3f}") # : .(för att visa att det ska vara decimaltal) 3(för att visa hur många decimaler) f(för att visa att det är en float)






# print(f"Pris 1 är {pris1:10}") # lägger till 10 platser för att visa svaret på:    3.14159 (lägg märke till mellanslagen innan)

# print(f"Pris 2 är {pris2:11}")# lägger till 11 platser för att visa svaret på:  -292.32222 (lägg märke till mellanslagen innan)

# print(f"Pris 3 är {pris3:30}")# lägger till 30 platser för att visa svaret på:                         12.112 (lägg märke till mellanslagen innan)



# print(f"Pris 1 är {pris1:010}") # lägger till 10 platser för att visa svaret på, men ifall det skulle finnas ett mellanslag finns nu en 0: 0003.14159

# print(f"Pris 2 är {pris2:011}")# lägger till 11 platser för att visa svaret på, men ifall det skulle finnas ett mellanslag finns nu en 0: -0292.32222

# print(f"Pris 3 är {pris3:030}")# lägger till 30 platser för att visa svaret på, men ifall det skulle finnas ett mellanslag finns nu en 0:  00000000000000000000000012.112



# print(f"Pris 1 är {pris1:<10}") # Byter sida på mellanslaget (3.14159    ) /// Det kommer inte paranteser, dom bara finns där för att lättare visa

# print(f"Pris 2 är {pris2:<11}") # Byter sida på mellanslaget (-292.32222  ) /// Det kommer inte paranteser, dom bara finns där för att lättare visa

# print(f"Pris 3 är {pris3:<30}") # Byter sida på mellanslaget (12.112                         ) /// Det kommer inte paranteser, dom bara finns där för att lättare visa



# print(f"Pris 1 är {pris1:^10}") # Samma sak bara att det är centrerat denna gång: (  3.14159  ) /// paranteser kommer inte, just for show

# print(f"Pris 2 är {pris2:^11}") # Samma sak bara att det är centrerat denna gång: osv

# print(f"Pris 3 är {pris3:^30}") # Samma sak bara att det är centrerat denna gång: osv





#print(f"Pris 1 är {pris1:+10}") # Lägg till ett + för att visa ifall ett tal är posetivt, alltså: +3.14159

#print(f"Pris 2 är {pris2:+11}") # Lägg till ett + för att visa ifall ett tal är posetivt, alltså funkar inte det för pris2 och vi får: -292.32222

#print(f"Pris 3 är {pris3:+30}") # Lägg till ett + för att visa ifall ett tal är posetivt, alltså: +12.112




# pris4 = 40000000.12

# print(f"Pris 4 är {pris4:,}") # Lägger till komma tecken för stora nummer, alltså i detta fall: 40,000,000.12


#Man kan kombinera olika format specifiers med varandra.


# print(f"Pris 4 är {pris4:,.1f}") # alltså 40,000,000.1

# print(f"Pris 4 är {pris4:+,.1f}") # +40,000,000.1



#_________________________________________________________________________



