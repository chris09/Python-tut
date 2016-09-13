for number in [1,2,3,4]:
    print(number)

for number in range(5):
    print(number)

surnames = ['Rivest', 'Shamir', 'Adleman']
for surname in surnames:
    print(surname)

for position, surname in enumerate(surnames):
    print(position, surname)

people = ['Jonas', 'Julio', 'Mike', 'Mez']
ages = [25, 30, 31, 39]
for position in range(len(people)):
    print(people[position], ages[position])

import random
from faker import Factory
fake = Factory.create()
for i in range(random.randint(0, 30)):
    print(fake.name())
    print(fake.address())


people = ['Jonas', 'Julio', 'Mike', 'Mez']
ages = [25, 30, 31, 39]
nationalities = ['Belgium', 'Spain', 'England', 'Bangladesh']
for data in zip(people, ages, nationalities):
    person, age, nationality = data
    print(person, age, nationality)
