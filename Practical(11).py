# this time we are doing list comprehensions
a = [1, 3, 5, 7]
# if you wanted to multiply each number into the list by 2 to make it a = [2,6,10,14,18,22]
# you can use the .append function
a.append(9)
a.append(11)
print (a[5])
print (a)
# you can do it by using the for loop
c = []
for x in a:
    c.append(x * 2)
# you can also write is as c = [x * 2 for x in a]
print(c)
# you can even comprehend ranges into a list
d = []
for x in range(1,7):
    d.append(x ** 2)
# you can write this as d = [x ** 2 for x in range(1,7)]
print(d)
# task create a lsit of [36, 25, 16, 9, 4, 1]
# 1.
e1 = []
for x in range (-6,0):
    e1.append(x ** 2)
print(e1)
# 2.
e2 = [x ** 2 for x in range(-6,0)]
print(e2)
print ("")

# Solution:-
print ("Solution:-")
range (6 , 0 , -1)
# this means that the range starts at 6 and ends at 0 but not including 0, and instes of going up by 1 we go down by 1
# 1.
f1 = []
for x in range(6, 0, -1):
    f1.append(x ** 2)
print (f1)
f2 = [x ** 2 for x in range (6,0,-1)]
print (f2)
