# Object = A "bundle" of related attributes (Variables) and methonds (functions)
#          Ex. phone, cup, book
#          You need a class to create many objects
# 
# 
# Method != Function (Method = Function inside an object)

# Class = (blueprint) used to design the structure and layout of an object



class Car:
    def __init__(self, model, year, color, for_sale):
        self.model = model
        self.year = year
        self.color = color
        self.for_sale = for_sale

    def drive(self):
        print(f"You drive the {self.model}")
    def stop(self):
        print(f"You stoped the {self.color} {self.model}")


car1 = Car("Tesla", 2024, "Silver", False)
car2 = Car("Audi", 1990, "Green", True )
car1.stop()

print(car1.year, car1.color, car1.for_sale, car1.model)
print(car2.color, car2.for_sale, car2.model, car2.year)




# Class variables = Shared among all intances of a class
#                   Defined outside the constructor
#                   Allow you to share data among all onjects created from a class


print("")
class Student:

    class_year = 2024
    num_students = 0

    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

        Student.num_students = Student.num_students + 1





student1 = Student("Oliver", 16, "B")
student2 = Student("Pyp", 168, "A")
student3 = Student("Jossi", 22, "A")
student4 = Student("Tården", 51, "B")





print("")

print(f"Det går {Student.num_students} elever i klassen")

print("")

# Egen for loop och list
studentlist = [student1, student2, student3, student4]
for student_print in studentlist:
    print(student_print.name)
    print(student_print.age)
    print(student_print.grade)
    print(Student.class_year)

    print("")







    # Inheretace = Allow a class to inherit attributes and methods from another class
    #              Helps with ode reusability and extensibility
    #              class Child(Parent)


class Animal:
    def __init__(self, name):
        self.name = name
        self.isalive = True
        self.isssleeping = True
    
    def eat(self):
        print(f"{self.name} is eating")
    
    def sleept(self):
        print(f"{self.name} is sleeping")

class Dog(Animal):
    def speak(self):
        print("TUT!!!")

class Cat(Animal):
    def speak(self):
        print("Mjau!!!")

class Marsvin(Animal):
    def speak(self):
        print("Pip!!!")

dog = Dog("Stellan")
    


cat = Cat("Musse")

marsvin1 = Marsvin("Lillen")

marsvin2 = Marsvin("Teddy")



print(dog.name)
dog.eat()
dog.sleept()
dog.speak()

print("")
print(cat.name)
cat.eat()
cat.sleept()
cat.speak()

print("")
print(marsvin1.name)
marsvin1.eat()
marsvin1.sleept()
marsvin1.speak()

print("")
print(marsvin2.name)
marsvin2.eat()
marsvin2.sleept()
marsvin2.speak()


# Multiple inheritance = inherit from more than one parent class
#                        C(A, B)

# multilevel inheritance = inherit from at parentwhich inherits from another parent
#                          C(B) <- B(A) <- A



print("")

class Prey:
    def flee(self):
        print("This animal is fleeing")
class Predetor:
    def hunt(self):
        print("This animal is hunting")


class Rabbit(Prey):
    pass

class Hawk(Predetor):
    pass

class Fish(Predetor, Prey):
    pass


rabbit = Rabbit()

hawk = Hawk()

fish = Fish()


rabbit.flee()

hawk.hunt()

fish.flee()

fish.hunt()


print("")


#Multilevel

class Animal():

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")
    def sleep(self):
        print(f"{self.name} is sleeping")



class Prey(Animal):
    def flee(self):
        print(f"{self.name} is fleeing")
class Predetor(Animal):
    def hunt(self):
        print(f"{self.name} is hunting")


class Rabbit(Prey):
    pass

class Hawk(Predetor):
    pass

class Fish(Predetor, Prey):
    pass


rabbit = Rabbit("Tony")

hawk = Hawk("James")

fish = Fish("Fishy")


rabbit.flee()
rabbit.sleep()

hawk.hunt()
hawk.eat()

fish.flee()

fish.hunt()


print("")






# super() = Function used in a child class to call methonds from parent class (Superclass)
#           Allows you to extend the functionality of the inherited methond


class Shape:
    def __init__(self, color, filled):
        self.color = color
        self.filled = filled

    def describe(self):
        print(f"it is {self.color}")   


class Circle(Shape):
    def __init__(self, color, filled, radius):
        super().__init__(color, filled)
        self.radius = radius

    

class Square(Shape):
    def __init__(self, color, filled, width):
        super().__init__(color, filled)
        self.width = width



class Triangle(Shape):
    def __init__(self, color, filled, width, height):
        super().__init__(color, filled)
        self.width = width   
        self.height = height

    def describe(self):
        print(f"it is an Triangle with the area {self.width*self.height/2}") #If the child has a simelor method as a parent the childs methond will be used
        super().describe

circle = Circle("red", True, 5)
print(circle.color)
print(circle.filled)
print(circle.radius)

square = Square("blue", False, 10)
print(square.color)
print(square.filled)
print(square.width)

triangle = Triangle("yellow", True, 7, 3)
print(triangle.color)
print(triangle.filled)
print(triangle.width)
triangle.describe()

print("")







# Mehtond overriding

class Animal:
    def eat(self):
        print("Is eating")
class Rabbit(Animal):
    def eat(self):
        print("Rabbit is eating")

rabbit = Rabbit()
rabbit.eat()


#Den kommer använda en metod som är närmre aassosierad med sig själv innan den tar en method från en parent



