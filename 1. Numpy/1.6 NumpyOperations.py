import numpy as np

arr = np.array([0, 1, 2, 3, 4, 5])
print(arr)

print(arr*arr)  # To calculate square

print(arr+arr)

print(arr/arr)  # It will return nan at 0/0

print(arr+100)  # 100 will be added to individual elements

# refer numpy mathematical functions
print(np.square(arr))
print(np.sqrt(arr))
