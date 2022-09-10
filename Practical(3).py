# a collection of code
def function1():
    print ("wow")
    print ("amazing")
print ("this is outside of function1")
function1()
# a mapping tool
def function2(x):
    return 2*x
# retrn value or output
a = function2(5)
print (a)
b = function2(7)
print (b)
def function3(y,x):
    return x + y
c = function3(4,9)
print (c)
def function4(z):
    print (z)
    print ("the value of has been doubled")
    return 2*z
f = function4(7)
print (f)
#remember its not nessecery to use the term "function" everytime, get creative
def function5(some_argument):
    print (some_argument)
    print ("weee")
function5(9)

#task: convert miles into kelometers
def convert(mile):
    km = 1.6 * mile
    return km
km1 = convert(80)
print(km1)
