#Q1
'''
while True:
    n = int(input("Enter a number: "))
    print (f"You entered {n}")

    if n == 0:
        break
'''

#Q2
'''
n = int(input("Enter a number: "))

for i in range(1, n+1):
    print(f"Squre of {i} is {i**2}.")
'''

#Q3
'''
n = int(input("Enter a number: "))
i = 1
while i<=n:
    if i%2 == 0:
        print(i)
    i += 1
'''

#Q5
'''
for i in range (5,50+1,5):
    print(i)
'''

#Q7
'''
for i in range (1,50+1):
    if i%2 == 0:
        if i%3 == 0:
            print(f"{i} is divisable by both")
        else:
            print(f"{i} is divisable by 2")

    elif i%3 == 0:
        print(f"{i} is divisable by 3")
'''