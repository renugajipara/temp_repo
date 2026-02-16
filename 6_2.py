#Q1
'''
a = int(input("Enter numerator: "))
b = int(input("Enter denominator: "))

try:
    c = a/b

except ZeroDivisionError as e:
    print(f"Not possiblr beacuse {e}")

else:
    print(f"Division of given numbers is: {c}")
'''

#Q2
'''
l = [1,2,3,4,5]
try:
    n = int(input("Enter index number: "))
    print(l[n])
except IndexError as e:
    print(f"Element is not found bcz {e}")
'''

#Q3
'''
file = input("Enter file name: ")

try:
    with open(file, "r") as f:
        text = f.read()

except FileNotFoundError as e:
    print(f"Can't open {file} bcz {e}")

else:
    print(text)
'''

#Q4
'''
s = input("Enter any string: ")
try:
    n = int(input("Enter index number: "))
    index = s[n]
except IndexError as e:
    print(f"Element is not found bcz {e}")
else:
    print(f"Charecter at index {n} is: {index}") 
'''

#Q5
'''
file = input("Enter file name: ")

try:
    f = open(file, "r")
    text = f.read()

except FileNotFoundError as e:
    print(f"Can't open {file} bcz {e}")

else:
    print(text)

finally:
    try:
        f.close()
        print("File closed successfully...")
    except:
        print("File has no connection, so no need to close...")
'''

#Q6
'''
a = int(input("Enter numerator: "))
b = int(input("Enter denominator: "))
c = None

try:
    c = a/b

except ZeroDivisionError as e:
    print(f"Not possiblr beacuse {e}")

finally:
    if c is not None:
        print(f"Division of given numbers is: {c}")
'''

#Q7
'''
import math

n = int(input("Enter any number: "))

try:
    if n<0:
        raise ValueError("Can't find sqaure root of negative number.")
    root = math.sqrt(n)
except ValueError as e:
    print(f"Invlid input: {e}")
else:
    print(f"Sqaure of given number is: {root}")
finally:
    print("Execution complete...")
'''