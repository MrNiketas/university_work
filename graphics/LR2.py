import math

import matplotlib.pyplot as plot
import numpy as np

ArrayPoints = np.array([
    (1.2, 0.8),
    (0.75, -1),
    (0, 0.5),
    (2, 1.5),
    (1, 3),
    (0, 1.5),
    (1.2, 0.5)

], dtype=float)

h = 0.001


class Bezier():
    def TwoPoints(t, P1, P2):
        Q1 = (1 - t) * P1 + t * P2
        return Q1

    def ThreePoints(t, P1, P2, P3):
        Q1 = ((1 - t)**2) * P1 + 2 * (1 - t) * t * P2 + (t**2) * P3
        return Q1

    def QuadPoints(t, P1, P2, P3, P4):
        Q1 = ((1 - t)**3) * P1 + 3 * ((1 - t)**2) * t * P2 + (t**2) * P3 * 3 * (1 - t) + (t**3) * P4
        return Q1

    def Points(t, points):
        newpoints = []
        for i1 in range(0, len(points) - 1):
            newpoints += [Bezier.TwoPoints(t, points[i1], points[i1 + 1])]
        return newpoints

    def Point(t, points):
        newpoints = points
        while len(newpoints) > 1:
            newpoints = Bezier.Points(t, newpoints)
        return newpoints[0]

    def Curve(t_values, points):
        curve = np.array([[0.0] * len(points[0])])
        for t in t_values:
            curve = np.append(curve, [Bezier.Point(t, points)], axis=0)
        curve = np.delete(curve, 0, 0)
        return curve


def plotCreator():
    t_points = np.arange(0, 1, h)
    points = Bezier.Curve(t_points, ArrayPoints)
    plot.plot(points[:, 0], points[:, 1])
    plot.plot(ArrayPoints[:, 0], ArrayPoints[:, 1], "ro")
    plot.grid()
    plot.show()


if __name__ == '__main__':
    plotCreator()
