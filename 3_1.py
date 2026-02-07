#Q3
'''
string = input("Enter a string: ")

rev = string[::-1]
print(f"Reversed string is: {rev}")

if string == rev :
    print("Given string is palindrome.")

else:
    print("Given string is not palindrome.")
'''

#Q4
'''
string = input("Enter a string: ")

print(f"Upper case string is: {string.upper()}")
print(f"Lower case string is: {string.lower()}")
print(f"Titled string is: {string.title()}")
'''

#Q5
'''
s = "Machine learning and AI are trending."
s2 = "data data mining and bid data."

pos = s.index("AI")
print(f"Index of AI is: {pos}")

cnt = s2.count("data")
print(f"Count of data is: {cnt}")
'''

#Q6
'''
s = "Apple,Banana,Grapes"
print(s.split(","))

word = ["Python", "is", "awesome"]
print(" ".join(word))

string = """Hello
I'm Rensee
I'm learning python"""

line = string.split("\n")
for i in line:
    print(i)
'''

#Q7
'''
s = "Hello World"
start = s.startswith("Hello")
end = s.endswith("World")

if start :
    print("String staring with Hello.")
else:
    print("String is not staring with Hello.")

if end :
    print("String ending with World.")
else:
    print("String is not ending with World.")

s2 = "Data123#Scince!"
string = " "
for i in s2:
    if i.isalpha():
        string += i
print(string)
'''