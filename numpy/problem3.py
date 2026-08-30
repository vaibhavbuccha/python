"""
Task 3 — Array indexing

Given:

arr = np.array([10, 20, 30, 40, 50, 60, 70])

Find:

First element
Last element
Third element
First 3 elements
Last 3 elements
Every second element
Array in reverse
"""

import numpy as np

arr = np.array([10,20,30,40,50,60,70])

print("First element :", arr[0])

print("Last element : ", arr[-1])

print("Third element :", arr[2])

print("First 3 elements", arr[:3])

print("Last 3 elements :", arr[-3:])

print("Every second element : ", arr[::2])

print("Array in reverse : ", arr[::-1])
