#Q1
'''
l = [1,5,8,34,29,63,91,78]

length = len(l)
maximum = max(l)
sort = sorted(l)
add = sum(l)
tp = type(l)
print(f"Length of list is {length}")
print(f"Maximum of list is {maximum}")
print(f"Sorted list is {sort}")
print(f"addition of list is {add}")
print(f"Type of list is {tp}")
'''

#Q2
'''
def fact():
    n = int(input("Enter a number: "))
    f = 1
    for i in range(n, 0, -1):
        f = f*i
    print(f"Factorial of given number is: {f}")
fact()
'''

#Q3
'''
def sqr():
    l = []
    
    n = int(input("Enter total number of element: "))
    for i in range(n):
        ele = int(input("Enter a number you want to enter: "))
        l.append(ele)
    print(l)
    l2 = []
    for i in l:
        l2.append(i ** 2)
    print(l2)
sqr()
'''

#Q4
'''
def frequency():
    freq = {}
    string = input("Enter a String : ")
    for i in string:
        if i in freq:
            freq[i] += 1

        else:
            freq[i] = 1
    return freq

print(frequency())
'''

#Q5
'''
def cube(l):
    lst = []
    for i in l:
        lst.append(i ** 3)
    return lst
    
l = []
n = int(input("Enter how many ele you want in list: "))
for i in range(n):
    l.append(int(input("Enter ele: ")))

print(l)
print(cube(l))
'''

#Q6
'''
def arbitary(*args):
    sum = 0
    product = 1
    for i in args:
        sum += i
        product *= i
    return sum, product

n = int(input("Enter how many number you want to give: "))
num = []

for i in range(n):
    num.append(int(input("Enter number: ")))
print(f"Sum and Product of given numbers: {arbitary(*num)}")
'''

#Q7
'''
def names(*args):
    if len(name) == 0:
        print("List is empty...")
    else:
        for i in name:
            print(i)

n = int(input("Enter how many names you want to enter: "))
name = []

for i in range(n):
    name.append(input("Enter name: "))

names(*name)
'''

#Q8
'''
def filter(*args):
    string = ()
    number = ()

    for i in arg:
        if isinstance(i, str):
            string = string + (i,)
        elif isinstance(i, int):
            number = number + (i,)

    print(f"tuple of string is: {string}")
    print(f"tuple of number is: {number}")

n = int(input("Enter how many arguments you want to give: "))
arg = ()

for i in range(n):
    val = input("Enter value: ")
    if val.isdigit():
        arg = arg + (int(val),)
    else:
        arg = arg + (val,)

filter(*arg)
'''

#Q9
'''
def demo(**kwargs):
    print(kwargs)

demo(name = "Rensee", age = 20, city = "Surat")
'''

#Q10
'''
def details(**kwargs):
    total = 0
    output = ""

    for key, value in kwargs.items():
        print(f"{key} : {value}")

    if "Price" in kwargs and "Quantity" in kwargs:
        total = kwargs["Price"] * kwargs["Quantity"]
        output += f"Total ammount is : {total}\n"

    return output    

n = int(input("Enater how many recordes you want to add: "))
for i in range(n):
    name = input("Enter product name: ")
    price = int(input("Enter product price: "))
    quantity = int(input("Enter product quantity: "))

    result = details(Name = name, Price = price, Quantity = quantity)
    print(result)
'''

#Q11
'''
def details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key} : {value}")

    req_feilds = ["Name", "Salary", "Department"]
    miss = []
    for i in req_feilds:
        if i not in kwargs:
            miss.append(i)

    if miss:
        print(f"Missing feild is: {', '.join(miss)}") 

    else:
        print("All required feild is present.")   

n = int(input("Enater how many records you want to add: "))
d={}

for i in range(n):
    key = input("Enter a key: ")
    value = input("Enter value of key: ")
    d[key] = value

details(**d)
'''

#Q12
'''
def area(length, width):
    """
Docstring for area:
This will give you area of rectangle
    
param length: Length of rectangle
param width: width of rectangle

return the area of rectangle
    """
    return length*width

l = int(input("Enter length of rectangle: "))
w = int(input("Enter width of rectangle: "))

rec_area = area(l, w)
print("Area of rectangle: ",rec_area)

print(area.__doc__)
'''

#Q13
'''
def fibonacci(n):
    """
This function returns the Fibonacci series

Parameter:
n : The limit up to which Fibonacci numbers are generated

Returns a list containing Fibonacci series up to n
    """
    series = []
    a, b = 0, 1

    while a <= n:
        series.append(a)
        a, b = b, a + b

    return series

n = int(input("Enter a number: "))

result = fibonacci(n)
print("Fibonacci series:", result)

print(fibonacci.__doc__)
'''