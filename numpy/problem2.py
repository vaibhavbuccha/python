"""
Task 2 — Different ways to create arrays

Create arrays using:

np.zeros()
np.ones()
np.full()
np.arange()
np.linspace()

For example:

5 zeros
10 ones
3×3 matrix filled with 7
Numbers from 1 to 100 with step 5
10 equally spaced numbers between 0 and 1
"""

import numpy as np

arrZeros = np.zeros(5)

arrOnes = np.ones(10)

arrFull = np.full((3,3,3),4)

arrArange = np.arange(1,100,3)

arrLinspace = np.linspace(1,100, 30)

print(f"Using zeros {arrZeros}")
print(f"Using Ones {arrOnes}")
print(f"Using Full {arrFull}")
print(f"Using Arange {arrArange}")
print(f"Using Linspace {arrLinspace}")