#Q1
'''
arr = []
rows = int(input("Enter how many rows you want to add? "))
colunms = int(input("Enter how many colunms you want to add? "))

for i in range(rows):
    row = []
    for j in range(colunms):
        ele = int(input("Enter element: "))
        row.append(ele)
    arr.append(row)
print(arr)

for i in arr:
    for j in i:
        print(j, end=" ")
    print()
'''

#Q2
'''
arr = []
rows = int(input("Enter how many rows you want to add? "))
colunms = int(input("Enter how many colunms you want to add? "))

for i in range(rows):
    row = []
    for j in range(colunms):
        ele = int(input("Enter element: "))
        row.append(ele)
    arr.append(row)
print(arr)

print("Transpose Matrix:")
for i in range(len(arr[0])):
    for j in arr:
        print(j[i], end=" ")
    print()
'''

#Q3
'''
arr = []
rows = int(input("Enter how many rows you want to add? "))
colunms = int(input("Enter how many colunms you want to add? "))

for i in range(rows):
    row = []
    for j in range(colunms):
        ele = int(input("Enter element: "))
        row.append(ele)
    arr.append(row)
print(arr)

sum = 0
for i in arr:
    for j in i:
        sum += j
print(f"Sum : {sum}")
'''

#Q4
'''
arr = []
rows = int(input("Enter how many rows you want to add? "))
colunms = int(input("Enter how many colunms you want to add? "))

for i in range(rows):
    row = []
    for j in range(colunms):
        ele = int(input("Enter element: "))
        row.append(ele)
    arr.append(row)
print(arr)

for i in arr:
    for j in i:
        maxi = arr[0][0]
        mini = arr[0][0]
        if j > maxi:
            maxi = j
        if j < mini:
            mini = j

print(f"Maximum : {maxi}")
print(f"minimum : {mini}")
'''

#Q5
'''
num = []
n = int(input("Enter how many number you want to store? : "))
for i in range(n):
    ele = int(input("Enter element: "))
    num.append(ele)
print(num)
num.sort()
print(f"Sorted list: {num}")
'''

#Q6
'''
l = []
n = int(input("Enter hoe many record you want to add: "))

for i in range(n):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    l.append((name, age))

print(l)

print(f"Sorted list by sencond element of tuple: {sorted(l,key = lambda x : x[1])}")
'''

#Q7
'''
l = []
n = int(input("Enter hoe many record you want to add: "))

for i in range(n):
    name = input("Enter name: ")
    age = int(input("Enter age: "))
    l.append({"name": name, "age": age})

print(l)

print(f"Sorted list by key of dictionary: {sorted(l, key = lambda x: x["name"])}")
'''

#Q8
'''
l = [2,5,9,6,3,8,4,7,1]
print(f"Original list: {l}")

l.sort()#this will direct update the original list permanently.
print(f"Sorted list using sort() method: {l}")

sort = sorted(l)#this will only return sorted list. don't change the list permanently.
print(f"Sorted list using of sorted() function: {sort}")
'''