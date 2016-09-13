t = () # empty tuple
type(t)

one_element_tuple = (42, )
print('one_element_tuple :', one_element_tuple)
three_element_tuple = (1, 3, 5, )
print('three_element_tuple :', three_element_tuple)

a, b, c = 1, 2, 3
print(a, b, c)
a, b, c = c, b, a
print(a, b, c)
