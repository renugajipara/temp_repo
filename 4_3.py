#Q1
'''
arr = [1, 2, 3, 4, 5]
for i in arr:
    print(i)
'''

#Q2
'''
arr = []
sum = 0
n = int(input("Enter how many words you want to store? : "))
for i in range(n):
    ele = int(input("Enter num: "))
    arr.append(ele)
    sum += ele

print(f"Sum of all elements: {sum}")
'''

#Q3
'''
arr = []

n = int(input("Enter how many words you want to store? : "))
for i in range(n):
    ele = int(input("Enter num: "))
    arr.append(ele)
print(f"Original array: {arr}")

index = int(input("Eneter index you want to change ele: "))
element = int(input("Eneter element: "))

if 0 <= index  <= len(arr):
    arr.insert(index, element)
    print(f"After adding new element: {arr}")

else:
    print("Invalid index")
'''

#Q4
'''
arr = [1, 3, 5, 7, 9]
arr.remove(5)
print(arr)
'''

#Q5
'''
arr = []
n = int(input("Enter how many words you want to store? : "))
for i in range(n):
    ele = int(input("Enter num: "))
    arr.append(ele)
print(f"Original array: {arr}")

index = int(input("Eneter index you want to change ele: "))
element = int(input("Eneter element: "))

if 0 <= index  <= len(arr):
    arr[index] = element
    print(f"Updated array: {arr}")

else:
    print("Invalid index")
'''

#Q6
'''
arr = []
n = int(input("Enter how many words you want to store? : "))
for i in range(n):
    ele = int(input("Enter num: "))
    arr.append(ele)
print(f"Original array: {arr}")

element = int(input("Enter element you want to search: "))
for i in range(len(arr)):
    if arr[i] == element:
        print(f"Index of searching element: {i}") 
'''

#Q7
'''
arr1 = []
arr2 = []

n1 = int(input("Enter how many words you want to store in Array1? : "))
for i in range(n1):
    ele = int(input("Enter num: "))
    arr1.append(ele)
print(f"Array1: {arr1}")

n2 = int(input("Enter how many words you want to store in Array2? : "))
for i in range(n2):
    ele = int(input("Enter num: "))
    arr2.append(ele)
print(f"Array2: {arr2}")

arr = arr1 + arr2
print(f"Concated array: {arr}")
'''