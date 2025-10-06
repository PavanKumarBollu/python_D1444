"""
Data types are nothing but the type of data which you want to work or you want to collect from the user
or you want to do some operation on it ...etc and store inside the variables

"""

""" different types of datatypes in python

whole numbers
decimal numbers
Boolean values
Strings values
list tuple dictionary set ..etc
"""

#whole number
age = 123
phone_no = 1234567890
aadhar_no = 123412341234


#decimal Numbers
bill_amount = 100.50
Pi = 3.147
cgpa = 8.5
petrol_rate = 110.9

#Boolean values
# when ever you are creating the boolean values it is suggested that the variable name should start with (is_) followed by name

is_eligible = True
is_completed = False


""" when you type boolean values it should be Either True or False other values we can't consider as boolean values 
if you try to store them as boolean values then it will trough an error

Ex : TRUE or FALSE fALSE TRue 

"""

# is_tested_possitive = TRUE
# is_tested_possitive = FALSE
# is_tested_possitive = falSE


# is_interested =bool(input("Are you interested ?"))
# print(is_interested)
# print("Type of Is_interested ",type(is_interested))


#String Datatype
"""
Anything you take it from the user that will be a string at the begging latter we will convert that values into specific 
type however we want
"""

#String is a special data type in python which will provide bunch of inbuit methods to work on

name = "Pavan"
print(name)
print(name.upper())