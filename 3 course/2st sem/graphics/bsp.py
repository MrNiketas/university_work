import numpy as np
import matplotlib.pyplot as plt

def Spline2(p):
    array = []
    i = 2
    while i <= len(p) - 1:
        for t in np.arange(0, 1.01, 0.01):
            array.append(0.5 * t ** 2 * p[i] + (3/4 - (t - 0.5) ** 2) * p[i - 1] + 0.5 * (1 - t) ** 2 * p[i - 2])
        i += 1
    return array

def Spline3(p):
    array = []
    i = 3
    while i <= len(p) - 1:
        for t in np.arange(0, 1.01, 0.01):
            array.append(1 / 6 * t ** 3 * p[i] + (2 / 3 - 1 / 2 * (t - 1) ** 3 - (t - 1) ** 2) * p[i - 1]
                         + (2 / 3 + 1 / 2 * t ** 3 - t ** 2) * p[i - 2] + 1 / 6 * (1 - t) ** 3 * p[i - 3])
        i += 1
    return array


x2 = [3, 3, 3, 5, 8, 15, 15, 15]
y2 = [5, 5, 5, 3, 1, 2, 2, 2]

x2_1 = [5, 1, 3, 5, 1]
y2_1 = [3, 2, 1, 3, 2]

x2_2 = [1, 1, 1, 2, 3, 2.5, 4, 5.5, 6.5, 6, 7, 7, 7]
y2_2 = [1, 1, 1, 0.5, 2, 3, 4, 3, 2, 0.5, 1, 1, 1]

x_new2 = Spline2(x2)
y_new2 = Spline2(y2)

fig, ax = plt.subplots()
plt.plot(x2,y2,'o',x_new2, y_new2, color="blue")
plt.grid()
plt.show()
"""
plt.plot(x2_1,y2_1,'o',Spline2(x2_1),Spline2(y2_1), color="blue")
plt.grid()
plt.show()
"""
plt.plot(x2_2,y2_2,'o',Spline2(x2_2),Spline2(y2_2), color="blue")
plt.grid()
plt.show()


x3 = [1, 1, 1, 3, 8, 12, 12, 12]
y3 = [1, 1, 1, 2, 3, 4, 4, 4]

x_new3 = Spline3(x3)
y_new3 = Spline3(y3)

plt.plot(x3,y3,'o',x_new3, y_new3, color="red")
plt.grid()
plt.show()