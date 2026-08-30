"""
Task 5 — Modify arrays

Given:

arr = np.array([10, 20, 30, 40, 50])

Perform:

Change 30 → 100
Add 10 to every element
Multiply every element by 2
Replace values greater than 50 with 0
"""

import numpy as np

arr = np.array([10, 20, 30, 40, 50])

arr[2] = 100

print(f"Change 30 → 100 {arr[2]}")

print(f"Add 10 to every element {arr+10}")

print(f"Multiply every element by 2 {arr*2}")

print("Replace values greater than 50 with 0", np.where(arr>50,0,arr))