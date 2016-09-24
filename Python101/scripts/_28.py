x = [5,6,2,1,6,7,2,2,6,7,2]

x.append(55)
print(x)

x.insert(2, 99)
print(x)

x.remove(2)  # remove first elements
print(x)

x.pop()
print(x)

print(x.count(2))

x.sort()
print(x)
x.reverse()
print(x)

# slice
y = x[:] # copy
print(y)
y = x[::-1] # reverse
print(y)
