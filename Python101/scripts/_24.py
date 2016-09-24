import statistics
import random


example_list = [random.randint(1, 100) for i in range(1000000)]
print('list is', example_list)
# mean 平均數
x = statistics.mean(example_list)
print('mean is', x)
# standard Deviation 標準差
y = statistics.stdev(example_list)
print('standard deviation is', y)
# variance 變異數
z = statistics.variance(example_list)
print('variance is', z)


# count mind
# 1,2,3,4,5
# n1 + n2 + n3 + n4 + n5 / n
# stdev = (n1-mean)**2 + (n2-mean)**2 + ... / n
# mean = 15/5 = 3
# variance = stdev ** 2
