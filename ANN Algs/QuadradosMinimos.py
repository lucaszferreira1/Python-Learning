import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt

# Dados fornecidos
X = np.array([-9, -6, -4, -2, 0, 2, 4])
Y = np.array([30, 10, 9, 6, 5, 4, 4])

# Definindo as funções a serem ajustadas
def func1(x, a, b):
    return x / (a * x + b)

def func2(x, a, b):
    return a * np.power(b, x)

# Ajustando a primeira função
params1, covariance1 = curve_fit(func1, X, Y)
a1, b1 = params1

# Ajustando a segunda função
params2, covariance2 = curve_fit(func2, X, Y)
a2, b2 = params2

# Gerando pontos para as curvas ajustadas
x_fit = np.linspace(min(X), max(X), 100)
y_fit1 = func1(x_fit, a1, b1)
y_fit2 = func2(x_fit, a2, b2)

# Plotando os resultados
plt.scatter(X, Y, label='Dados Originais')
plt.plot(x_fit, y_fit1, label=f'Função 1: $\\frac{{x}}{{{a1:.2f}x + {b1:.2f}}}$', linestyle='--')
plt.plot(x_fit, y_fit2, label=f'Função 2: ${a2:.2f} * {b2:.2f}^x$', linestyle='--')
plt.axis('equal')
plt.legend()
plt.xlabel('X')
plt.ylabel('Y')
plt.title('Ajuste de Curva usando Mínimos Quadrados')
plt.show()
