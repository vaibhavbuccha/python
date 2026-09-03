"""
Task 11 — Reshape

Create:

arr = np.arange(1, 25)

Convert it into:

2×12
3×8
4×6
6×4
2×3×4

Then convert it back to 1D.
"""


import numpy as np

arr = np.arange(1,25)

a = arr.reshape(2,12)
print('2 x 12 :', a)

b = arr.reshape(3,8)
print('3 x 8 :', b)

c = arr.reshape(4,6)
print('4 x 6 :', c)

d = arr.reshape(6,4)
print('6 x 4 :', d)

e = arr.reshape(2,3,4)
print('2 x 3 x 4 :', e)

f = e.flatten()
print('flatten :', f)