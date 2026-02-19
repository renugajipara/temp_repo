#Q1
'''
class Person:
    name = None
    age = None

    def display(self, name, age):
        print(f"Name of person is {name} and age {age}")

p = Person()
r = Person()

p.display("Rensee", 21)
r.display("Nely", 20)
'''

#Q2
'''
class counter:
    count = 0 

    def increament(self):
        self.count += 1

    def display(self):
        print(f"Increamented count: {self.count}")

c = counter()
c.increament()
c.increament()
c.increament()
c.increament()
c.increament()
c.display()
'''

#Q3
'''
class demo:
    def demo1(self):
        print("Hello")

d = demo()
d.demo1()
'''

#Q4
'''
class Book:
    __title = None
    __author = None

    def __init__(self, title, author):
        self.__title = title
        self.__author = author

    def display(Self):
        print(f"Title of the book is: {Self.__title}")
        print(f"Author of the book is: {Self.__author}")

b = Book("wings of fire", "APJ Abdul Kalam")
b.display()
'''

#Q5
'''
class Account:
    def __init__(self, balance):
        self.__balance = balance

    def deposit(self, d_amount):
        if d_amount >= 0:
            self.__balance += d_amount
            print(f"Balance after diposit: {self.__balance}")
        else:
            print("Deposited amount must be Positive.")

    def withdraw(self, w_amount):
        if w_amount <= 0:
            print("Withdrawal amount must be Positive.")

        elif w_amount > self.__balance:
            print("Insufficient blance in your account.")

        else:
            self.__balance -= w_amount
            print(f"Balance after withdrawal: {self.__balance}")

    def display(self):
        print(f"Total balance : {self.__balance}")

balance = float(input("How many balance you have right now in your account?: "))
d_amount = float(input("How many amount you want to deposit in your account?: "))
w_amount = float(input("How many amount you want to withdraw in your account?: "))

a = Account(balance)
a.deposit(d_amount)
a.withdraw(w_amount)
a.display()
'''

#Q6
'''
class Age_Checking:
    def __init__(self, age):
        self.age = age
       
    def getdata(self):
        if self.age <= 0:
            print("Please enter valid age.")
       
        else:
            print("Age of a person is: ", self.age)
           
user = int(input("Enter Age: "))
a = Age_Checking(user)
a.getdata()
'''

#Q7
'''
class Student:
    def __init__(self, name, maths, physics, chemistry):
        self.__name = name
        self.__maths = maths
        self.__physics = physics
        self.__chemistry = chemistry

    def average(self):
        self.avg = (self.__maths + self.__physics + self.__chemistry) / 3
        print(f"Average of three subject is: {self.avg}")
        return self.avg
    
    def grade(self):
        avg = self.average()

        if avg > 90:
            print("Grade of student is 'A'")

        elif avg <= 90 and avg > 80:
            print("Grade of student is 'B'")

        elif avg <= 80 and avg > 70:
            print("Grade of student is 'C'")

        elif avg <= 70 and avg > 60:
            print("Grade of student is 'D'")

        else:
            print("Student has very less marks...")

name = input("Enter student name: ")
maths = int(input("Enter the marks of the subject maths: "))
physics = int(input("Enter the marks of the subject physics: "))
chemistry = int(input("Enter the marks of the subject chemistry: "))

s = Student(name, maths, physics, chemistry)
s.grade()
'''