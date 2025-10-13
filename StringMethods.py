"""
When you talk about the string methods that means some in-built methods has already provided for us we just we
what are all they and how we can use them
What is String
How to define them
accessing
traversing
special operators
methods on strings


"""

#upper() and Lower() methods
# name = "aNDIP foundation madhapur hyderabad"
# name_upper = name.upper()
# print(name_upper)
# name_lower = name.lower()
# print(name_lower)
# name_capitalized = name.capitalize()
# print(name_capitalized)

#replace(oldValue, newValue)

# text_old = "andip foundation"
# text_replaced = text_old.replace("n", "N")
# print(text_replaced)


#strip() , lstrip(), rstrip()
# these are the functions which are used to remove white spaces, tabs newline ..etc

# text_value = "  python   "
# text_value_1 = " \n python   "
# # print(text_value)
# # print(text_value.strip())#python #removes the spaces from both sides of the string
# # print(text_value )
# # print(text_value.lstrip())#removes the spaces from only left side
#
# # print(text_value )
# # print(text_value.rstrip())#removes the spaces form right side only
#
# print(text_value_1)
# print(text_value_1.strip())


#split() split(sep=None, maxsplit=-1)

# str_python = "Python programming language is very easy and fun to learn it have very easy syntax "
# # print(str_python.split())
#
# print(str_python.split(" ", maxsplit=5))

#join(sequence(iterable))
# words = ["Anudip", "Foundation", "Madhapur"]
# print("#".join(words))
# print(" ".join(words))
# print("_".join(words))

# find(subString, start=0, end=-1)
# This method searches for the first occurrence of a subString which we have mentioned and returns in the index value
# where it is present if no substring is present then its gonna return -1


# str_python = "Python programming language is very easy and fun to learn it have very easy syntax very"
# ind = str_python.find("very")
# print(ind)

# ind = str_python.find("very", 35, -1)
# print(ind)


#count() counts the number of occurrences in the substring
#
# str_occ = str_python.count("very")
# print(str_occ)

#startswith() and endswith()

# str_python = "Python programming language is very easy and fun to learn it have very easy syntax very"
# print(str_python.startswith("Python")) #True
# print(str_python.endswith("Python")) #False
# print(str_python.endswith("very"))#True


#isalpha(), isdigit()
#isalpha is going to check weather the string contains only charecters
#isdigit() is going to check weather the string contains only digits
#if string contains both digits and characters then both of the above functions is going to return the result as false
# str_python = "Python programming language is very easy and fun to learn it have very easy syntax very"
#
# print(str_python.isalpha())#True
# print(str_python.isdigit())#False
# str_num = "123"
# print(str_num.isdigit())

# write a program to take the input from the user and remove all the digits in that numbers and print only characters

# u_input = input("Enter Anything Here to remove the digits : ")
#
# result = ""
# for char in u_input:
#     if char.isdigit():
#         continue
#     else:
#         result += char
# print(result)

#task ->
# write a program to take the input from the user and remove all the characters in that string and print only digits
# u_input = input("Enter a Anything here : ")
#
# characters = ""
# digits = ""
#
# for char in u_input:
#     if char.isdigit():
#         digits += char
#     elif char.isalpha():
#         characters += char
#     else:
#         continue
# print(f"total charecters present the given string {characters}")
# print(f"total digits present the given string {digits}" )









