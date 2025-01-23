import numpy as np

# Create an array of 10 zeros
zeros = np.zeros(10)

# Create an array of 10 ones
ones = np.ones(10)

# Create an array of 10 fives
fives = np.full(10, 5)

# Concatenate the arrays
result = np.concatenate((zeros, ones, fives))

print(result)