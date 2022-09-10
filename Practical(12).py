# Now we will learn about sets in python
# A set is a type of data thata stores things
a = set()
print (a)
# you can us .add to add things in the set
a.add(1)
print(a)
a.add(2)
print(a)
# if you try to add the same item in the set twicw it wont be added
# you can use this to iterate
for x in a:
    print (x)
# what if you want to remove duplicates from a list? you can do it like this
given_list = [1,1,2,4,2]
new_set1 = set()
for x in given_list:
    new_set1.add(x)
# you can create a lsit out a set by doing this
print (new_set1)
newlist1 = list()
for x in new_set1:
    newlist1.append(x)
print (newlist1)
# you can add strings and integers in a set
b = set()
b.add("apple")
b.add("banana")
b.add(1)
print (b)
# here is a task, find the sum of the unique elements in the given_list
given_list1 = [1,3,4,1,3]
newset = set()
newlist = list()
total = 0
for x in given_list1:
    newset.add(x)
print(newset)
for x in newset:
    newlist.append(x)
print (newlist)
for x in newlist:
    total = total + x
print (total)
# you can use a shortcut by applying the end sum() function
# Solution
print ("Solution:-")
for x in given_list1:
    newset.add(x)
print(sum (newset))
# or
given_list1 = [1,3,4,1,3]
newset = set()
for x in given_list1:
    newset.add(x)
print(newset)
total1 = 0
for x in newset:
    total1 += x
print (total1)
