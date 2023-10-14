import numpy as np

#Neural Network Demo Example

input_size = 2
hidden_size = 3
output_size = 1

weight = np.random.randn(hidden_size, input_size) # 3x2
inputs = np.array([
    [3],
    [2],
])
print('Inputs:')
print(inputs)

bias = np.random.randn(3, 1)
print('Bias:')
print(bias)

layer1 = np.dot(weight, inputs) + bias
print("Layer:")
print(layer1)

weight_output = np.random.randn(hidden_size, output_size) # 3x1
bias_output = np.random.random((1, 2))

output = np.array([1])
final_output = np.dot(layer1.transpose(), weight_output) + bias_output # 1x1
print('Final Result')
print(final_output)

error = output - final_output

