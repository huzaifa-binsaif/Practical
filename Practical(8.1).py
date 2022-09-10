# Insted of doing it with a lot of def and functions, you can do it with a constructor
# you can create a custom constructor by using the function "__init__"
class Robot:
    def __init__(self, name, colour, age):
        self.name = name
        self.colour = colour
        self.age = age
    def introduce_self(self):
            print ("my name is "+ self.name )# self is this in java
    def introduce_self1(self):
                print ("my favorate colour is "+ self.colour)
    def introduce_self2(self):
                print ("I am " + self.age + " years old")
                print ("")

r1= Robot("Tom", "Red", "30")
r2= Robot("Lena", "Orange", "22")
r1.introduce_self()
r1.introduce_self1()
r1.introduce_self2()

r2.introduce_self()
r2.introduce_self1()
r2.introduce_self2()
