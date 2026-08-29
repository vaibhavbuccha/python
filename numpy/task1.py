import numpy as np 
import sys
import time

a = np.array([1,2,3,4,5])

print(a[0:2])
print(a[0:3])
print(a[0:4])
print(a[0:5])

print(a[4:])
print(a[3:])
print(a[2:])
print(a[1:])

# How we can say numpy is faster than python list 

# python list
l = range(1000)

# numpy array
nl = np.arange(1000)

sizeOfL = sys.getsizeof(5)
sizeOfnl = nl.itemsize

print(f'Size of python list element {sizeOfL}')
print(f'Size of numpy array element {sizeOfnl}')


size = 10000000

l1 = range(size)
l2 = range(size)

start = time.time()

result = [(x+y) for x,y in zip(l1,l2)]

end = time.time()

print(f"Time taken by python list is {(end-start)*1000}")

# numpy 

nl1 = np.arange(size)
nl2 = np.arange(size)

start = time.time()

result = nl1+nl2

end = time.time()

print(f"Time taken by numpy array is {(end-start)*1000}")

# When size is small the difference is not noticable
# When size is large the difference is noticable 