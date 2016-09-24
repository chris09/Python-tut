import numpy as np


a = np.arange(5)

print(a)
print(a.dtype)
print(a.shape)

# multidimensional array
m = np.array([np.arange(2), np.arange(2)])
print(m)
print(m.dtype)
print(m.shape)


# Stacking arrays
a = np.arange(9).reshape(3, 3)
print(a)
b = 2 * a
print(b)

c = np.hstack((a, b))
print(c)
c = np.concatenate((a, b), axis=1)
print(c)

c = np.vstack((a, b))
print(c)
c = np.concatenate((a, b), axis=0)
print(c)
