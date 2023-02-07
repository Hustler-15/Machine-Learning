import numpy as np

#To create a range of array
arr1 = np.arange(1,10)
print(arr1)

arr2 = arr1.reshape(3,3)    #It will reshape and if values are less then it will give error
print(arr2)

#To create array of zeros or ones
one = np.ones(10)
print(one)

#in particular dimension with type int
one = np.ones((2,3,4),int)
print(one)

#To create an identity matrix
ident = np.eye(3,dtype = int)         #It will create 3*3 Identity matrix
print(ident)