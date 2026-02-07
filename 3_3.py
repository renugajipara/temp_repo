#Q1
'''
s ={1,2,3,4,5}
s.add(6)
print(s)
s.remove(3)
print(s)
ans = 2 in s
print(ans)
'''

#Q2
'''
s1 = {1,2,3,4}
s2 = {3,4,5,6}

a1 = s1.union(s2)
a2 = s1.intersection(s2)
a3 = s1.difference(s2)

print(f"Union of two set is {a1}\nIntersection of two set is {a2}\nDifference of two set is {a3}")
'''

#Q3
'''
student = {"name": "Rensee", "age": 20, "grade": "A"}
for i in student.items():
    print(i)
student["city"] = "Delhi"
print(student)
student["age"] = 21
print(student)
del student["grade"]
print(student)
'''

#Q4
'''
keys = ['id', 'name', 'email']
values = [101, 'Bob', 'bob@example.com']
d = {}

for i in range(len(keys)):
    d[keys[i]] = values[i]
print(d)
'''

#Q5
'''
s ='123'
print(int(s))

l = [1,2,3]
print(tuple(l))

t = (1,2,3)
print(list(t))

d = [(1,'A'),(2,'B')]
print(dict(d))
'''