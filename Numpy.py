"""
Numpy --> it a s library of numerical computing in python we call it as a Numerical Python
we will use this to work with 2d arrays,matrix ..etc types of data


characteristics of numpy
------------------------
multidimensional arrays
element wise operations
random number generations
collaborating with other libraries

"""
#
# import numpy as np
# print(np.__version__)
"""
numpy datatypes

int64, int32, int16, int8 --> Signed DataTypes

"""
import numpy as np
arr = np.array([1,2,3,4,5], dtype=np.int32)
print(arr,type(arr))


"""
uint64, uint32, uint16, uint8 --> unSigned Datatypes
"""
import numpy as np
arr_u = np.array([1,2,3,4,5], dtype=np.uint32)
print(arr_u, type(arr_u))

"""
float64, float32, float16
"""
arr_f = np.array([1.0,2.5,3.5,5.0], dtype=np.float32)
print(arr_f, type(arr_f))

"""
bool type of data
"""

import numpy as np
arr_bool = np.array([True, True, False], dtype=np.bool)
print(arr_bool, type(arr_bool))


"""object creation in numpy"""

import numpy as np
arr_object = np.array(['PK',5.9,True,"120kg"], dtype=object)
print(arr_object, type(arr_object))

"""
String Type
"""
arr_string = np.array(["BMW", "AUDI", "Maruthi"], dtype=str)
print(arr_string, type(arr_string))

"""
Creating an array with random value and zero as default value and 1 as default value
"""

import numpy as np
arr_zeros_default = np.zeros(5, dtype = int)
print(arr_zeros_default)

import numpy as np
arr_ones_default = np.ones(5, dtype = int)
print(arr_ones_default)


import numpy as np
arr_rand_value = np.random.rand(5,5)
print(arr_rand_value)

#by using the index value we can access like following
print(arr_rand_value[0][0]) #prints the first element


arr_rand_int = np.random.randint(1,10,(5,5))
print(arr_rand_int)


arr_twod = np.array([[1,2,3],[4,5,6],[7,8,9]],dtype = int)
print(arr_twod)

