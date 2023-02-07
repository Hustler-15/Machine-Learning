import numpy as np

arr = np.linspace(1,10,11)       #It will distribute data in 10 parts from start to end not end-1
print(arr)

print(np.random.rand(10))         #It will 10 random values beteen 0 to 1

print(np.random.rand(2,3))       #It will give the value in matrix

arr =  np.random.randn(10)        #It will give normal distribution and the range is -4 to 4  After this learn normal and uniform distribution
print(arr)

print(arr.min())

print(arr.max())

print(arr.mean())

print(arr.argmin())          #Index of minimum value in array

print(arr.argmax())