"""
Task 10 — Random numbers

Generate:

10 random integers between 1–100
5×5 random matrix
10 random floating-point numbers
Random numbers following a normal distribution

Then calculate their mean and standard deviation.
"""

import numpy as np

a = np.random.randint(1,100,10)

print('a :', a)

b = np.random.rand(5,5)
print('b :', b  )

c = np.random.randn(10)
print('c :', c)

d = c.mean()
print('d :', d)

e = c.std()
print('e :', e)