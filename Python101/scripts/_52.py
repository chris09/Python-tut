from matplotlib import pyplot as plt
import csv
import numpy as np
from matplotlib.dates import datetime as dt


dates = []
values = []
with open('goog.csv') as csvFile:
    data = csv.reader(csvFile)
    count = 0
    for row in data:
        # print(row)
        count += 1
        if count > 1:
            row[0] = dt.datetime.strptime(row[0], '%Y-%m-%d')
            dates.append(row[0])
            values.append(row[1])

plt.plot(dates, values)

# use numpy read txt csv
# x, y = np.loadtxt('exampleFile.txt', unpack=True, delimiter=',')
# print(x)
# print(y)
# plt.plot(x, y)

plt.title('Epic Chart')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()
