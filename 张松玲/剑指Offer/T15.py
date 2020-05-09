import numpy as np

n = int(-987446)

count = 0
while n:
    n = n & (n - 1)
    n = np.asarray(n, dtype=np.int32)
    count = count + 1

print count
