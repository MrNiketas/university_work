import numpy as np


A1, A2, A3, A4 = 2820, 137, 880, 600
E1, E2, E3, E4 = 75000, 45000, 66500, 59000
R = 8.31
u = 180
ro = 1.6

dl = 0.5
dtao = 1


def k(A, E, T):
    return A * np.exp(-E / (R * T))


def c1(c1in, k1, k2, k3, k4, c1, c2, c3, c5):
    dc1 = (k1 * c2 - k2 * c1 + 2 * k3 * c3 + k4 * 2 * c5) / u
    dt1 = (k1 * c2 - k2 * c1 + 2 * k3 * c3 + k4 * 2 * c5) - dc1 * u
    return c1in + dc1 * dl + dt1 * dt1 * dtao


def c2(c2in, k1, k3, c2, c3):
    dc2 = (-k1 * c2 + 2 * k3 * c3) / u
    dt2 = (-k1 * c2 + 2 * k3 * c3) - dc2 * u
    return c2in + dc2 * dl + dt2 * dtao


def c3(c3in, k3, c3):
    dc3 = (-k3 * 5 * c3) / u
    dt3 = (-k3 * 5 * c3) - dc3 * u
    return c3in + dc3 * dl + dt3 * dtao


def c4(c4in, k3, k4, c3, c5):
    dc4 = (k3 * 3 * c3 + k4 * 3 * c5) / u
    dt4 = (k3 * 3 * c3 + k4 * 3 * c5) - dc4 * u
    return c4in + dc4 * dl + dt4 * dtao


def c5(c5in, k4, c5):
    dc5 = (-k4 * 5 * c5) / u
    dt5 = (-k4 * 5 * c5) - dc5 * u
    return c5in + dc5 * dl + dt5 * dtao

# расчёт для случайных процессов
def generate_process(L, T, C3):
    k1 = k(A1, E1, T)
    k2 = k(A2, E2, T)
    k3 = k(A3, E3, T)
    k4 = k(A4, E4, T)

    c10 = 0
    c20 = 20
    c30 = C3[0]
    c40 = 0
    c50 = 40

    c20 = (c20 * ro) / (100 * 0.03)
    c50 = (c50 * ro) / (100 * 0.044)

    c1_curr, c2_curr, c3_curr, c4_curr, c5_curr = c10, c20, c30, c40, c50

    SUM = []
    for time_i, c3i in enumerate(C3):
        c30 = c3i

        SUM.append(c1_curr + c4_curr)

        c10 = c1_curr
        c20 = c2_curr
        c50 = c5_curr

        c1_curr = c1(c10, k1, k2, k3, k4, c1_curr, c2_curr, c3_curr, c5_curr)
        c2_curr = c2(c20, k1, k3, c2_curr, c3_curr)
        c4_curr = c4(c40, k3, k4, c3_curr, c5_curr)
        c5_curr = c5(c50, k4, c5_curr)
        c3_curr = c3(c30, k3, c3_curr)

    return SUM








