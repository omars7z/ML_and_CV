import numpy as np
import random

arr = []
# for i in range(5):
    #np.random.randint([])
    #arr[i].append(randint(0, 10))

a = np.random.randint(low=10, size=(3, 3))
print('Matrix: ', a)

t= np.transpose(a)
print('Transpose: ', t)

d = np.linalg.det(a)
print('Determinant: ', d)

if d!=0:
    print('Inverse: ',np.linalg.inv(a))
else:
    print('Inverse doesn\'t exist')
