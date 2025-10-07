#Operators
"""
operators are symbols or special keywords that are used to perform some operations

operators are used to perform some mathematical operations inside the program like addition subtraction multiplication ..etc



Operator , Operands
Example a + b -> a,b are operands and +  is the operator

"""


"""
Types of Operators in python

Arithmetic Operators
Comparison Operators
logical operators
assignment operators
Identity Operators
Bitwise Operators
membership operators

"""
#Arithmetic Operators

"""
+
-
*
/
//
%
** 

"""
#Examples
# a=10
# b=20
# c=a+b
# print(c)
#
# d=20
# e=10
# f=d-e
# print(f)
#
# m = 10
# n = 3
# o = m*n
# print(o)
#
# j = 15
# k = 2
# l = j/k
# print(l)

# x = 15
# y = 2
# z = x//y # quotient  15 / 3 (3 * 5 = 15 )-> 0
# # 15 / 2 ( 2 * 7.5(7 will be the answer in this case = 10 )-> 0
# print(z)
#
# p = 5
# q = 2
# r = p**q
# print(r)


#Comparison Operators

"""
==
>=
<=
>
<
!= 
"""
#examples
#
# print(a!=b)
# print(m==n)
# print(j>=k)
# print(x<=y)
# print(p<q)
# print(p>q)
# print(1>0)
# print()
# print(True>False)
# print(False > True)
# print(True>=False)
# print(False >= True)
# print(False == True)

# logical operators


"""
AND
OR
NOT

"""

#examples
# print(x > 5 and y < 4)
# print(x > 0 or y > 0)
# print(not x>0)
# print(not not x>0)





# Assignment Operators



"""
Assignment operators are used to perform basic arithmatic operations and assign back 
the values to the same variable instead of creating new variable

=
+=
-=
*=
/=
%=
**=
//=

"""

#assignment operators
print("assignment operators")
x = 25
print(x)
x+=2 # X = X + 2 (Increment -> x += 1 -> x = x + 1 Ex : x = 2 -> 3 , 4, 5, ..etc
print(x)
x-=2
print(x)
x*=2
print(x)
x/=3
print(x)
print()

#Membership operators

"""
in (membership)
not in (negated membership)

"""

print("Membership operators")

fruits = ["apple", "orange", "banana"]
print(fruits)

is_avaliable = "Banana" in fruits
print(is_avaliable)

fruit = "graphs"
is_not_avaliable =  fruit not in fruits
print(is_not_avaliable)#True


#Identity Operators
print(fruit is fruits)#false
print( fruit is not fruits)#true



# Bitwise Operators
res = 2 & 5 # 2 -> 0010 , 5 -> 0101  -> 0000 -> 0

"""
2 -> 0 0 1 0 
5 -> 0 1 0 1
a -> 0 0 0 0 -> 0 
"""

print(res) #0 AND
print(2 | 5) #7 OR
"""
2 -> 0 0 1 0 
5 -> 0 1 0 1
a -> 0 1 1 1 -> 7
"""
print(2 ^ 5) #7 XOR
"""
2 -> 0 0 1 0 
5 -> 0 1 0 1
a -> 0 1 1 1 -> 7
"""

print(2 << 5) #leftShift
"""
 2 ^ 5 -> 2 * 2 ^ 5 -> 64
"""
print(2 >> 5) #right shift
"""
 2 >> 5 -> 2 / 2 ^ 5 -> 2 / 32 -> 0.0625 -> 0
"""
