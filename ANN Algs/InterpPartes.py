import numpy as np
import matplotlib.pyplot as plt


def interpolacao_por_partes(x, y):
    """
    Função para interpolação por partes para encontrar a função polinomial quadrática.

    Parâmetros:
    - x: Lista com as coordenadas x dos pontos.
    - y: Lista com as coordenadas y dos pontos.

    Retorna:
    - Coeficientes a, b, c da função quadrática ax^2 + bx + c.
    """
    n = len(x)

    if n < 3:
        raise ValueError("É necessário pelo menos 3 pontos para interpolação por partes.")

    # Calcula as diferenças divididas finitas
    diffs = np.zeros((n, n))
    diffs[:, 0] = y

    for j in range(1, n):
        for i in range(n - j):
            diffs[i][j] = (diffs[i + 1][j - 1] - diffs[i][j - 1]) / (x[i + j] - x[i])

    # Coeficientes da função quadrática
    a = diffs[0][2]
    b = diffs[0][1] - a * (x[0] + x[1])
    c = diffs[0][0] - a * x[0] ** 2 - b * x[0]

    return a, b, c


def plotar_grafico(x, y, a, b, c):
    """
    Função para plotar o gráfico da função polinomial quadrática resultante.
    """
    x_vals = np.linspace(min(x), max(x), 100)
    y_vals = a * x_vals ** 2 + b * x_vals + c

    plt.scatter(x, y, color='red', label='Pontos dados')
    plt.plot(x_vals, y_vals, label=f'Função Quadrática: {a:.2f}x^2 + {b:.2f}x + {c:.2f}')

    plt.title('Interpolação por Partes - Função Quadrática')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()


# Pontos de exemplo
x_pontos = [0, 1/6, 1/3, 1/2, 2/3, 5/6, 1]
y_pontos = [1, 3, 2, 1, 0, 2, 1]

# Encontrar coeficientes da função quadrática
a, b, c = interpolacao_por_partes(x_pontos, y_pontos)

# Plotar o gráfico
plotar_grafico(x_pontos, y_pontos, a, b, c)
