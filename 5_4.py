#Q1
'''
def add(a, b):
    return a+b

n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
print(f"Adition of two number is: {add(n1,n2)}")

s1 = input("Enter a string: ")
s2 = input("Enter a string: ")
print(f"Concatenation of two string: {add(s1, s2)}")
'''

#Q2
'''
class Shape:
    def area(self):
        print("Every shape has it's own area.")

class Circle(Shape):
    def area(self,r):
        print(f"Area of circle is: {3.14*r*r}")

class Rectangle(Shape):
    def area(self, l, w):
        print(f"Area of rectangle is: {l*w}")

radius = int(input("Enter the radius of circle: "))
length = int(input("Enter the length of rectangle: "))
width = int(input("Enter the width of rectangle: "))

s = Shape()
c = Circle()
r = Rectangle()

s.area()
c.area(radius)
r.area(length, width)
'''

#Q3
'''
s = input("Enter a string: ")
print(f"Length of string is: {len(s)}")

l = [20, 21, 22, 23, 35, 25]
print(f"Length of list is: {len(l)}")

d = {"name": "Renu", "age": 20, "course": "AI/ML"}
print(f"Length of Dictionary is: {len(d)}")
'''

#Q4
'''
class Transport:
    def travel(self):
        pass

class Train(Transport):
    def travel(self):
        print("You are in train")
    
class Plane(Transport):
    def travel(self):
        print("You are in plane")

t = Train()
p = Plane()

t.travel()
p.travel()
'''

#Q5
'''
class Calculator:
    def multiply(self, a=1, b=1, *args):
        result = a*b
        for i in args:
            result *= i
        return result
    
c = Calculator()
print(c.multiply(3, 4))
print(c.multiply(3, 4, 6))
print(c.multiply())
'''

#Q6
'''
class Animal:
    def speak(self):
        print("Any animal can speak...")

class Dog(Animal):
    def speak(self):
        print("Dog is barking...")

class Cat(Animal):
    def speak(self):
        print("Cat is meow...")

a = Animal()
d = Dog()
c = Cat()
a.speak()
d.speak()
c.speak()
'''

#Q7
'''
class Shape:
    pi = 3.14
    def area(self):
        print("Every shape has it's own area.")

class Circle(Shape):
    @classmethod
    def area(cls, r):
        print(f"Area of circle is: {cls.pi*r*r}")

class Rectangle(Shape):
    @staticmethod
    def area(l, w):
        print(f"Area of rectangle is: {l*w}")

radius = int(input("Enter the radius of circle: "))
length = int(input("Enter the length of rectangle: "))
width = int(input("Enter the width of rectangle: "))

s = Shape()
s.area()
Circle.area(radius)
Rectangle.area(length, width)
'''

#Q8
'''
class Vehicle:
    def Start(self):
        print("Every Vehicles can start with it's own method.")

class Bike(Vehicle):
    def Start(self):
        print("Bike is start with kick...")

class Car(Vehicle):
    def Start(self):
        print("Car is start with push button...")

a = Vehicle()
d = Bike()
c = Car()
a.Start()
d.Start()
c.Start()
'''

#Q9
'''
class Printer:
    def Print(self, *args):
        if isinstance(args[0], int):
            print(f"Integer:{args}")

        elif isinstance(args[0], str):
            print(f"String: {args}")

        else:
            print("Invalid input...")

p = Printer()
p.Print("hello")
p.Print(1, 2, 3)
'''

#Q10
'''
class Person:
    pass

class Student(Person):
    pass

print(f"Student is subclass of Person?? -->>  {issubclass(Student, Person)}")
'''

#Q11
'''
class Employee:
    def __init__(self, emid, name, age, salary):
        self.emid = emid
        self.name = name
        self.age = age
        self.salary = salary

class Manager(Employee):
    def __init__(self, emid, name, age, salary, department):
        super().__init__(emid, name, age, salary)
        self.deptartment = department

    def getdata(self):
        print(f"Employee_Id : {self.emid}, Name : {self.name}, Age : {self.age}, salary : {self.salary}, Department : {self.deptartment}")

emid = int(input("Eneter employee id: "))
name = input("Enter a name: ")
age = int(input("Eneter employee age: "))
salary = int(input("Eneter employee salary: "))
department = input("Enter a department: ")

m = Manager(emid, name, age, salary, department)
m.getdata()
'''

#Q12
'''
class grandparent:
    pass

class parent(grandparent):
    pass

class child(parent):
    pass

print(f"Child is subclass of Parent?? -->> {issubclass(child, parent)}")
print(f"Parent is subclass of Grandparent?? -->> {issubclass(parent, grandparent)}")
print(f"Child is subclass of Grandparent?? -->> {issubclass(child, grandparent)}")
'''

#Q13
'''
class Base:
    def display(self):
        print("This is base class...")

class Derived(Base):
    def display(self):
        super().display()
        print("This is derived class...")

d = Derived()
d.display()
'''

#Q14
'''
class User:
    def __init__(self, userid, name):
        self.userid = userid
        self.name = name

class Admin(User):
    def __init__(self, userid, name):
        super().__init__(userid, name)
    
    def display(self):
        print(f"User_Id : {self.userid}, User Name : {self.name}")

userid = int(input("Enter user id: "))
name = input("Enter user name: ")
a = Admin(userid, name)
a.display()
'''