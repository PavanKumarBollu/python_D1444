"""
calculator application
addition
subtraction
multiplication
division

task
---

enhance this application by adding some more features like
floor division
exponentiation
modulos

some things which you can add by user self


"""

def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b

while True:
    print("Enter 1 for addition : ")
    print("Enter 2 for subtraction : ")
    print("Enter 3 for multiplication : ")
    print("Enter 4 for division : ")
    print("Enter 5 for quit: ")
    u_input = input("what would you like to do .? : ")

    if u_input == "1":
        num1 = int(input("Enter first number : "))
        num2 = int(input("Enter second number : "))
        res = addition(num1, num2)
        print(res)
    elif u_input == "2":
        num1 = int(input("Enter first number : "))
        num2 = int(input("Enter second number : "))
        res = subtraction(num1, num2)
        print(res)
    elif u_input == "3":
        num1 = int(input("Enter first number : "))
        num2 = int(input("Enter second number : "))
        res = multiplication(num1, num2)
        print(res)
    elif u_input == "4":
        num1 = int(input("Enter first number : "))
        num2 = int(input("Enter second number : "))
        res = division(num1, num2)
        print(res)
    elif u_input == "5":
        break
    else:
        break
