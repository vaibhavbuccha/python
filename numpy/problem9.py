"""
Task 9 — Replace values

Given:

temperatures = np.array([22, 25, 31, 35, 18, 40, 28])

Replace:

Temperature > 30 → "Hot"
Temperature < 20 → "Cold"
Everything else → "Normal"

Try using NumPy rather than a Python for loop.
"""

import numpy as np

temperatures = np.array([22, 25, 31, 35, 18, 40, 28])

conditions = [
    temperatures > 30,
    temperatures < 20
]
choices = ["Hot", "Cold"]

# Categorize temperatures, default to "Normal"
result = np.select(conditions, choices, default="Normal")

print("Original Temperatures:", temperatures)
print("Categorized Temperatures:", result)

