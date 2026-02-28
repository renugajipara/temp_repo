import uuid
from functools import reduce
#Q1
'''
random = uuid.uuid4()
print(random)

name = uuid.NAMESPACE_DNS
my_uuid = uuid.uuid5(name,"example.com")
print(f"Name space based uuid: {my_uuid}")
'''

#Q2
'''
d = {}
n = int(input("Enter students you want to add: "))

for i in range(1, n+1):
    uid = uuid.uuid4()
    d[i] = uid
    print(f"Student_Id: {i} | UUID: {uid}")
print(d)
'''

#Q3
'''
u1 = uuid.uuid4()
u2 = uuid.uuid4()
u3 = u1

print(f"First uuid: {u1}")
print(f"Second uuid: {u2}")

print(f"uuid1 == uuid2 : {u1 == u2}")
print(f"uuid1 == uuid3 : {u1 == u3}")
'''

#Q4
'''
class order:
    def __init__(self, product, quantity):
        self.order_id = uuid.uuid4()
        self.product = product
        self.quantity = quantity
        
    def display(self):
        print(f"Order Id : {self.order_id}")
        print(f"Product  : {self.product}")
        print(f"Quantity : {self.quantity}")
        print("="*10)
        
orders = []
n = int(input("Enter how many orders do you want to place? "))

for i in range(n):
    print(f"Order no {i+1} details:")
    product = input("Enter product name: ")
    quantity = int(input("Enter quantity of product: "))
    o = order(product, quantity)
    orders.append(o)
        
print("\n===== All Orders =====")
for o in orders:
    o.display()  
'''

#Q5
'''
l = [3, 6, 1, 8, 2, 9, 7]
print(f"Sorted list in ascending order: {sorted(l)}")
print(f"Sorted list in ascending order: {sorted(l, reverse=True)}")
'''

#Q6
'''
l = ["Rensee", "Nely", "Kelvi", "Krisha"]
print(f"Sorted by length of word: {sorted(l, key=len) }")
print(f"Sorted by last letter of word: {sorted(l, key = lambda x:x[-1])}")
'''
#Q7
'''
d = [{"name" : "Rensee","age" : 21}, {"name" : "Nely","age" : 20}, {"name" : "Kelvi","age" : 22}]
print(f"Sorted list of dictionary by one key: {sorted(d, key = lambda x:x["age"])}")
'''

#Q8
'''
l = ["Rensee", "Nely", "Kelvi", "Krisha"]
print(f"Uppercase: {list(map(str.upper, l))}")
'''

#Q9
'''
l = [2,5,3,9,7,6]
print(f"Sqaure of int in list using map: {list(map(lambda x:x**2, l))}")
'''

#Q10
'''
l = [200, 400, 500, 650, 720, 810]
print(f"Prices after 18% GST: {list(map(lambda x:round(x*1.18, 2), l))}")
'''

#Q11
'''
l = [2,5,3,9,7,6,4,8]
print(f"Even numbers from list using filter: {list(filter(lambda x: x%2==0, l))}")
'''

#Q12
'''
l = ["Rensee", "Nely", "Kelvi", "Krisha"]
print(f"Strings that has more than 5 characters in list: {list(filter(lambda x: len(x)>5, l))}")
'''

#Q13
'''
student_score = [33, 47, 89, 64, 52, 100]
print(f"Student score >= 40: {list(filter(lambda x: x>=40, student_score))}")
'''

#Q14
'''
l = [2,5,3,9,7,6,4,8]
product = reduce(lambda x,y: x*y, l)
print(f"Product of all element using reduce: {product}")
'''

#Q15
'''
l = ["Rensee", "Nely", "Kelvi", "Krishaa"]
long = reduce(lambda x, y: x if len(x)>= len(y) else y, l)
print(f"Longest word from list: {long}")
'''

#Q16
'''
l = ["Hello!!", "I'm", "Rensee"]
s = reduce(lambda x, y: x+ " "+ y, l)
print(f"Concatenated list: {s}")
'''