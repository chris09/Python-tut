my_name = 'Chris Yu'
my_age = 38
my_height = 74
my_weight = 180
my_eyes = 'Black'
my_teeth = 'White'
my_hair = 'Black'

a = b = c = 3
x, y = (3, 5)

print('Lets talk about %s' % my_name)
print("He's %d inches tall." % my_height)
print("He's %d pounds heavy." % my_weight)
print("Actually that's not too heavy.")
print("He's got %s and %s hair." % (my_eyes, my_hair))
print("His teeth are uaually %s depending on the coffee." % my_teeth)

# this line is tricky, try to get ti exactly right
print("If I add %d, %d, and %d I get %d." % (my_age, my_height, my_weight, my_age + my_height + my_weight))


print(a, b, c)
print(x, y)
