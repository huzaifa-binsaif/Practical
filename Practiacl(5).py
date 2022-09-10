a = ["banana", "apple", "mycrosoft"]
# if you want to print the items in the list above you can use this method:
print(a[0])
print(a[1])
print(a[2])
# or you can use this method which is less cumbersum
# this method means that do the following for the elements in the list of a
for element in a:
    print(element)
b = [20, 10, 5]
total = 0
for numbers in b:
    print(numbers)
    total = total + numbers
print (total)
# you can also print different items more then One time
for i in range(len(a)):
    for j in range(i + 1):
        # i = 0 -> j = 0
        # i = 1 -> j = 0, 1
        # i = 2 -> j = 0, 1, 2
        print (a[i])
# to create a long list for example, 1, 2, 3, 4 ....100; you can use the "range" function
# you can also make a list out of the ranges like this
c = list(range(1,100))
print (c)
total1 = 0
# the word i is the term we have chosen in place of elements
for i in c:
    print (i)
    total1 = total1 + i
print (total1)
# lets say we want a sum of the multiples of 3 in the range
#to do so we need to understand modulo operator "%" which gives us the remainder of a division
print(list(range (1,8)))
print (4 % 3)
print(5 % 3)
total2 = 0
for i in range(1, 8):
    if i % 3 == 0:
        total2 = total2 + i
print(total2)
# task: can you compute all the multiples of 3, 5
# that are less then 100
total3 = 0
for i in range(1, 100):
    if i % 3 == 0:
        total3 = total3 + i
print(total3)
total4 = 0
for i in range(1, 100):
    if i % 5 == 0:
        total4 = total4 + i
print(total4)
total5 = total3 + total4
print(total5)
# the error might be because your algorathm inclided numbers like 15 and 30, which are multiple of both 3 & 5, twice

# SOLUTION
total6 = 0
for i in range (1, 100):
    if i % 3 == 0:
        total6 += i
    elif i % 5 == 0:
        total6 += i
print (total6)
# you can skip some steps by doing this:
total7 = 0
for i in range (1,100):
    if i % 3 == 0 or i % 5 == 0:
        total7 += i
print (total7)
