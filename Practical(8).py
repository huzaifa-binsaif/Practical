# okay now we are going to get a bit advanced
# we are going to learn about classes and objects
# we will first add the name,colour and weight of the robot and a function for introduction
class Robot:
    def introduce_self(self):
        print ("my name is "+ self.name )# self is this in java
    def introduce_self1(self):
            print ("my favorate colour is "+ self.colour)
    def introduce_self2(self):
            print ("I am " + self.age + " years old")
            print ("")
r1= Robot()
r1.name = "Tom"
r1.colour = "Red"
r1.age = "30"

r2= Robot()
r2.name ="Lena"
r2.colour ="Orange"
r2.age = "22"
r1.introduce_self()
r1.introduce_self1()
r1.introduce_self2()

r2.introduce_self()
r2.introduce_self1()
r2.introduce_self2()
