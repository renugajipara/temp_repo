#Q1
'''
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

if a==b and b==c :
    print("Entered numbers are same...")

elif a==b or a==c or b==c:
    print("Entered two numbers are same...")

else:
    if a>b :
        if a>c :
            print(f"{a} is the greatest.")
        else : 
            print(f"{c} is the greatest.")

    else :
        if b>c :
            print(f"{b} is the greatest.")
        else :
            print(f"{c} is the greatest.")
'''

#Q2
'''
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))

if a==b and b==c :
    print("Entered numbers are same...")

elif a==b or a==c or b==c:
    print("Entered two numbers are same...")

else:
    if a<b :
        if a<c :
            print(f"{a} is the smallest.")
        else : 
            print(f"{c} is the smallest.")

    else :
        if b<c :
            print(f"{b} is the smallest.")
        else :
            print(f"{c} is the smallest.")
'''

#Q3
'''
a = int(input("Enter a number: "))
b = int(input("Enter a number: "))
c = int(input("Enter a number: "))
d = int(input("Enter a number: "))

if a==b and b==c and c==d :
    print("Entered numbers are same...")

else :
    if a>b :
        if a>c :
            if a>d :
                print(f"{a} is the greatest.")
            else : 
                print(f"{d} is the greatest.")
        elif c>d:
            print(f"{c} is the greatest.")
        else : 
            print(f"{d} is the greatest.")
    else:
        if b>c :
            if b>d:
                print(f"{b} is the greatest.")
            else :
                print(f"{d} is the greatest.")

        else :
            if c>d:
                print(f"{d} is the greatest.")
            else :
                print(f"{d} is the greatest.")
'''

#Q4
'''
num1 = int(input("Enter a number: "))
num2 = int(input("Enter a number: "))

while True:
    print("Press '+' for Add  \nPress '-' for subtract \nPress '/' for division \nPress '*' for multiplication \nPress 1 for Exit" )

    choice = input("Enter your choice:")

    match choice:
        case '+':
            add = num1 + num2
            print (f"Addition of {num1} and {num2} is {add}")

        case '-':
            diff = num1 - num2
            print (f"subtraction of {num1} and {num2} is {diff}")

        case '/':
            div = num1 / num2
            print (f"division of {num1} and {num2} is {div}")

        case '*':
            mul = num1 * num2
            print (f"Multiplication of {num1} and {num2} is {mul}")

        case '1':
            break

        case _:
            print("Invalid input!!!")
'''

#Q6
'''
while True:
    print("Press 1 for English")
    print("Press 2 for हिंदी")
    print("Press 3 for ગુજરાતી")
    print("Press 0 for Exit")

    choice = int(input("Enter your choice / अपनी भाषा चुनें / તમારી ભાષા પસંદ કરો: "))

    match choice:
        case 1:
            print("You have selected English")
            print("1. Balance Enquiry")
            print("2. Internet Plan")
            print("3. Customer Care")

            sub = int(input("Choose your option: "))

            match sub:
                case 1:
                    print("Your balance is ₹199")
                case 2:
                    print("You have a 1.5GB/day plan")
                case 3:
                    print("Please wait to talk to customer care")
                case _:
                    print("Invalid option")

        case 2: 
            print("आपने हिंदी चुनी है")
            print("1. बैलेंस जांच")
            print("2. इंटरनेट प्लान")
            print("3. कस्टमर केयर")

            sub = int(input("अपना विकल्प चुनें: "))

            match sub:
                case 1:
                    print("आपका बैलेंस ₹199 है")
                case 2:
                    print("आपके पास 1.5GB/दिन का प्लान है")
                case 3:
                    print("कृपया कस्टमर केयर से बात करने के लिए प्रतीक्षा करें")
                case _:
                    print("अमान्य विकल्प")

        case 3: 
            print("તમે ગુજરાતી પસંદ કરી છે")
            print("1. બેલેન્સ તપાસ")
            print("2. ઇન્ટરનેટ પ્લાન")
            print("3. કસ્ટમર કેર")

            sub = int(input("તમારો વિકલ્પ પસંદ કરો: "))

            match sub:
                case 1:
                    print("તમારું બેલેન્સ ₹199 છે")
                case 2:
                    print("તમારી પાસે 1.5GB/દિવસનો પ્લાન છે")
                case 3:
                    print("કૃપા કરીને કસ્ટમર કેર સાથે વાત કરવા રાહ જુઓ")
                case _:
                    print("અમાન્ય વિકલ્પ")
        case 0:
            break

        case _:
            print("You entered invalid number....")
'''