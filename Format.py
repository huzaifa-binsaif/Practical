#def OddDigits():
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
   newnum= num -1
   print("the updated number is", newnum)
else:
   print("{0} is Odd".format(num))