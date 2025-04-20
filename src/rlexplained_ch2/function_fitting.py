import random

import numpy as np
from matplotlib import pyplot as plt

from src.rlexplained_ch2.BucketMemory import BucketMemory
from src.rlexplained_ch2.Sigmoid import Sigmoid

nSteps=1000
alpha=0.1
mem = BucketMemory()
sigmoid = Sigmoid()

for i in range(1, nSteps):
    x = random.uniform(-10, 10)
    hc = mem.get_hc(x)
    fappr = mem.readAtHash(hc)
    e = sigmoid.compute(x)-fappr
    mem.writeAtHash(hc,fappr+alpha*e)

xvec=np.arange(-10,10,0.1)
yvec=[]
for x in xvec:
    y=mem.read(x)
    yvec.append(y)  # Store current weight value

plt.plot(xvec, yvec)  # Plot each alpha on the same graph
plt.xlabel("x")
plt.ylabel("y")
plt.title("Sigmoid")
plt.grid(True)
plt.show()