"""
Task 8 — Boolean filtering

Given:

marks = np.array([45, 78, 92, 33, 67, 89, 21, 76, 55])

Find:

Students who scored > 60
Students who scored < 40
Students who scored between 50 and 80
Count students who passed

Hint: Boolean masking.
"""

import numpy as np
marks = np.array([45, 78, 92, 33, 67, 89, 21, 76, 55])

conditions = [
    marks>60,
    marks<40,
]

choices = ['passed', 'failed']

result = np.select(conditions, choices, default="average")
print('Result: ', result)


print("Count students who passed", len(marks[marks>60]))