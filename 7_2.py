
import math
import random
import time
#Q1
'''
print(f"Square root : {math.sqrt(81)}")
print(f"Factorial : {math.factorial(8)}")
print(f"Power : {math.pow(2, 5)}")
'''

#Q2
'''
r = int(input("Enter radius of circle: "))
print(f"Area of circle: {math.pi * r * r}")

print(f"Natural log: {math.log(r)}")
'''

#Q3
'''
angle = 90
radian = math.radians(angle)

print(f"Sin value: {math.sin(radian)}")
print(f"Cos value: {math.cos(radian)}")
print(f"Tan value: {math.tan(radian)}")
'''

#Q4
'''
n = float(input("Enter any number: "))

print(f"Ceil value : {math.ceil(n)}")
print(f"floor value : {math.floor(n)}")
print(f"Absolute value : {abs(n)}")
'''

#Q5
'''
gen = []
for i in range(10):
    gen.append((random.randint(1, 100)))
print(f"Random number from 1 to 100: {gen}")
'''

#Q6
'''
dice = random.randint(1,6)
print(f"Roll Dice: {dice}")

l = [1, 4, 7, 9, 2, 5, 3]
random.shuffle(l)
print(f"Shuffled list: {l}")
'''

#Q7
'''
l = ["Rensee", "Nely", "Kelvi", "Krisha"]
choice = random.choice(l)
print(f"Random name: {choice}")
'''

#Q8
'''
player = input("Enter your move: ")
print(f"Player: {player}")

l = ["Stone", "Paper", "Scissor"]
ai = random.choice(l)
print(f"AI: {ai}")

time.sleep(1)

if player in l:
    if (player=="Stone" and ai=="Scissor") or (player=="Scissor" and ai=="Paper") or (player=="Paper" and ai=="Stone"):
        print("Player has won!!")

    elif (ai=="Stone" and player=="Scissor") or (ai=="Scissor" and player=="Paper") or (ai=="Paper" and player=="Stone"):
        print("AI has won!!")
    
    else:
        print("Game tie...")

else:
    print("Invalid Input from Player!")
'''