# this block states that, the numbers in the range have to be added and the total is then formed
# to add all the numbers in a range of numbers you can use "+=" which means add and equate
# this example is a "for" loop
total = 0
for i in range (1, 5):
    total += i
print (total)
# This example is of an "while" loop
total1 = 0
j = 1
while j < 5:
    total1 += j
    j += 1
print (total1)
# A "while" loop can help when you don't know how many loops you need, like for example:
# Find the sum of the postive numbers
given_list = [5,4,4,3,1,-2,-3,-5]
total2 = 0
i = 0
while given_list[i] > 0:
    total2 += given_list[i]
    i += 1
print (total2)
# if the range is only made up of positive numbers then there eill be an error because the loop will reach the end of the
# that is because the loop will reach the end of the range and will have no further items to increminate to
# to solve the above we can design the algorathim in a slightly different way
given_list = [5,4,4,3,1]
total2 = 0
i = 0
while i < len(given_list) and given_list[i] > 0:
    total2 += given_list[i]
    i += 1
print (total2)
# You can also use the "break" statement which commands the loop to be broken when it reaches a serten point
given_list1 = [5,4,4,3,1,-2,-3,-5]
total3 = 0
for element in given_list1:
    if element <= 0:
        break
    total3 += element
print (total3)
# same thing but with the while loops
# A "True" statement is always true
total4 = 0
i = 0
while True :
    total4 += given_list1[i]
    i += 1
    if given_list1[i] <= 0:
        break
print (total4)
# given_list2 = [7,5,4,4,3,1,-2,-3,-5,-7]
# find the sum of all the negative numbers
given_list2 = [7,5,4,4,3,1,-2,-3,-5,-7]
total5 = 0
i = 6
while i < len(given_list2) and given_list2[i] < 0:
    total5 += given_list2[i]
    i += 1
print (total5)

# SOLUTION
given_list3 = [7,5,4,4,3,1,-2,-3,-5,-7]
total6 = 0
j = len(given_list3) - 1
while given_list3[j] < 0:
    total6 += given_list3[j]
    j -= 1
print (total6)
