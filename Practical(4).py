# A list is a collection of values
a = [1, 9, -10]
print (a)
# append is a predefined term and the . is normally used with it insted of a = or -
# the append function is used to add a number or code to your list
a.append(7)
print (a)
a.append("hello world")
print (a)
# a prexisting list can also contain another list within it
a.append([1, 2])
print (a)
# If you are to delete a number or code from a lsit you use pop
# pop is also a predefined term, and it is used to remove items form the list
# pop removes to very latest item added to the list
a.pop()
print (a)
a.pop()
print (a)
# if you want to retreve an item remember that in every programing language...
# the first item has the value 0
print (a[0])
print (a[3])
# if you want to change the value of an item, you can do it as follows:
a[0] = 100
print (a)
# task: swap the value of item 0 with item 2
b = ["banana", "apple", "mycrosoft"]
print(b)
temp = b[0]
b[0] = b[2]
b[2] = temp
print (b)
# there is also a shortcut of doing this
b[0], b[2] = b[2], b[0]
print(b)
