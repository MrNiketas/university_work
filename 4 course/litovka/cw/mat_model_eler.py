import numpy as np
from matplotlib import pyplot as plt

# исходные данные из варианта
A1, A2, A3, A4 = 2820, 137, 880, 600
E1, E2, E3, E4 = 75000, 45000, 66500, 59000
R = 8.31
u = 180
ro = 1.6

dl = 0.5

# функция для расчёта коэффециентов k1, k2, k3, k4 (скорость каждой из представленных реакций)
def k(A, E, T):
    return A * np.exp(-E / (R * T))

# расчёт значения концентрации для каждого из веществ (C1, C2, C3, C4, C5)
def c1(c1in, k1, k2, k3, k4, c1, c2, c3, c5):
    dc1 = (k1 * c2 - k2 * c1 + 2 * k3 * c3 + k4 * 2 * c5) / u
    return c1in + dc1 * dl


def c2(c2in, k1, k3, c2, c3):
    dc2 = (-k1 * c2 + 2 * k3 * c3) / u
    return c2in + dc2 * dl


def c3(c3in, k3, c3):
    dc3 = (-k3 * 5 * c3) / u
    return c3in + dc3 * dl


def c4(c4in, k3, k4, c3, c5):
    dc4 = (k3 * 3 * c3 + k4 * 3 * c5) / u
    return c4in + dc4 * dl


def c5(c5in, k4, c5):
    dc5 = (-k4 * 5 * c5) / u
    return c5in + dc5 * dl


def get_test_model(L, T):
    # расчёт всех коэфициентов k (k1, k2, k3, k4)
    k1 = k(A1, E1, T)
    k2 = k(A2, E2, T)
    k3 = k(A3, E3, T)
    k4 = k(A4, E4, T)


    c20 = 20
    c30 = 40
    c50 = 40
    c10 = 0
    c40 = 0

    c20 = (c20 * ro) / (100 * 0.03)
    c30 = (c30 * ro) / (100 * 0.058)
    c50 = (c50 * ro) / (100 * 0.044)

    C1 = []
    C2 = []
    C3 = []
    C4 = []
    C5 = []
    SUM = []

    current_L = 0
    sum_max=0
    # в цикле методом Эйлера вычисляем значение концентрации для каждого из веществ
    while current_L < L:
        c1_curr = c1(c10, k1, k2, k3, k4, c10, c20, c30, c50)
        c2_curr = c2(c20, k1, k3, c20, c30)
        c3_curr = c3(c30, k3, c30)
        c4_curr = c4(c40, k3, k4, c3_curr, c50)
        c5_curr = c5(c50, k4, c50)

        C1.append(c1_curr)
        C2.append(c2_curr)
        C3.append(c3_curr)
        C4.append(c4_curr)
        C5.append(c5_curr)
        SUM.append(c1_curr + c4_curr)

        c10, c20, c30, c40, c50 = c1_curr, c2_curr, c3_curr, c4_curr, c5_curr
        current_L += dl
        if(sum_max<(c1_curr + c4_curr)):
            sum_max=c1_curr + c4_curr
        if(sum_max>(c1_curr + c4_curr)):
            print(current_L)
    # построение графика
    plt.plot(np.arange(0, L, step=dl), C1, label="C1 (C2H4)")
    plt.plot(np.arange(0, L, step=dl), C2, linestyle="--", label="C2 (C2H6)")
    plt.plot(np.arange(0, L, step=dl), C3, linestyle="--", label="C3 (C4H10)")
    plt.plot(np.arange(0, L, step=dl), C4, label="C4 (C3H6)")
    plt.plot(np.arange(0, L, step=dl), C5, linestyle="--", label="C5 (C3H8)")
    plt.plot(np.arange(0, L, step=dl), SUM, label="C1 + C4")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    L = 250
    T = 1100
    get_test_model(L, T)

