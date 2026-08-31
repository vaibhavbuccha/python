"""
Task 6 — Mathematical operations

Given:

prices = np.array([100, 200, 300, 400, 500])

Calculate:

10% discount
Final prices
GST of 18%
Final price including GST

Try doing everything without loops.
"""


import numpy as np

prices = np.array([100, 200, 300, 400, 500])

discount = 0.10

discountPrices = prices*discount

finalPrices = prices-discountPrices

gst = 0.18

gstPrices = finalPrices*gst

finalPriceWithGST = finalPrices+gstPrices

print(f"10% discount {discountPrices}")

print(f"Final price {finalPrices}")

print(f"GST of 18% {gstPrices}")

print(f"Final price including GST {finalPriceWithGST}")