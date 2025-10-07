"""
while loop

while is control statement in python which is used to execute some lines of code repeatedly until the condition is false

while syntax:

while condition:
    #code(lines of code ) to be executed repeatedly

-> in while loop there should be a way to stop the program otherwise it would result in infinite loop


"""

# while examples
# count = 1
# while count <=10:
#     print(count)
#     count += 1


#
# count = 2
# while True:
#     print(count)
#     if(count == 2):
#         break


# write a program to print the even numbers until the user specified number
# if user has entered 6 -> 2 4 6

num = int(input("enter the max number"))

count = 1
while count <= num:
    if count % 2 == 0:
        print(count)
    count +=1












