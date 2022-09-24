import matplotlib.pyplot as plot
import numpy as np
import math

P = np.array([(10,10),(20,10)])

R = np.array([(0,10),(0,10)])

def hermite(t): return P[0]*(2*t**3-3*t**2+1)+P[1]*(-2*t**3+3*t**2)+R[0]*(t**3-2*t**2+t)+R[1]*(t**3-t**2)
def function_Hermite():
    fig, ax = plot.subplots()
    t = np.arange(0,1,0.01)
    iMax,c = 1000, 0
    points = np.zeros((2, iMax))
    for i in t:
        points[:,c] = hermite(i)
        c = c+1
    points = points[:, 0: t.size]
    plot.xlim((0,22))
    plot.ylim((0, 12))
    plot.grid(True)
    plot.plot(points[0, :], points[1, :])


    #ax.arrow(10,10,10,10)

    plot.show()
if __name__ == '__main__':
    function_Hermite()