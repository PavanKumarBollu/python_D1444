# num = int(input("Enter a number: "))
# sum = 0
# i = 0
# while i <= num:
#     sum += i
#     i+=1
# print(sum)

#if -> input is 10 then result of the above code is -> 55


"""
For loop
--------
for loop is a control flow statement in python programming which allows us to execute some code repeatedly
for a specific number of times or iterate over a sequence of elements such as list arrays ..etc

syntax of for loop
------------------

for variable in sequence(range):
    #code to be executed in each iteration

for -> this is a keyword that specify and starts the loop

variable -> this is a variable which tracks on the value of each iteration

in -> in is a keyword used to specify the sequence we want to iterate over

sequence -> this is the actual set of elements that we want to loop through it can be anything like list,
String, range, tuples ...ect



"""



#examples
# for i in range(1,6):
#     print(i)

# when you mentions the range make sure that you are mentions the max range + 1 at the last



# name = "Pavan"
# for i in range(1,11):
#     print(name)

# fruits = ["apple", "banana", "cherry", "orange"]
# for fruit in fruits:
#     print(fruit)


"""
nesting of the loops
--------------------
we can write one loop inside an other loop this concept we will call it as a nesting of the loops

syntax of nested for loop:
--------------------------
for out_var in outer_sequence:
    #outer_loop code
    for inner_var in inner_sequence:
        #inner_loop code
    #rest of the outer_loop code



"""
#program to print the * in square format
# for i in range (5):
#     for j in range (5):
#         print(" x ", end = " ")
#     print()

#program to print the * in right-angled triangle format
# for i in range (10):
#     for j in range (i):
#         print(" x ", end = " ")
#     print()

#program to print the * in pyramid style
#prints the stars in odd numbers like 1,3,5 ...etc
num = int(input("Enter a number: "))
for i in range(1, num + 1):
    for space in range(1, (num-i)+1):
        print(" ", end = " ")
    for col in range(1, 2*i):
        print("*", end = " ")
    print()

#prints the stars in even numbers like 2,4, 6 ..etc
num = int(input("Enter a number: "))
for i in range(1, num + 1):
    for space in range(1, (num-i)+1):
        print(" ", end = " ")
    for col in range(2, 2*i):
        print("*", end = " ")
    print()

#prints the stars in like real numbers 1,2,3,4,...etc
# for i in range(1, num + 1):
#     print(" "*(num-i), end = "")
#     print("* " * i)

# 10 -> 10 times
# first iteration - > print(" "*(num-i), end = "") will prints the 9 spaces
# print("* " * i) -> will prints 1 stars

# second iteration - > print(" "*(num-i), end = "") will prints the 8 spaces
# print("* " * i) -> will prints 2 stars

# .
# .
# .

# last iteration - > print(" "*(num-i), end = "") will prints the 0 spaces
# print("* " * i) -> will prints 10 stars


#what is the difference between the for loop and while loop
# 1. both are used to repeat the code execution
# 2. repeat the code for every item in sequence --> for loop
# 3. repeat code as long as the condition is true -> while loop

#how to skip or break the loops













