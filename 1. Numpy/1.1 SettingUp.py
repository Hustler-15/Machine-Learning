import numpy as np

#Creating an Array
list1 = [1,2,3,4,5]
npArray = np.array(list1)
print(npArray)

#To check the array location
print(npArray.data)  

#To check the datatype
print(npArray.dtype) 

#To check the shape
npArray2 = np.array([[1,2,3,4],
                    [4,6,7,8],
                    [9,10,11,12],
                    [0,0,0,0]])
print(npArray2.shape)   
