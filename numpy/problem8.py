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

print("Students who scored > 60", marks>60)

print("Students who scored < 40", marks<40)

print("Students who scored between 50 and 80", (marks>50) & (marks<80))

print("Count students who passed", len(marks[marks>60]))