import math
import numpy as np
import matplotlib.pyplot as plt

g=9.81

class CannonDistance:
    def __init__(self, v0):
        self.v0=v0

    def d_calc(self, thetaDegr):
        thetaRad = thetaDegr*np.pi/180
        d = (self.v0**2)*np.sin(2*thetaRad)/g
        return d