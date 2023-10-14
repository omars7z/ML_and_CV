import matplotlib.pyplot as plt
import numpy as np

shape = plt.imread("screenshot5.png")

array = np.array([
                 [0, 2, 3, 4],
                 [1, 2, 3, 4],
                 [1, 2, 3, 4],
                 [1, 2, 3, 6]
                ])

array2 = np.array([
                 [0, 1, 0, 1],
                 [1, 0, 1, 0],
                 [0, 1, 0, 1],
                 [1, 0, 1, 0]
                ])
print(array.shape)
array3 = np.array([
                 [0, 1, 1, 1, 0],
                 [0, 1, 0, 0, 0],
                 [0, 1, 1, 1, 0],
                 [0, 0, 0, 1, 0],
                 [0, 1, 1, 1, 0],
])
print(type(array))
plt.imshow(array3, cmap='Blues')
plt.show()
