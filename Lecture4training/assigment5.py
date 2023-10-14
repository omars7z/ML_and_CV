import numpy as np
import random

a = np.random.randint(low=0,high=11, size=(3, 3))
t = np.zeros(shape=(a.shape[1], a.shape[0]))

for i in range(a.shape[0]):
    for j in range(a.shape[1]):
        t[j][i] += a[i][j]

print(a)
print(t)