import numpy as np
import matplotlib.pyplot as plt

x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 10, 20, 30, 40, 50])

plt.plot(x, y, marker='o')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Simple Line Plot")
plt.grid(True)
plt.show()