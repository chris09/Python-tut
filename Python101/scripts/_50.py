from matplotlib import pyplot as plt
from matplotlib import style

# download some matplotlib style
# style.use('')

x = [5,6,7,8]
y = [1,2,3,4]
x2 = [5,6,7,8]
y2 = [3,4,5,6]

plt.plot(x, y, 'orange', linewidth=5)
plt.plot(x2, y2, 'skyblue', linewidth=10)
plt.title('Epic Chart')
plt.xlabel('X Axis')
plt.ylabel('Y Axis')
plt.legend()
plt.grid(True, color='r')
plt.show()
