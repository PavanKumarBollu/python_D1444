"""
list is a in-built data structure in pytho to store the elements here elements in the sense we can store in thing
inside the list like characters and number ...etc


list is the very much used data set in realtime projects

features
ordered
mutable
heterogeneous -> can contain the different data types of elements
dynamic in size -> no fixed size is there for the list

"""
#example
# person = ["Ganesh",29, 'single', """this is multi line
# """, True, 102.25 ]
#
# print(person)

#things we can do on the list
# creating the list
# accessing the elements
# slicing the elments
# modifying


#accesing the list elements
# marks = [10,15,24,16,9,13]
# print(marks[0])#10
# print(marks[-1])#13
#
# #slicing
# print(marks[::])# [10, 15, 24, 16, 9, 13]
# print(marks[::-1]) # [13, 9, 16, 24, 15, 10]
# print(marks[:: 2]) # [10, 24, 9]
# print(marks[1:4]) # [15, 24, 16]


#modifing
# print(marks) # [10, 15, 24, 16, 9, 13]
# marks[0] = 11
# print(marks) # [11, 15, 24, 16, 9, 13]
# marks[4] = 17
# print(marks) # [11, 15, 24, 16, 17, 13]

# function on the list

"""
python has built -in function to manipulate the data in the list 

"""

# user = ["Ganesh", 23, 12345678, "gmail.com", 5.7, "120kg"]


#len() find the total number of elements in the list
# print(len(user)) #6

#append() adds an new item to the existing list
# user.append("python")
# print(user)


#insert()  will inserts the elements at specified position(index)
# print(user)
# user.insert(1,"Kumar")
# print(user)

nums = [10,11,10,12,10,13]
#remove() removes the first occurrence of a specified value for the list
# print(nums)
# nums.remove(10)
# print(nums)

#pop() removes and gives you the removed at in return at a specified index
# if no index is menetioned then it will remove the last elements and returns the last elements
# print(nums)
# print(nums.pop(2))
# print(nums)

#index() returnd the first occurrence index value

# print(nums.index(10))#0

# to count the elements repetition then we can use the count() function

# print(nums.count(10))


#sorting the list in aschending order

# print(nums)
# nums.sort() #modifing the existing list
#
# print(nums)

# but if we want a new list in sorting order without modifing the original list
# then we can use sorted function


# print(nums)
# new_list =  sorted(nums)
# print(new_list)


#reverse() to reverse the list order
# nums = [5,3,2,89,65,47,584,642,35,31,64,74]
# print(nums)
# nums.reverse()
# print(nums)

# convert the list in reverse order
# by using the sort and reverse functions we can archive this

# nums = [5,3,2,89,65,47,584,642,35,31,64,74]
# print(f"before sorting the list {nums} ")
# nums.sort()
# print(f"after sorting the list {nums} ")
# nums.reverse()
# print(f"list is deschending order {nums} ")

# nums = [5,3,2,89,65,47,584,642,35,31,64,74]
# print(f"before sorting the list {nums} ")
# nums.sort()
#
# print(f"after sorting the list {nums} ")
# desc_num = sorted(nums, reverse=True)
#
# print(f"list is deschending order {desc_num} ")

#travesing the list
# nums = [5,3,2,89,65,47,584,642,35,31,64,74]
# for num in nums:
#     print(num)

# for i in range(len(nums)):
#     print(nums[i])



#comprehension

# fruits =  ['apple','kiwi','orange','mango']
# new_list = []

# for fruit in fruits:
#     if "a" in fruit:
#         new_list.append(fruit)
#
# print(new_list)



# fruits =  ['apple','kiwi','orange','mango']
# print(fruits)
#
# new_list = [fruit for fruit in fruits if "a" in fruit]
#
# print(new_list)



