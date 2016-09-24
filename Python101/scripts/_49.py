from matplotlib import pyplot as plt
from matplotlib import style

# style.use('')

x = [5,6,7,8]
y = [1,2,3,4]
x2 = [5,6,7,8]
y2 = [3,4,5,6]

plt.plot(x, y, 'orange')
plt.plot(x2, y2, 'skyblue')
plt.title('Epic Chart')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.show()
