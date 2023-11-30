import numpy as np

N = 10** 3
interval = [0, 1]

cont = 0

x = np.random.random_sample(size=N)
y = np.random.random_sample(size=N)

area_qua = (interval[1] - interval[0]) ** 2

for i in range(N):
    if (x[i]**2 + y[i]**2) < area_qua:
        cont += 1

area_curva = 4 * cont / N

print(area_curva)
