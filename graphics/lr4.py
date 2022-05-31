import numpy as np
from scipy import interpolate

import matplotlib.pyplot as plt


ctr = np.array([(3.28,0.00),(4.00,0.50),(4.40,1.0),(4.60,1.52),(5.00,2.5),(5.00,3.34),(4.70,3.8),(4.50,3.96),(4.20,4.0),(3.70,3.90),(3.00,3.5),(2.00,2.9)])
x=ctr[:,0]
y=ctr[:,1]

# uncomment both lines for a closed curve
#x=np.append(x,[x[0]])  
#y=np.append(y,[y[0]])

l=len(x)  

t=np.linspace(0,1,l-2,endpoint=True)
t=np.append([0,0,0],t)
t=np.append(t,[1,1,1])

tck=[t,[x,y],3]
u3=np.linspace(0,1,(max(l*2,70)),endpoint=True)
out = interpolate.splev(u3,tck)

plt.plot(x,y,'k--',label='Control polygon',marker='o',markerfacecolor='red')
#plt.plot(x,y,'ro',label='Control points only')
plt.plot(out[0],out[1],'b',linewidth=2.0,label='B-spline curve')
plt.legend(loc='best')
plt.scatter(x, y, color='black')
plt.title('Cubic B-spline curve evaluation')
plt.show()