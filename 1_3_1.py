#Q1
'''
inpt = input("Enter any string: ")
print(f"user entered '{inpt}' as string and type:{type(inpt)}")

a = int(inpt)
b = float(inpt)
c = bool(inpt)

print(f"typecasting as int :{a}, type:{type(a)}")
print(f"typecasting as float :{b}, type:{type(b)}")
print(f"typecasting as boolean :{c}, type:{type(c)}")
'''

#==================
#Q2
'''
inpt = bool(input("Enter any boolean value: "))
print(f"user entered '{inpt}' and type:{type(inpt)}")

a = int(inpt)
b = str(inpt)

print(f"typecasting as int :{a}, type:{type(a)}")
print(f"typecasting as str :{b}, type:{type(b)}")
'''

#Q3

a = 2
b = 3.4
c = 'Rensee'
d = True
l = [1,2,3,4]
t = (1,2,3,4)
dic = {1:'you', 2:'are', 3:'cute'}

print(f"int :{a}, type:{type(a)}, Id:{id(a)}")
print(f"float :{b}, type:{type(b)}, Id:{id(b)}")
print(f"string :{c}, type:{type(c)}, Id:{id(c)}")
print(f"boolean :{d}, type:{type(d)}, Id:{id(d)}")
print(f"list :{l}, type:{type(l)}, Id:{id(l)}")
print(f"tuple :{t}, type:{type(t)}, Id:{id(t)}")
print(f"dictionary :{dic}, type:{type(dic)}, Id:{id(dic)}")
