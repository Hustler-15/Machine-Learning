import numpy as np
arr1 = np.arange(0,10)

print(arr1[1:5])       #same as string slicing

print(arr1[0:15])      #It will print till last value and returns no error
 
 #We can broadcast value in numpy arrays
arr1[1:5] = 71
print(arr1) 

arr1 = np.arange(0,10)
print(arr1)

#To get subset of a value

arr2 = arr1[1:5]
print(arr2)

arr2[:] = 25
print(arr2)
print(arr1)  #values will be changed in both array bcz python uses references
arr1 = np.arange(0,10)
print(arr1)

#How to copy array
arr2 = arr1.copy()
arr2[5:]=77
print(arr2)