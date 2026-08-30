"""
Task 4 — 2D array indexing

Create:

10 20 30
40 50 60
70 80 90

Find:

50
First row
Last row
First column
Last column
20, 30, 50, 60
70, 50, 30
"""


import numpy as np 

arr = np.array([[10,20,30],[40,50,60], [70,80,90]])

print("Element at 1,1", arr[1,1])
print("First row", arr[0])
print("Last row", arr[-1])
print("First Column", arr[:,0])
print("Last column",arr[:, -1])

arr2 = arr.flatten()

print("20, 30, 50, 60", arr[0:2, 1:3])

print("70, 50, 30", arr2[6:1:-2])