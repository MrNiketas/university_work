import math
import matplotlib.pyplot as plt

kt = 5000
t = 5000
ct = 4187
Tr = 90
r = 2.26 * 10 ** 6
F = 10

sigma = 0.12
S = 0.75
P_null = 7900
P_first = 7600

delta_C_vh = 3
delta_m_vh = 2.8
delta_T_vh = -5

C0, C1 = 7, 12
m0, m1 = 3.9, 5.4
T0, T1 = 125, 145

t = 0
t_max = 500
delta_t = 0.1

C_vhod = 10
m_vhod = 4
T_vhod = 138

C_vihod = []
m_vihod = []
T_vihod = []

C, m, T, vr = [], [], [], []
c = lambda m_vh, C_vh, C_vihod, T0, m_vt: (m_vh * C_vh - C_vihod * sigma * math.sqrt(P_null + M(m_vh, m_vt) / S - P_first) - C_vihod * dM(m_vh, m_vt, T0)) / M(m_vh, m_vt)  # из файла

f = lambda C_vh, m_vh, T_vh: (m_vh * C_vh * (ct * Tr - r)) / (kt * F * (T_vh - Tr) + m_vh * (ct * Tr - r))

M = lambda m_vh, m_vt: S * ((((m_vh - m_vt) / sigma) ** 2) + P_first - P_null)

dM = lambda m_vh, m_vt, T0: ((r * m_vh - r * sigma * math.sqrt(P_null + M(m_vh, m_vt) / S - P_first) - kt * F * (T0 - Tr) - ((m_vh - sigma * math.sqrt(P_null + M(m_vh, m_vt) / S - P_first)) * ct * Tr)) / (r - ct * Tr))  # из файла

cc = f(C0, m_vhod, T_vhod)

C0 += delta_C_vh
m_vt = m_vhod - ((m_vhod * C0) / cc)

while t < t_max:
    t = t + delta_t
    vr.append(t)

t = 0
while t < t_max:
    t = t + delta_t
    cc = cc + (c(m_vhod, C0, cc, T_vhod, m_vt) * delta_t)
    C.append(cc)

t = 0
cc = f(C_vhod, m0, T_vhod)
m0 += delta_m_vh
m_vt = m0 - ((m0 * C_vhod) / cc)
while t < t_max:
    t = t + delta_t
    cc = cc + c(m0, C_vhod, cc, T_vhod, m_vt) * delta_t
    m.append(cc)

t = 0
cc = f(C_vhod, m_vhod, T0)
T0 += delta_T_vh
m_vt = m_vhod - ((m_vhod * C_vhod) / cc)
while t < t_max:
    t = t + delta_t
    cc = cc + c(m_vhod, C_vhod, cc, T0, m_vt) * delta_t
    T.append(cc)

fig, axes = plt.subplots(nrows=1, ncols=3, figsize=(12, 5))

axes[0].set(title='С.вых (C.вх)')
axes[1].set(title='С.вых (m.вх)')
axes[2].set(title='С.вых (T.вх)')
axes[0].grid(True)
axes[1].grid(True)
axes[2].grid(True)
axes[0].plot(vr, C, color='blue')
axes[1].plot(vr, m, color='blue')
axes[2].plot(vr, T, color='blue')

plt.subplots_adjust(wspace=0.5, hspace=0)
plt.show()