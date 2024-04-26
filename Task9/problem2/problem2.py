import numpy as np
array = np.arange(2, 34, 2)
array = array.reshape(4, 4)
mean = np.mean(array)
std = np.std(array)
halfStd = 0.5 * std
lower_bound = mean - halfStd
upper_bound = mean + halfStd
values = array[(array > lower_bound) & (array < upper_bound)]

print(array)
print("----------------")
print(values)
