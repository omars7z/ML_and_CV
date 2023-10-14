import math
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def tanh(x):
    return 2 / (1 + np.exp(-2 * x)) - 1

def relu(x):
    return np.maximum(0, x)

print(sigmoid(np.array([20, 5, 61])))
print(sigmoid(np.array([20, 5, 61])))
print(relu(np.array([-1000, 20, 30])))