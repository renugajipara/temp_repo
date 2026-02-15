#Q1
'''
with open("sample.txt", "w") as f:
    f.write("Python is versetile programming langauge.")
'''

#Q2
'''
with open("sample.txt", "r") as f:
    print(f.read())

with open ("sample.txt", "w") as f:
    f.write("Learning file handling in python is fun!!")
'''

#Q3
'''
with open("sample.txt", "r") as f:
    print(f.read())
'''

#Q4
'''
with open ("notes.txt", "a") as f:
    n = int(input("Enter how many lines you want to enter: "))

    for i in range(n):
        content = input("Enter content: \n")
        f.write(f"Line {i} : {content}\n")
'''

#Q5
'''
with open ("notes.txt", "a") as f:
    f.write("Line 4 : Python support multiple modes of file handling.")
'''

#Q6
'''
with open("sample.txt", "rb") as f:
    print(f.read())
'''

#Q7
'''
with open("notes.txt", "r") as f:
    content = f.read()
    print(content)
    print(f"Total charechters : {len(content)}")
    print(f"Total words : {len(content.split())}")
    line = content.count("\n") + 1
    print(f"Total lines : {line}")
'''

#Q8
'''
with open("sample.txt", "r+") as f:
    print(f.read())
    f.write("\nThis file was last modified by adding this sentence")
'''

#Q9
'''
with open("sample.txt", "r+") as f:
    content = f.readlines()
    word = input("Enter a word you want to search: ")

    for i in range(len(content)):
        if word in content[i]:
            print(f"Word found in line {i+1}")
'''

#Q10
'''
with open ("source.txt", "w") as f:
    f.write("this is source file...")

with open ("source.txt", "r") as f:
    content = f.read()

with open ("backup.txt", "w") as f:
    f.write(content)
'''

#Q11
'''
with open ("source.txt", "w") as f:
    f.write("this is source file...")

with open ("source.txt", "r") as f:
    print(f"r mode : {f.read()}")

with open ("source.txt", "a") as f:
    f.write("append using a mode")

with open ("source.txt", "r+") as f:
    content = f.read()
    f.write("Print using r+ mode")

with open ("source.txt", "w+") as f:
    f.write("\nModifies with new content.")
    f.seek(0)
    print(f.read())

with open ("source.txt", "a+") as f:
    f.write("\nappend usng a+ mode")
    f.seek(0)
    print(f"Reading the latest content: {f.read()}")
'''