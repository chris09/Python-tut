num_list = [12,23,2,2,3,1,3,52,44,65,4,12]
fruit_list = ['apple', 'banana', 'cherry']
student_dict = {
    'id' : 1,
    'name' : 'chris',
}

for i in num_list:
    print(i)

for i in range(10):
    print(i)

for i in range(1,100,3):
    print(i)

for fruit in fruit_list:
    print(fruit)

for key in student_dict:
    print(key)

for key, value in student_dict.items():
    print(key, value)
