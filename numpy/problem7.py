"""
Task 7 — Statistics

Given:

marks = np.array([78, 85, 92, 67, 88, 95, 73, 81])

Calculate:

Mean
Median
Minimum
Maximum
Standard deviation
Variance
Total
Average
"""

import numpy as np

marks = np.array([78, 85, 92, 67, 88, 95, 73, 81])

print("Mean", np.mean(marks))

print("Median", np.median(marks))

print("Minimum", np.min(marks))

print("Maximum", np.max(marks))

print("Standard deviation", np.std(marks))

print("Variance", np.var(marks))

print("Total", np.sum(marks))

print("Average", np.sum(marks) / len(marks) )