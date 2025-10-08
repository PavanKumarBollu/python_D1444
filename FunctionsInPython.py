"""
in python function is a reusable block of code which performs a specific tasks.

Types of functions in python
1. User Defined
2. Built-In Functions


--> user defined function are created by the user (the entire function logic is writenned by the programmer only)
--> built-in functions are already available in the python lang it self

Examples : int() , print() , input()...etc functions are inbuilt functions
Examples : addition(), subtraction(), is_eligible() ..etc are user defined functions



syntax of functions in python
-----------------------------


def function_name(parameters):
    #function_Body(lines of code )
    # return(optional)

def -> is a keyword to indicate to the interpreter saying that we are gonna create a function

function_name -> name of the funtion which you want to create

parameters -> inputs to the function, parameters are also called as arguments
    but the parameters are name of the variables inside the function () but arguments are the actual values
    which are passed to the function

function_body -> functionality of the function which is created

return -> used to return some value back to the calling thing -> optional if we don't want to return anything


"""

#examples
def add(a, b):
    print(a + b)

add(10,20)
add(15 ,25)


def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b
def division(a, b):
    return a / b

# until we call the function with the function name we will not see any results




"""
functions can also have the default values for the parameters allowing us to call the functions without passing the argumets

"""

def greet(name, greeting="HELLO"):
    message = f"{greeting}, {name}"
    return message

msg_1 = greet("Pavan", "Hello, How are you..?")
msg_2 = greet("pavan")

print(msg_1)
print(msg_2)