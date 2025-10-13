"""
dictionary is collection key-value pairs
to map the elements with the associated keys then we will use the dictionary

things to remember about dictionary is:
key-value pairs
unordered -> no order is maintained like list
mutable
dynamic in size
we can store different types of data
we will access the elements by using the key
IMP :- no duplicate keys
...
...
etc



"""
from Datatypes import phone_no

# Example dictionary creation

# user = {
#     "name": "Ganesh",
#     "age": 22,
#     "height": 70,
#     "weight": 80,
#     "phone_no" :1234567890
# }

# use cases of the dictionary is
""" 
-> counting the occurrence of items in a collection
-> store the information with some meaning lables 
.
.
.
-> messages with types from the server



"""
# we can create empty dictionary too
dic_empty = {}

# we can create the dictionary using the dict() constructor
dic_constructor = dict()
dic_constructor_1 = dict(name ="Ganesh", age = 22, height = 70, weight = 80, phone_no = "1234567890")


#methods on dictionary

# copy() creates the copy of the dictionary
user = {
    "name": "Ganesh",
    "age": 22,
    "height": 70,
    "weight": 80,
    "phone_no" :1234567890
}

# print(user)
# new_user = user.copy()
# print(new_user)

#get(key ,  default=None) return the values associated with the key if found otherwise it will return the default value
# print(user.get("name"))
# print(user.get("name","User_name_Is_Not_Available"))

#items() will return the all key value pairs in the dictionary
# print(user.items())
#
# #key() will return the all keys inside the dictionary
# print(user.keys())
#
# #values() will return all the values inside the dictionary
# print(user.values())


#pop() by using the pop we can remove any item from the dictionary if key not found then error
# print(user)
# print(user.pop("phone_no"))
# print(user)

user.update({"location":"Hyderabad"})
print(user)














