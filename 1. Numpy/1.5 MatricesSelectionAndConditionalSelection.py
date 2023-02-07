import numpy as np
arr = np.array([[7,8,9,6],[8,5,2,1],[8,8,6,2]])
print(arr)

print(arr[1])

print(arr[1][3]) #To access matrix

print(arr[1,3]) #another method

#slicing
print(arr[1:,0:])
print(arr[:,2:3])

print(arr[1:,2:])

print(arr[:,1:3])

arr2 = np.arange(0,10)
print(arr2[arr2>4] )

#behind the scene
arr3 = arr2>5
print(arr3)
print(arr2[arr3])