import numpy as np
import matplotlib.pyplot as plt


def inverse_lagrange_interpolation(x_values, y_values, y):
    """
    Tenta inverter a interpolação de Lagrange para encontrar uma aproximação de x dado f(x) = y.

    :param x_values: Lista dos valores de x conhecidos.
    :param y_values: Lista dos valores correspondentes de f(x).
    :param y: Valor de f(x) para o qual a aproximação de x é desejada.
    :return: Uma aproximação de x para o dado f(x).
    """
    n = len(x_values)
    result = 0.0

    for i in range(n):
        term = y / y_values[i]
        for j in range(n):
            if j != i:
                term = term * (y_values[j] - y) / (y_values[j] - y_values[i])
        result += term * x_values[i]

    return result


def lagrange_interpolation(x_values, y_values, x):
    n = len(x_values)
    result = 0.0

    for i in range(n):
        term = y_values[i]
        for j in range(n):
            if j != i:
                term = term * (x - x_values[j]) / (x_values[i] - x_values[j])
        result += term

    return result


# Exemplo de uso:
x_values = [0.5, 0.75, 1, 1.5, 2, 2.5, 3]
y_values = [-2.8, -0.6, 1, 3.2, 4.8, 6, 7]

# Valor de f(x) para o qual queremos a aproximação de x
y_to_approximate = 0.23

# Tenta inverter a interpolação de Lagrange
approximated_x = inverse_lagrange_interpolation(x_values, y_values, y_to_approximate)

print(f"A aproximação de x para f(x)={y_to_approximate} é: {approximated_x}")

# Gera a função aproximada para o gráfico
y_approximated = [lagrange_interpolation(x_values, y_values, x) for x in x_values]


# Gera o gráfico
plt.figure(figsize=(8, 6))
plt.scatter(x_values, y_values, label='Pontos Conhecidos', color='red')
plt.plot(x_values, y_approximated, label='f(x) Aproximada', linestyle='dashed', color='green')
plt.title('Interpolação de Lagrange')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.legend()
plt.grid(True)
plt.show()