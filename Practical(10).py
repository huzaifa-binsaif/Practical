# you can find the type of an item by using the type() function which defines the type
print(type("lena"))
print(type(4))
print(type(True))
# you can use the boleen valuse to determin if someting is true or false
a = 1
b = 5
c = 7
d = 0
if a < b:
    print ("b is greater than a")
if True:
    print ("b is greater than a")
# you can store the booleen value in variables
boolean_value = a < b
print (boolean_value)
if boolean_value:
    print ("b is greater than a")
# you can use the boolean values in complex functions like below
def Are_you_sad(is_rainy, have_umbrella):
    if is_rainy == True and have_umbrella == False:
        return True
        print ("I am sad")
    else:
        return False
        print("I am not sad")
print(Are_you_sad(True, False))
print(Are_you_sad(False, True))
print(Are_you_sad(True, True))
print(Are_you_sad(False, False))
# task: define c if c is greater than d + e
def Number_cde(c,d,e):
    if c > d + e:
        return True
    else:
        return False
print(Number_cde(8,2,4))
