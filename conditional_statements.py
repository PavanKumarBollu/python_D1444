# if , if-elif , if-elif-else
# nesting the conditions


# if condition

# the if statements allows you to execute a block of code by checking some condition
"""
if syntax:

if condition:
    #lines of code that needs to be excecuted when the condition is true


if condition:
    #lines of code that needs to be excecuted when the condition is true
else:
    #lines of code that needs to be excecuted when the condition is false


if condition1:
    #lines of code that needs to be executed when the condition is true
elif condition2:
    #lines of code that needs to be excecuted when the condition is true
elif condition3:
    #lines of code that needs to be excecuted when the condition is true
else:
    #lines of code that needs to be excecuted when all the condition is false

"""

# examples:
# age = 2
#
# if age >= 18:
#     print("You are eligible to vore..!")

#
# age = 20
#
# if age >= 18:
#     print("You are eligible to vote..!")
# else:
#     print("You are not eligible to vote..")


# take a number from the user and verify weather the number is even or not

# num = int(input("Enter a number: "))
# if num %2 == 0:
#     print( f" {num} is a Even number")
# else:
#     print(f" {num} is a Odd number")



# take a alphabet from the user and check weather the alphabet is vowel or not
# if user entered character is in a e i o u then it's a vowel otherwise it's not vowel




# char = input("Enter a character: ")
#
# if char == "a" or char == "e" or char == "i" or char == "o" or char == "u" or char == "A" or char == "E" or char == "I" or char == "O" or char == "U":
#     print(f"{char} is a vowel character")
# else:
#     print(f"{char} is not a vowel character")
#
#
#
# if char == "a" or char == "A":
#     print(f"{char} is a vowel ")
# elif char == "e" or char == "E":
#     print(f"{char} is a vowel ")
# elif char == "i" or char == "I":
#     print(f"{char} is a vowel ")
# elif char == "o" or char == "O":
#     print(f"{char} is a vowel ")
# elif char == "u" or char == "U":
#     print(f"{char} is a vowel ")
# else:
#     print(f"{char} is not a vowel ")



vowels = ['a', 'e', 'i', 'o', 'u']

char = input("Enter a character: ")

if char in vowels:
    print(f"{char} is a vowel ")
else:
    print(f"{char} is not a vowel")










