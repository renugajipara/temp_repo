#Q1
'''
arr = []
n = int(input("Enter how many words you want to store? : "))
for i in range(n):
    ele = int(input(f"a[{i}]: "))
    arr.append(ele)
print(f"Original array: {arr}")
print(f"Length of the array: {len(arr)}")
'''

#Q2
'''
arr = []
sum = 0 
n = int(input("Enter how many words you want to store? : "))

for i in range(n):
    ele = int(input(f"a[{i}]: "))
    arr.append(ele)
    sum += ele
    avg = sum / len(arr)

print(f"Original array: {arr}")
print(f"Average of elements: {avg}")
'''

#Q3
'''
arr1 = []
arr2 = []

n = int(input("Enter how many words you want to store in Array? : "))
print("Enter Array A element:")
for i in range(n):
    ele = int(input(f"a[{i}]: "))
    arr1.append(ele)
print(f"Array1: {arr1}")

print("Enter Array B element:")
for i in range(n):
    ele = int(input(f"a[{i}]: "))
    arr2.append(ele)
print(f"Array2: {arr2}")

arr = []
for i in range(n):
    arr.append(arr1[i] + arr2[i])

print(f"Array C is: {arr}")
'''

#Q4
'''
arr = [1,2,3,4,5,6,7,8,9,10]
mul = []
for i in arr:
    mul.append(i * 2)
print(f"Array after multiply by 2: {mul}")
'''

#Q5
'''
arr = []
n = int(input("Enter how many words you want to store? : "))
for i in range(n):
    ele = int(input("Enter num: "))
    arr.append(ele)
print(f"Original array: {arr}")

element = int(input("Enter element you want to search: "))
found = False
for i in range(len(arr)):
    if arr[i] == element:
        print(f"Index of searching element: {i}") 
        found = True
        break

if not found:
    print("Element not found.")
'''

#Q6
'''
arr = []
n = int(input("Enter how many words you want to store? : "))
for i in range(n):
    ele = int(input("Enter num: "))
    arr.append(ele)
print(f"Original array: {arr}")

for i in arr:    
    if i%2 == 0:
        print(f"Even number: {i}")

    else:
        print(f"Odd numbers: {i}")
'''

#Q7
'''
arr = []
n = int(input("Enter how many words you want to store? : "))
for i in range(n):
    ele = int(input("Enter num: "))
    arr.append(ele)
print(f"Original array: {arr}")

print(f"First 5 elements: {arr[:5]}")
print(f"Alternative in array: {arr[::2]}")
'''

#Q8
'''
arr = []
n = int(input("Enter how many words you want to store? : "))
for i in range(n):
    ele = int(input("Enter num: "))
    arr.append(ele)
print(f"Original array: {arr}")

print(f"First element of array: {arr[0]}")
print(f"Last element of array: {arr[-1]}")
print(f"Middle element of array: {arr[n // 2]}")
'''