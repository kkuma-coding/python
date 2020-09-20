# https://cs231n.github.io/python-numpy-tutorial/#lists

import numpy as np

input = [10,9,2,5,3,7,101,18]
print (type(input))

a = np.array([1, 2, 3]) # Create a rank 1 array
print (type(a))         # prints "<class 'numpy.ndarray'>"
print (a.shape)         # Prints "(3,)"
print (a[0], a[1], a[2])
a[0] = 5
print (a[0], a[1], a[2])
print (a)

b = np.array([[1, 2, 3], [4, 5, 6]])
print (b.shape)
print (b[0, 0], b[0, 1], b[1, 0])