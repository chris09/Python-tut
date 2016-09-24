# class function
def example(a, b, **kw):
    return a * b

print(type(example))
print(example.__code__.co_varnames)
print(example.__code__.co_argcount)


mersenne = lambda x: 2 ** x - 1
print(type(mersenne))
print(mersenne(4))
