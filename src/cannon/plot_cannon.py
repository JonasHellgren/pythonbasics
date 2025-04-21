import numpy as np
from matplotlib import pyplot as plt

from src.cannon.CannonDistance import CannonDistance

v0=300 #m/s

theta_vec=np.arange(2,80,1)
d_vec=[]
d_calc=CannonDistance(v0)

for theta in theta_vec:
    d=d_calc.d_calc(theta)
    d_vec.append(d)  # Store current d value

plt.plot(theta_vec, d_vec)  # Plot each alpha on the same graph
plt.xlabel("Angle theta (degrees)")
plt.ylabel("Distance (m)")
plt.title("Cannon")
plt.grid(True)
plt.show()