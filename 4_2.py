#Q1
'''
def factorial(n):
    if n < 0:
        print("Input is Invalid. PLz enter positive number.")

    if n == 0 or n == 1:
        return 1
        
    return n * factorial(n-1)

n = int(input("Enter any number: "))
print(f"Factorial of {n} is {factorial(n)}")
'''

#Q2
'''
def fibonaci(n):
    if n < 0:
        print("Input is Invalid. PLz enter positive number.")

    if n == 0:
        return 0
    
    if n == 1:
        return 1
    
    return fibonaci(n-1) + fibonaci(n-2)

n = int(input("Enter any number: "))
print(f"Fibonaci series of given number: {fibonaci(n)}")
'''

#Q3
'''
def reverse(s):
    if len(s) == 0:
        return s
    
    return reverse(s[1:]) + s[0]

s = input("Enter any string: ")
print(f"Reversed stirng : {reverse(s)}")
'''

#Q4
'''
def sum(n):
    if len(n) == 1:
        return int(n)
    
    return int(n[0]) + sum(n[1:])

n = input("Enter any number: ")
print(f"Sum of given number is: {sum(n)}")
'''

#Q5
'''
def prime(n, divisor=2):
    if n <= 1:
        return False
    
    if divisor * divisor > n:
        return True
    
    if n % divisor == 0:
        return False

    return prime(n, divisor+1)

def display(n1, n2):
    if n1 > n2:
        return
    
    if prime(n1):
        print(n1)
    
    display(n1+1, n2) 

n1 = int(input("Enter first number: "))
n2 = int(input("Enter second number: "))

print(f"Prime numbers between {n1} and {n2} are:")
display(n1, n2)
'''

#Q6
'''
sqr = lambda a : a ** 2
n = int(input("Enter any numbder: "))
print(f"Square of given number: {sqr(n)}")
'''

#Q7
'''
num = []
n = int(input("Enter how many number you want to store? : "))
for i in range(n):
    ele = int(input("Enter element: "))
    num.append(ele)

odd = list(filter(lambda x : x%2 == 1, num))
print(f"Odd numbers from the list: {odd}")
'''

#Q8
'''
maximum = lambda x, y, z : x if x>y and x>z else(y if y>z else z)
n1 = int(input("Enter a number: "))
n2 = int(input("Enter a number: "))
n3 = int(input("Enter a number: "))

print(f"Maximum of given three number: {maximum(n1, n2, n3)}")
'''

#Q9
'''
count = 0
def sum():
    global count
    count += 1

sum()
sum()
sum()
print(f"Functoin is called {count} times.")
'''

#Q10
'''
sum = 0

def total():
    global sum
    n = int(input("Enter a number: "))
    sum += n 
    print(f"Sum : {sum}")

total()
total()
total()
'''

#Q11
'''
name = None

def update():
    global name 
    name = input("Enter your name: ")
    print(f"Updated name: {name}")

update()
'''

#Q12
'''
def initilize():
    global n
    n = 5
    print(f"Initial value: {n}")

def increament():
    global n 
    a = int(input("Enter number how much you want to increament: "))
    n += a
    print(f"Increamented value: {n}")

initilize()
increament()
'''

#Q13
'''
x = 5
print(f"Global variable value: {x}")

def demo():
    x = 10
    print(f"Local variable value: {x}")

demo()
'''

#Q14
'''
num = []
n = int(input("Enter how many number you want to store? : "))
for i in range(n):
    ele = int(input("Enter element: "))
    num.append(ele)
print(num)

def sum():
    add = 0
    for i in num:
        add += i 
    return add
def maximum():
    maxi = num[0]
    for i in num:
        if i > maxi:
            maxi = i
    return maxi

def minimum():
    mini = num[0]
    for i in num:
        if i < mini:
            mini = i
    return mini

print(f"Total : {sum()}")
print(f"Maximum : {maximum()}")
print(f"Minimum : {minimum()}")
'''

#Q15
'''
def rectangle():
    l = int(input("Eneter length of rectangle: "))
    w = int(input("Eneter width of rectangle: "))

    perimeter = 2 * (l+w)
    area = l * w

    return perimeter, area

perimeter, area = rectangle()

print(f"Perimeter of rectangle is: {perimeter}")
print(f"Area of rectangle is: {area}")
'''

#Q16
'''
def calc():
    n = int(input("Enter a number: "))
    t = ()
    sqr = n ** 2
    cube = n ** 3
    t += (sqr, cube)
    return t

print(f"Returned tuple: {calc()}")
'''

#Q17
'''
def partition(s):
    vowels = "aeiouAEIOU"
    vow = set()
    char = set()
    for i in s:
        if i in vowels:
            vow.add(i)
        else:
            char.add(i)

    return vow, char

s = input("Enter any string: ")
vowels, char = partition(s)

print(f"Vowels from given string is: {vowels}")
print(f"Character from given string is: {char}")
'''

#Q18
'''
def diff(l):
    vowels = "aeiouAEIOU"
    vow = []
    char = []

    for i in l:
        if i[0] in vowels:
            vow.append(i)
        else:
            char.append(i)
    return vow, char

l = []
n = int(input("Enter how many words you want to store? : "))
for i in range(n):
    ele = input("Enter word: ")
    l.append(ele)
print(f"Given list: {l}")

vowels, char = diff(l)
print(f"Words that start with vowels: {vowels}")
print(f"Words that start with cosonant: {char}")
'''