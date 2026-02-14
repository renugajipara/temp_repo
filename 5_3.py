#Q1(single Inheritance)
'''
class A:
    def display(self):
        print("You are in parent class")

class B(A):
    pass

obj = B()
obj.display()
'''

#Q2(Multiple Inheritance)
'''
class Teacher:
    pass

class Administrator:
    pass

class Headmaster(Teacher, Administrator):
    pass
    
h = Headmaster()
'''

#Q3(Multilevel Inheritance)
'''
class Grand_Parent():
    def grd(self):
        print("This is grand parent class")
class Parent(Grand_Parent):
    def par(self):
        print("This is parent class")
class Child(Parent):
    def cld(self):
        print("This is ckild class")

obj = Child()
obj.grd()
obj.par()
obj.cld()
'''

#Q4(Heirarchical Inheritance)
'''
class Animal():
    def main(self):
        print("This is animal")

class Dog(Animal):
    def voice(self):
        print("Dog is barking")

class Cat(Animal):
    def drink(self):
        print("Cat is drinking milk")

obj = Dog()
obj1 = Cat()

obj.main()
obj.voice()
obj1.main()
obj1.drink()
'''

#Q5(Hybrid Inheritance)
'''
class A:
    def show(self):
        print("Class A")

class B(A):         
    def show(self):
        super().show()
        print("Class B")

class C(A):          
    def show(self):
        super().show()
        print("Class C")

class D(B, C):    
    def show(self):
        super().show()
        print("Class D")

obj = D()
obj.show()
'''

#Q6(Type of Objects)
'''
class Student:
    pass

class Car(Student):
    pass

s1 = Student()   
c1 = Car()       

print(type(s1))
print(type(c1))
'''

#Q7(List all atrributs and methods of class)
'''
class Student:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(self.name)

print(dir(Student))
'''

#Q8(Ckeck whether the the object is instance of a class or not)
'''
class Car:
    pass

obj1 = Car()
bj = Car()

print(isinstance(obj1, Car))
print(isinstance(bj, Car))
'''

#Q9(To retrieve documentation string of an object)
'''
class Demo:
    pass

    def show(self):
        print("Hello")

help(Demo)
'''