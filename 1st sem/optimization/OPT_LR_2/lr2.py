import math as mth
import matplotlib.pyplot as plt
import numpy as np

A = -2
B = 4
C = 2
D = 5
ALPHA = 35
E = 0.01
E2 = 0.001
S = 0.5

alpha = 1
beta = 2
gamma = 0.5
bgt = False


def Function1(x1, x2):
    return ((x1 - A) * mth.cos(ALPHA) + (x2 - B) * mth.sin(ALPHA)) ** 2 / C ** 2 + (
            (x2 - B) * mth.cos(ALPHA) - (x1 - A) * mth.sin(ALPHA)) ** 2 / D ** 2


def Function2(x1, x2):
    return 100 * (x2 - x1 ** 2) ** 2 + (1 - x1) ** 2


def Function(x1, x2):
    return Function2(x1, x2)


def plotCreator(fx, fy):
    x = np.arange(-5, 5, 0.01)
    y = np.arange(-5, 5, 0.01)
    [X, Y] = np.meshgrid(x, y)
    Z = np.arange(-25, 100, 15)
    plt.contour(X, Y, Function(X, Y), Z)
    plt.plot(fx, fy,"o-")
    plt.show()


def main():

    x = -5
    y = 5
    X, Y = MethodSimplex([x, y])
    plotCreator(X, Y)


def getHX(x, y):
    if bgt:
        return 0.08
    r = x
    xCenter = r
    c = S*2
    while True:
        xLeft = xCenter - c
        xRight = xCenter + c
        a = xLeft
        b = xRight
        while True:
            x1 = a + 0.38 * (b - a)
            x2 = b - 0.38 * (b - a)
            if Function(x1, y) > Function(x2, y):
                a = x1
            else:
                b = x2
            if mth.fabs(b - a) < E2:
                xPass = xCenter
                xCenter = (a + b) / 2
                break
        if mth.fabs(xPass - xCenter) < E:
            break
        else:
            c = c * 0.9
    return mth.fabs(xCenter - r)


def getHY(x, y):
    if bgt:
        return 0.08
    r = y
    xCenter = r
    c = S*2
    while True:
        xLeft = xCenter - c
        xRight = xCenter + c
        a = xLeft
        b = xRight
        while True:
            x1 = a + 0.38 * (b - a)
            x2 = b - 0.38 * (b - a)
            if Function(x, x1) > Function(x, x2):
                a = x1
            else:
                b = x2
            if mth.fabs(b - a) < E2:
                xPass = xCenter
                xCenter = (a + b) / 2
                break
        if mth.fabs(xPass - xCenter) < E:
            break
        else:
            c = c*0.9
    return mth.fabs(xCenter - r)


