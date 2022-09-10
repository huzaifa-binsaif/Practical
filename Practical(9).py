# this is an example of two different classes and objects intracting with each other
#the intraction can be done in two ways:
# 1. through adding another argument in the constructor
# 2. just through assigning the robot to the human
class Robot:
    def __init__(self, name, colour, age):
        self.name = name
        self.colour = colour
        self.age = age
    def self_introduction(self):
        print ("Robot")
        print ("My name is " + self.name)
        print ("My favorate colour is " + self.colour)
        print ("I am " + self.age + " years old")
        print ("")
r1= Robot("Tom", "Red", "30")
r2= Robot("Lena", "Orange", "22")
class Human:
    def __init__(self, n, p, i ):
        self.name = n
        self.personality = p
        self.present = i
    def is_present(self):
        self.present = True
    def isnt_present(self):
        self.present = False

    def self_profile(self):
        print("Human")
        print ("student name: " + self.name)
        print ("Personality: " + self.personality)
        if self.present == True:
            print ("Atendance: Present")
        else:
            print ("Atendance: Absent")
        print ("")

h1= Human("Lena", "Anoying", True)
h2= Human("Moira", "Creative", False)

h1.robot_owned = r2
h2.robot_owned = r1
h1.self_profile()
h1.robot_owned.self_introduction()
h2.self_profile()
h2.robot_owned.self_introduction()
