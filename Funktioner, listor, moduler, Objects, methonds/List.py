# List comprehension = A concise way to create lists in python
#                      Compact and eisier to read then traditional loops

#                      [Expression for value in iterable if condition]


# doubles = []
# for x in range(1, 11):
#     doubles.append(x * 2)

# print(doubles)

# Jobbigt och svårt att läsa



# doubles = [Expression for value in iterable if condition]


# doubles = [x * 2 for x in range(1, 11)]

# print(doubles)



# Exercices

#Gångra med 3
# triples = [x * 3 for x in range(1, 11)]
# print(triples)

#Square
# squares = [x**2 for x in range(1, 11)]
# print(squares)


#Fruits
# fruits = ["apple", "orange", "banana", "pinapple"]
# fruits = [fruit.upper() for fruit in fruits]

# print(fruits)


#Hitta första bokstaven i vrje fruit
# fruits = ["apple", "orange", "banana", "pinapple"]
# fruitschars = [fruit[0] for fruit in fruits]

# print(fruitschars)



#Numbers
# numbers = [1, -2, 3, -4, 5, -6]
# numberspositive = [negative for negative in numbers if negative >= 0]
# numbersnegative = [negative for negative in numbers if negative <= 0]
# print(numberspositive)
# print(numbersnegative)