def MethodSimplex(X0):
    X = []
    Y = []

    x0 = X0[0]
    y0 = X0[1]
    X.append(x0)
    Y.append(y0)
    H = getHX(x0, y0)
    x1 = x0 + H
    y1 = y0
    X.append(x1)
    Y.append(y1)

    x2 = x0
    y2 = y0 + H
    X.append(x2)
    Y.append(y2)
    X.append(x0)
    Y.append(y0)

    f0 = Function(x0, y0)
    f1 = Function(x1, y1)
    f2 = Function(x2, y2)
    i = 0
    while True:
        b = beta
        fx = max(f0, f1, f2)
        if fx == f0:
            dx = (x1 + x2) / 2 - x0
            dy = (y1 + y2) / 2 - y0

            while True:
                if Function(x0 + b * dx, y0 + b * dy) < Function(x0, y0):

                    X.append(x0)
                    Y.append(y0)

                    x0 = x0 + b * dx
                    y0 = y0 + b * dy
                    f0 = Function(x0, y0)

                    X.append(x0)
                    Y.append(y0)

                    X.append(x1)
                    Y.append(y1)

                    X.append(x2)
                    Y.append(y2)

                    X.append(x0)
                    Y.append(y0)

                    break
                else:
                    b = b * 0.96
                if b < E:
                    break
        elif fx == f1:
            dx = (x0 + x2) / 2 - x1
            dy = (y0 + y2) / 2 - y1
            while True:
                if Function(x1 + b * dx, y1 + b * dy) < Function(x1, y1):

                    X.append(x1)
                    Y.append(y1)

                    x1 = x1 + b * dx
                    y1 = y1 + b * dy
                    f1 = Function(x1, y1)

                    X.append(x1)
                    Y.append(y1)

                    X.append(x2)
                    Y.append(y2)

                    X.append(x0)
                    Y.append(y0)

                    X.append(x1)
                    Y.append(y1)

                    break
                else:
                    b = b * 0.96
                if b < E:
                    break
        else:
            dx = (x0 + x1) / 2 - x2
            dy = (y0 + y1) / 2 - y2
            while True:
                if Function(x2 + b * dx, y2 + b * dy) < Function(x2, y2):

                    X.append(x2)
                    Y.append(y2)

                    x2 = x2 + b * dx
                    y2 = y2 + b * dy
                    f2 = Function(x2, y2)

                    X.append(x2)
                    Y.append(y2)

                    X.append(x0)
                    Y.append(y0)

                    X.append(x1)
                    Y.append(y1)

                    X.append(x2)
                    Y.append(y2)

                    break
                else:
                    b = b * 0.96
                if b < E:
                    break
        if b < E:
            print(x0, y0)
            print(x1, y1)
            print(x2, y2)
            break
        i = i + 1
    print("Кол-во итераций: ", i)
    return X, Y


def MethodPowell(X0):
    X = []
    Y = []
    x = X0[0]
    y = X0[1]
    X.append(x)
    Y.append(y)
    dX = []
    dY = []
    dX.append(x)
    dY.append(y)
    xCount = 0
    yCount = 0
    s = dX[xCount]
    d = dY[yCount]
    jumpX = True
    jumpY = True
    hX = 0
    hY = 0
    while True:
        if jumpY:
            hX = getHX(x,y)
            while True:
                if Function(x + hX, y) == min(Function(x + hX, y), Function(x - hX, y), Function(x, y)):
                    x = x + hX
                    X.append(x)
                    Y.append(y)
                    dX.append(x)
                    break
                elif Function(x - hX, y) == min(Function(x + hX, y), Function(x - hX, y), Function(x, y)):
                    x = x - hX
                    X.append(x)
                    Y.append(y)
                    dX.append(x)
                    break
                else:
                    hX = hX * 0.96
                if hX < E2:
                    xCount-=1
                    break
        if jumpX:
            hY = getHY(x,y)
            while True:
                if Function(x, y - hY) == min(Function(x, y - hY), Function(x, y + hY), Function(x, y)):
                    y = y - hY
                    X.append(x)
                    Y.append(y)
                    dY.append(y)
                    break
                elif Function(x, y + hY) == min(Function(x, y - hY), Function(x, y + hY), Function(x, y)):
                    y = y + hY
                    X.append(x)
                    Y.append(y)
                    dY.append(y)
                    break
                else:
                    hY = hY * 0.96
                if hY < E2:
                    yCount-=1
                    break

        if (not jumpX) & jumpY:
            xCount = xCount + 1
            s = dX[xCount]
        if (not jumpY) & jumpX:
            yCount = yCount + 1
            d = dY[yCount]

        dx = x - s
        dy = y - d

        if jumpY & jumpX:
            jumpX = False
        elif (not jumpX) & jumpY:
            jumpX = True
            jumpY = False
        elif (not jumpY) & jumpX:
            jumpY = True
            jumpX = False

        while True:
            x1 = x + dx
            y1 = y + dy
            if Function(x, y) > Function(x1, y1):
                x = x1
                y = y1
                jumpX = True
                jumpY = True
                s = x
                d = y
                X.append(x)
                Y.append(y)
            else:
                break
        if (hX < E2) & (hY < E2):
            break

    print(x, y)
    print("Кол-во итераций: ", len(X))
    return X, Y


if __name__ == "__main__":
    main()
