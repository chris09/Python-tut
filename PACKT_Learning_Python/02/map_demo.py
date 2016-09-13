a = dict()
b = {}
c = dict(A=1, B=-1)
print(a, b, c)

a.update({'A': 'apple'})
print(a)
a.update(B='banana')
print(a)
a.pop('A')
print(a)
print(a.get('B'))

a.update(A='apple')
print(a)

for key, value in a.items():
    print(key, value)
