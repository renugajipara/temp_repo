#Q1
'''
l = ["Apple", "Mango", "Cherry", "Avacado", "Grapes"]
print(f"Second ele of list is {l[1]} and last ele of list is {l[-1]} ")

l.append("Kiwi")
print(l)

l.sort()
print(l[::-1])
'''

#Q2
'''
t = 1,2,3,4,5
print(t[2])

# t[1] = 8
# print(t)
# We can't replace ele of tuple bcz tuple is Immutable
'''

#Q3
'''
l = ["Apple", "Mango", "Cherry", "Avacado", "Grapes"]
l[2] = "Dragon fruit"
print(l)
'''

#Q4
'''
l = []
for i in range(1,11):
    i = i**2
    l.append(i)
print(l)

l2 = []
for i in range(1,21):
    if i%2 == 0:
        l2.append(i)
print(l2)

s = ['hello', 'WORLD', 'PyTHon']
for i in s:
    print(i.lower())
'''