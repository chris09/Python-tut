from matplotlib import pyplot as plt
from matplotlib import style

# download some matplotlib style
# style.use('')

x = [5,6,7,8]
y = [1,2,3,4]
x2 = [5,6,7,8]
y2 = [7,1,3,2]

# plt.scatter(x, y, color='orange')
# plt.scatter(x2, y2, color='skyblue')
plt.bar(x, y, color='orange', align='center')
plt.bar(x2, y2, color='skyblue', align='center')

plt.title('Epic Chart')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend()
plt.grid(True, color='r')
plt.show()
