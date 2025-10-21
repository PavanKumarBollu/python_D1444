"""
slicing allows us to extract some portion of the large arrays from numpy
for doing the slicing we need to tell the following
[start:stop:step]


"""


import numpy as np
# arr_num = np.array([1,2,3,4,5,6,7,8,9],dtype = int)
# print(arr_num)
# sliced_num = arr_num[3:7]
# print(sliced_num)
#
# sliced_num_step = arr_num[1::2]
# print(sliced_num_step)



#we can use negitive indexing also just as how we have used in the string and list ..etc
# condition = arr_num %2 == 0
# arr_even = arr_num[condition]
# print(arr_even)



# arr_multi = np.array([[1,2,3],[4,5,6],[7,8,9]],dtype = int)
# print(arr_multi)
# print(arr_multi[2,:])
# print(arr_multi[:,0])
#
#
# # updating a single value using the index
# arr_multi[1][1] = 55
# print(arr_multi)


# copy , view
#copy will create the copy of the array even any change in the copied array will not affect the original array
# arr_multi = np.array([[1,2,3],[4,5,6],[7,8,9]],dtype = int)
# print(arr_multi)
# arr_multi_copy = arr_multi.copy()
# arr_multi_copy[0][2] = 33
# print(arr_multi_copy)

#view is going to just create one more instance of the array in the memory and it will be referenced to the same location
# so any modification in the view() will effect the original array
# arr_multti_view = arr_multi.view()
# arr_multti_view[0][2] = 33
# print(arr_multi)
# print(arr_multti_view)
#
#


# to check the shape of the array then you can use the shape method
# print(arr_multi.shape)


arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],dtype = int)
print(arr)

# arr_reshaped = arr.reshape((5,2))
# print(arr_reshaped)

arr_reshaped = arr.reshape(-1,3)
print(arr_reshaped)




