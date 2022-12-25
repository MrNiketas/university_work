import math
import numpy as np

# генератор случайных процессов
class RandomProcess:
    l1 = 5 ** 9
    l2 = 3 ** 8

    M0: float
    v0: float

    Ns = 10

    def __init__(self, M0, v0, al, N):
        self.M0 = M0
        self.v0 = v0
        self.alpha0 = al
        self.N = N

    def generate(self, N): # метод генерации
        rand_numbers = np.empty(N)
        x_i = 1
        for i in range(N):
            x_i = (self.l1 * x_i) % self.l2
            rand_numbers[i] = x_i

        for i in range(N):
            rand_numbers[i] = (rand_numbers[i] / self.l2) - 0.5

        return rand_numbers

    def M(self, z): # расчёт мат ожидания
        return (1 / len(z)) * np.sum(z)

    def variance(self, z, M): # расчёт дисперсии
        return (1 / len(z)) * np.sum((M - z) ** 2)

    def Z(self, k, Ns, vx, x): # формула случайного процесса
        sum = 0
        for i in range(k, k + Ns):
            factor = math.sqrt(self.v0 / (vx * self.alpha0)) * math.exp(-self.alpha0 * (i - k))
            sum += x[i] * factor + self.M0
        return sum / Ns

    def count(self): # рассчёт случайных значений для входной переменной
        x = self.generate(self.N)
        Mx = self.M(x)
        variance_x = self.variance(x, Mx)

        z = []
        for k in range(1, self.N - self.Ns + 1):
            z.append(self.Z(k, self.Ns, variance_x, x))
        z = np.array(z)
        return z

