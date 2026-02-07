
students = [{"id":101, "name": "Alice", "score":85 },
            {"id":102, "name": "Bob", "score":78 },
            {"id":103, "name": "Charlie", "score":92 }]
'''
for i in students:
    print(i["name"])
'''
'''
sc = 0
for i in students:
    sc = i["score"] + sc
print(sc/3)
'''
'''
students.append({"id":104, "name": "Walt", "score":80})
print(students)
'''
'''
for i in students:
    if i["id"] == 102:
        i["score"] = 88
print(students)
'''
'''
for i in students:
    if i["name"] == "Charlie":
        students.remove(i)
print(students)
'''
'''
for i in students:
    if i["score"] > 80:
        print(i["name"])
'''
'''
students.sort(key=lambda x: x["score"], reverse=True)
print(students)
'''
'''
high_sc = students[0]

for i in students:
    if i["score"] > high_sc["score"]:
        high_sc = i
print(high_sc)
'''

for i in students:
    if i["score"] >= 90:
        i["grade"] = "A"
        
    elif i["score"] >= 80 and i["score"] < 90:
        i["grade"] = "B"
        
    else:
        i["grade"] = "C"
    print(f"Name:{i["name"]} | Score:{i["score"]} | Grade:{i["grade"]}")

    
c1 = 0
c2 = 0
c3 = 0
for i in students:
    if i["grade"] == "A":
        c1 += 1
    elif i["grade"] == "B":
        c2 += 1 
    elif i["grade"] == "C":
        c3 += 1
print(f"{c1} students have 'A' grade")
print(f"{c2} students have 'B' grade")
print(f"{c3} students have 'C' grade")