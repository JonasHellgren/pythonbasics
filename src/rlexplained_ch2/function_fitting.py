import random

from src.rlexplained_ch2.BucketMemory import BucketMemory

nSteps=1000
alpha=0.1
mem = BucketMemory()
sigmoid = Sigmoid()

for i in range(1, nSteps):
    x = random.uniform(-10, 10)
    hc = mem.get_hc(x)
    fappr = mem.read(hc)
    e = sigmoid.f(x)-fappr
    mem.save(hc,fappr+alpha*e)
