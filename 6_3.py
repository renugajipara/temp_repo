#Q1
'''
try:
    n = int(input("Enter a number: "))

    if n < 0:
        raise ValueError("Plz enter positive number...")
    
    print(f"Entered number is: {n}")

except ValueError as e:
    print(f"Error: {e}")
'''

#Q2
'''
def check_even(num):
        if not isinstance(num, int):
            raise TypeError("Given number is not integer...")

        if num%2 == 1:
            raise ValueError("Given number is odd.")
        
        print(f"{num} is even integer...")

try:
    n = int(input("Enter any number: "))
    check_even(n)
    
except ValueError as e:
    print(f"Error: {e}")
'''

#Q3
'''
age = int(input("Enter your age: "))

try:
    if age <= 0 :
        raise ValueError("Age can't be in negative.")

    assert age>=18, "Age must be greater than or equal to 18"

except AssertionError:
    print("Age must be greater than or equal to 18")

except ValueError as e:
    print(f"Error: {e}")

else:
    print("You can vote.")
'''

#Q4
'''
def check_palindrome(string):
    assert string != "", "Sring is empty."

    if string == string[::-1]:
        print(f"{string} is Palindrome string.")
    else:
        print(f"{string} is not Palindrome string.")

try:
    s = input("Enter any string: ")
    check_palindrome(s)

except AssertionError as e:
    print(f"Error: {e}")
'''

#Q5
'''
class InsufficientBalanceError(Exception):
    pass

def withdraw(balance, amount):
    if amount > balance:
        raise InsufficientBalanceError ("Your blance is less than your withdrawal amount.")
    
    balance -= amount
    print(f"Balance after withdrawal is {balance}")

try:
    balance = float(input("Enter how many balance you already have?: "))
    amount = float(input("Enter how many amount you want to withdraw: "))
    withdraw(balance, amount)

except InsufficientBalanceError as e:
    print(f"Error: {e}")
'''

#Q6
'''
class InvalidEmailError(Exception):
    pass

def validate_email(email):
    if "@" not in email:
        raise InvalidEmailError("Your email is not containg @")
    
    if not (email.endswith(".com") or email.endswith(".org")):
        raise InvalidEmailError("Your email is not end with .com or .org")
    
    print("Valid Email.")
        
try:
    email = input("Enter your email: ")
    validate_email(email)

except InvalidEmailError as e:
    print(f"Error: {e}")
'''

#Q7
'''
class InvalidGradeError(Exception):
    pass

def validate_grade(grade):
    assert grade.strip() != "", "Grade input cannot be empty."

    try:
        grade = float(grade)
    except ValueError:
        raise ValueError("Grade must be a numeric value.")

    if grade < 0 or grade > 100:
        raise ValueError("Grade must be between 0 and 100.")

    if grade < 40:
        raise InvalidGradeError("Grade is below 40. Student has failed.")

    print("Grade is valid. Student passed.")

try:
    grade = input("Enter student's grade: ")
    validate_grade(grade)

except (AssertionError, ValueError, InvalidGradeError) as e:
    print("Error:", e)
'''

#Q8
'''
class HighTemperatureError(Exception):
    pass

def validate_temperature(temp):
    try:
        temp = float(temp)
    except ValueError:
        raise TypeError("Temperature must be a numeric value.")

    assert -273 <= temp <= 10000, "Temperature must be between -273°C and 10,000°C."
        
    if temp > 1000:
        raise HighTemperatureError("Temperature exceeds 1000°C. Unrealistic for common applications.")

    print("Temperature is valid.")

try:
    temp = input("Enter temperature in Celsius: ")
    validate_temperature(temp)

except (AssertionError, TypeError, HighTemperatureError) as e:
    print("Error:", e)
'''