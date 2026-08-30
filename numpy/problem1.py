"""
Task 1 — Create and inspect arrays

Create NumPy arrays for:

[10, 20, 30, 40, 50]
A 3×3 matrix
An array containing numbers from 1–20

Print:

Array
Shape
Number of dimensions (ndim)
Data type (dtype)
Number of elements (size)
"""


import numpy as np

arr = np.array([10,20,30,40,50])

arr2 = np.array([[1,2,3],[4,5,6],[7,8,9]])

arr3 = np.arange(1,21)


print("Printing arrays")
print(arr)
print(arr2)
print(arr3)

print("Shapes of the arrays")
print(arr.shape)
print(arr2.shape)
print(arr3.shape)

print('number of dimensions')
print(arr.ndim)
print(arr2.ndim)
print(arr3.ndim)

print("dataType of the array")
print(arr.dtype)
print(arr2.dtype)
print(arr3.dtype)


print("size of the array")

print(arr.size)
print(arr2.size)
print(arr3.size)
