import numpy.random

def f(u):
    if u >= 0:
        return 1
    else:
        return -1

def findOutput(data, w):
    u = 0.0
    for i in range(0, len(data)):
        u += data[i] * w[i]
    return f(u)

# inputs : O terceiro elemento -1 de cada porta lógica é a entrada dummy
p = [[1, 1, -1], [1, -1, -1], [-1, 1, -1], [-1, -1, -1]]
d = [1, 1, 1, -1]
w = numpy.random.rand(len(p[0]))

# Taxa de aprendizado
c = 0.5
# Taxa de erro desejada
d_error = 0.01
# Contador de interações
inter = 0

while True:
    error = 0
    for i in range(0, len(p)):
        o = findOutput(p[i], w)
        error += ((d[i] - o) ** 2) / 2
        learningSignal = c * (d[i] - o)
        for j in range(0, len(p[i])):
            w[j] += learningSignal * p[i][j]    # Atualização do Peso

    inter += 1
    print(error, " ## ", w)
    if error < d_error:
        print('N. interações ', inter)
        break

print(findOutput([1, 1, -1], w))
print(findOutput([1, 1, -1], w))
print(findOutput([-1, 1, -1], w))
print(findOutput([-1, -1, -1], w))
