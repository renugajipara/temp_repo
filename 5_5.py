from abc import ABC, abstractmethod
#Q1
'''
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class Circle(Shape):
    def area(self,r):
        print(f"Area of circle is: {3.14*r*r}")

class Rectangle(Shape):
    def area(self, l, w):
        print(f"Area of rectangle is: {l*w}")

radius = int(input("Enter the radius of circle: "))
length = int(input("Enter the length of rectangle: "))
width = int(input("Enter the width of rectangle: "))

c = Circle()
r = Rectangle()

c.area(radius)
r.area(length, width)
'''

#Q2
'''
class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def perimeter(self, r):
        self.r = r

    def area(self):
        print(f"Area of circle is: {3.14*self.r*self.r}")

class Rectangle(Shape):
    def perimeter(self, l, w):
        self.l = l
        self.w = w

    def area(self):
        print(f"Area of rectangle is: {self.l*self.w}")

radius = int(input("Enter the radius of circle: "))
length = int(input("Enter the length of rectangle: "))
width = int(input("Enter the width of rectangle: "))

c = Circle()
r = Rectangle()

c.perimeter(radius)
r.perimeter(length, width) 

c.area()
r.area()

# class new(Shape):
#     def perimeter(self):
#         print("This is for trial purpose...")

# n = new()
# n.perimeter()

#TypeError: Can't instantiate abstract class new without an implementation for abstract method 'area'
'''

#Q3
'''
class MLModel(ABC):
    @abstractmethod
    def train(self):
        pass
    
    @abstractmethod
    def predict(self):
        pass

class LinearRegressionMoodel(MLModel):
    def train(self):
        print("This is training phase of Linear Regression model")

    def predict(self):
        print("This is predicting phase of Linear Regression model\n")

class DecisionTreeModel(MLModel):
    def train(self):
        print("This is training phase of Decision Tree model")
    
    def predict(self):
        print("This is predicting phase of Decision Tree model")

models = [LinearRegressionMoodel(), DecisionTreeModel()]

for i in models:
    i.train()
    i.predict()
'''

#Q4
    
class Account(ABC):
    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass

class BankAccount:
    def __init__(self, account_number, balance):
        __account_number = account_number
        __balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"New balance is : {self.__balance}")
        else: 
            print("Invalid amount...")

    def widthraw(self, amount):
        if amount < self.__balance:
            self.__balance -= amount
            print(f"Remaing balance is : {self.__balance}")
        else:
            print("Please check your balance...")

    def get_balance(self):
        return self.__balance
    
class SavingAccount(BankAccount, Account):
    def __init__(self, account_number, balance, intrest_rate):
        super().__init__(account_number, balance)
        self.intrest_rate = intrest_rate

    def add_intrest(self):
        intrest = self.get_balance() * self.intrest_rate / 100
        self.deposit(intrest)
        print(f"{intrest} intrest added.")

class CurrentAccount(BankAccount, Account):
    def __init__(self, account_number, balance, limit):
        super().__init__(account_number, balance)
        self.limit = limit

    def widthraw(self, amount):
        if amount <= self.get_balance():
            super().widthraw(amount)
        else:
            shortfall = amount - self.get_balance()
            super().withdraw(self.get_balance()) 
            print(f"Overdraft used: ${shortfall}.")
            print("Transaction Successful.")

print(f"{"="*20} Bnak Account Management System {"="*20}")

account = []

for i in account:
    i.deposit()
    i.withdraw()
    i.get_balance()