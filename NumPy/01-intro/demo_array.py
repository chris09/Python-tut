import numpy as np


def pythonsum(n):
    a = [x for x in range(n)]
    b = [x for x in range(n)]
    c = []
    for x in range(len(a)):
        a[x] = x ** 2
        b[x] = x ** 3
        c.append(a[x] + b[x])
    return c


def numpysum(n):
    a = np.arange(n) ** 2
    b = np.arange(n) ** 3
    c = a + b
    return c

sum_arr = pythonsum(3)
numpy_arr = numpysum(3)

print(sum_arr)
print(numpy_arr.dtype)
print(numpy_arr)
