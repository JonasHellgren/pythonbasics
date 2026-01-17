import numpy as np
import matplotlib.pyplot as plt
import sys, os
# TCL_LIBRARY: C:\Users\jonashe2\AppData\Local\Programs\Python\Python313\tcl\tcl8.6
# TK_LIBRARY: C:\Users\jonashe2\AppData\Local\Programs\Python\Python313\tcl\tk8.6

x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([0, 10, 20, 30, 40, 50])

plt.plot(x, y, marker='o')
plt.xlabel("x")
plt.ylabel("y")
plt.title("Simple Line Plot")
plt.grid(True)
plt.show()