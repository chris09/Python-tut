my_list = []
print('my_list', my_list)

another_list = list()
print('another_list', another_list)

list_a = [1,2,3,4,5]
print('list_a :', list_a)
list_a.append(6)
print('list_a.append(6) :', list_a)
print('list_a.pop()', list_a.pop())
list_b = [6,7,8,9,10]
list_a.extend(list_b)
print(list_a)
print('count 1 in list_a :', list_a.count(1))
print('find 1 index in list_a :', list_a.index(1))
list_a.insert(10, 11)
print(list_a)
list_a.remove(11)
print(list_a)
list_a.reverse()
print(list_a)
list_a.sort()
print(list_a)
print('minimum in list_a', min(list_a))
print('maximum in list_a', max(list_a))
print('sum list_a', sum(list_a))
print('len in list_a', len(list_a))

list_c = list('hello')
print(sorted(list_c))

# multiple list
from operator import itemgetter
a = [(1,2),(3,4),(5,3),(6,3),(5,1)]
print(sorted(a))
print(sorted(a, key=itemgetter(0,1)))

# permutations
from itertools import permutations
print(list(permutations('ABC')))
