#Q1
'''
class City:
    def __init__(self, city):
        self.city = city
        print(f"Welecome to {self.city}")

    def __del__(self):
        print(f"Thank you for visiting {self.city}")

c1 = City("Surat")
c2 = City("Ahemdabad")
c3 = City("Gandhinagar")

del c1
del c2 
del c3
'''

#Q2
'''
class Animal:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Name of the animal is: {self.name}")

name = input("Enter a name of an animal: ")

a = Animal(name)
a.display()
'''

#Q3
'''
class Rectangle:
    def __init__(self, l, w):
        self.length = l
        self.width = w

    def area(self):
        if self.length > 0 and self.width > 0:
            print(f"Area os rectangle is: {self.length * self.width}")
        else:
            print("Please enter positive values.")

length = int(input("Enter length of rectangle: "))
width = int(input("Enter width of rectangle: "))

r = Rectangle(length, width)
r.area()
'''

#Q4
'''
class Employee:
    def __init__(self):
        self.emid = int(input("Enter employee id: "))
        self.name = input("Enter employee name: ")
        self.age = int(input("Enter employee age: "))
        self.salary = int(input("Enter employee salary: "))

    def __del__(self):
        print(f"Goodbye {self.name} !! You done very good job for company.")

e = Employee()
del e
'''

#Q5
'''
class Student:
    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        print("\nStudent details:")
        print(f"Name : {self.name} \nRoll_No. : {self.roll_no} \nMarks : {self.marks}")

    def grade(self):
        if self.marks >= 90:
            print("Grade : A")

        elif self.marks >= 80:
            print("Grade : B")

        elif self.marks >= 70:
            print("Grade : C")

        elif self.marks >= 60:
            print("Grade : D")

        else:
            print(f"Student {self.name} has very less marks.")

name = input("Enter name of student: ")
roll_no = int(input("Enter roll number of student: "))
marks = int(input("Enter marks of the student: "))

s = Student(roll_no, name, marks)
s.display()
s.grade()
'''