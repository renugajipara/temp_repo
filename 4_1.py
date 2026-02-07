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

