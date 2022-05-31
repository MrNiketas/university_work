from cProfile import label
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

def annotate_points(ax, A, B):
    for xy in zip(A, B):
        ax.annotate('(%s, %s)' % xy, xy=xy, textcoords='offset points')

points = [(3.28,0.00),(4.00,0.50),(4.40,1.0),(4.60,1.52),(5.00,2.5),(5.00,3.34),(4.70,3.8)]
points = points + [(4.50,3.96),(4.20,4.0),(3.70,3.90),(3.00,3.5),(2.00,2.9)]
x, y = zip(*points)
l=len(x)
fig = plt.figure()
ax = fig.add_subplot(111)
plt.scatter(x, y, color='black')
#annotate_points(ax, x, y)

tck,u = interpolate.splprep([x, y], s=0)
unew = np.linspace(0, 1,max(l-2,70),endpoint=True)
out = interpolate.splev(unew, tck)

plt.plot(x,y,'k--',label='Control polygon',marker='o',markerfacecolor='red')
#plt.plot(x,y,'ro',label='Control points only')
plt.plot(out[0],out[1],'b',linewidth=2.0,label='B-spline curve')
plt.legend(loc='best')
plt.scatter(x, y, color='black')
plt.title('SPLEV')
plt.show()
