#Typecasting = Convertera en datatyp till en annan 
#(Booleon, int, str, float)

#Explicit


Fnatt = ""
name = "Musse"
age = 9 #int
gps = 1.9
Katt = True

gps = int(gps)
age = float(age)
Katt = str(Katt)
name = bool(name)

print(type(name))
print(type(age))
print(type(gps))
print(type(Katt))



gps = bool(gps) # om man konverterar ett nummer(int eller float) till en bool så kommer det alltid vara True om det inte är 0 tilloch med negativa tal
name = bool(name) # Ifall man konvertar en str till en bool så kommer den alltid bli True ifall det finns tecken i stringen, om den är tom blir den False, ett mellanslag blir också True
Fnatt = bool(Fnatt)
print(gps)
print(name)
print(Fnatt)



#Inplicit

#Det är när en value eller vriabel blir converterad till en annan data typ automatiskt




x = 2
y = 2.0

x = x/y
#Dela int på float blir det en float automatiskt



print(x)


