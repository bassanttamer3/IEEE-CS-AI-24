# Create a 3x3 array that contains a diagonal of nines.
import numpy as np

array = np.zeros((3, 3))
np.fill_diagonal(array, 9)

print(array)

