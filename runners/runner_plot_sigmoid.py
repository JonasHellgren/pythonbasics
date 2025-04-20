import numpy as np
from matplotlib import pyplot as plt

from src.rlexplained_ch2.Sigmoid import Sigmoid

xvec=np.arange(-10,10,0.1)
yvec=[]
sigm=Sigmoid()

for x in xvec:
    y=sigm.compute(x)
    yvec.append(y)  # Store current weight value

plt.plot(xvec, yvec)  # Plot each alpha on the same graph
plt.xlabel("x")
plt.ylabel("y")
plt.title("Sigmoid")
plt.grid(True)
plt.show()
