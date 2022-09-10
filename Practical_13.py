class Employee:
    raise_amount = 1.04
    num_of_employees = 0
    def __init__(self,firstname,lastname,salary):
        self.firstname = firstname
        self.lastname = lastname
        self.email = firstname +'.'+ lastname + '@overwatch.com'
        self.salary = salary
        self.fullname = '{} {}'.format(self.firstname, self.lastname)

        Employee.num_of_employees += 1
    def Employee_Profile(self):
        print (self.fullname)
        print (self.email)
        print (self.salary)
        print ("")
    def apply_raise(self):
        raise_apply = int(self.salary * self.raise_amount)
        print(raise_apply)
        print ("")
    # this is how you uses @classmethod
    @classmethod
    # cls means class
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount
# by using the split function, you saperated the string into three different inputs when the hiphen '-' was removed
    @classmethod
    def from_string(cls, emp_string):
        firstname, lastname, salary = emp_string.split('-')
        return cls(firstname, lastname, salary)
    # to create the static method you can use '@staticmethod' decorator
    @staticmethod
# one way to tell if the static method is to be used, check if the class variable or the instance variable is making sence
# if not; you can then use the ststicmethod
    def work_day(day):
        # python has a built in weekday system in which monday = 0 and sinday=6
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True
# you can inherite and function from one class to another by using '()' and the class
class Developer(Employee):
    # we can simply change an instance like raise_amount (x) and that value of raise is applied to the seveloper subclass
    raise_amount = 10
    def __init__(self,firstname,lastname,programing_lang,salary):
        # insted of copping and pasting the whole code of self you can let the program inherate the commen things and only focus on p.l
        # you can do that by using super().__init__(x y z)
        super().__init__(firstname,lastname,salary)
        self.programing_lang = programing_lang
    def Developer_Profile(self):
        print (self.fullname)
        print (self.email)
        print (self.salary)
        print (self.programing_lang)
        print (self.apply_raise)
        print ("")
class Manager(Employee):
    raise_amount = 13
    def __init__(self,firstname,lastname,qulification,salary,employees=None):
        super().__init__(firstname, lastname, salary)
        self.qulification = qulification
        self.email = firstname + '.' + lastname + '@Dota2.com'
        if employees is None:
            self.employees = []
        else:
        # you should never leave a list empty
            self.employees = employees
    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)
    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)
    def print_emp(self):
        for emp in self.employees:
            print (emp.fullname())
    def Manager_Profile(self):
        print (self.fullname)
        print (self.email)
        print (self.salary)
        print (self.qulification)
        print (self.apply_raise)
        print ("")

dev_1 = Developer('Brigetta', 'Lindhoim','Python', 120000)
dev_2 = Developer('Ana', 'Amari','C++', 150000)
dev_1.Developer_Profile()
print(dev_1.salary)
dev_1.apply_raise()
dev_2.Developer_Profile()

man_1 = Manager('Sky', 'Wrath', 'Mage', 7000000, [dev_1])
man_1.Manager_Profile()
print(man_1.print_emp)

emp_1 = Employee('Scott','Mccall',25000)
emp_2 = Employee('Lena','Oxton',100000)
emp_1.Employee_Profile()
emp_1.apply_raise()
emp_2.Employee_Profile()
emp_2.apply_raise()
# to find out the whole class info of an object you can use the __dict__ function
# it will print out the whole informatoin of a given object
print (emp_1.__dict__)
print (Employee.__dict__)
# you can change a give instance of a class by doing this because of them being eather maliable or constantly changing
Employee.raise_amount = 1.05
print(Employee.raise_amount)
print ("")
# but you can alse change the instance for a specific object as well
emp_1.raise_amount = 1.06
print (emp_1.__dict__)
print (emp_1.raise_amount)
print (Employee.raise_amount)
print (emp_2.raise_amount)
# you can create instances that apply to the whole class and have no meaning if applied to self
print (Employee.num_of_employees)
# now we will do regular methods, class methods and ststic methods
# the regular method takes the instance as an argument and follows through whereas a class method takes the whole class as the argument
# and the ststic method takes nothing for an argument
# you use the class method decorator @classmethod the create a class method
# but it dosn't override the instance argument that was prevously provided
Employee.set_raise_amt(5)
print (Employee.raise_amount)
print (emp_1.raise_amount)
print (emp_2.raise_amount)
# you can also use the instance variables insted of the calss variables to get the same result
emp_1.set_raise_amt(1.07)
print (Employee.raise_amount)
print (emp_1.raise_amount)
print (emp_2.raise_amount)
# again it dosn't afect the instance cammand given before
print ("")
# you can use class methods as indivisual constructiors
# lets say that there are three strings saperated with hiphens '-'
# you have to remove the hipons before entering the data in the function
# you can solve that buy using the classmethod
emp_string_1 = 'Amelie-Lacroix-60000'
emp_string_2 = 'Hana-Song-75000'
emp_string_3 = 'Pharah-Amari-55000'
# now you can use the class method function to split the string and crate a valid variable
new_emp_string_1 = Employee.from_string(emp_string_1)
new_emp_string_2 = Employee.from_string(emp_string_2)
new_emp_string_3 = Employee.from_string(emp_string_3)
new_emp_string_1.Employee_Profile()
new_emp_string_2.Employee_Profile()
new_emp_string_3.Employee_Profile()
# now we will learn about static methods
# the static methods dont pass anything predetermenetly like class or instance
# we have to input the required values
# there is a a datetime madule thet you can uses to create a datetime related  function
import datetime
my_date = datetime.date(2016, 7, 4)
# to check if its a workday you can just print it like this
print (Employee.work_day(my_date))
my_date1 = datetime.date(2018, 8, 24)
print (Employee.work_day(my_date1))
my_date2= datetime.date(2019, 12, 21)
print (Employee.work_day(my_date2))
# now we will do class inheritance which helps you inherite certain atributes from the class
# this is good because you can use it to create alternate subclasses
# we can create subclasses like developer and manager to get a better understanding
# one really usefull function is the help function
# just write print (help(class or subclass))
# lets say that each developer has his own programing equation, this requires 4 inputs in the init function
# so we can create a sapetrate function for the subclass "Developer"
