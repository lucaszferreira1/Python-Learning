import numpy as np

def lagrange_interpolation(x, y, x_interp):
    """
    Realiza a interpolação polinomial de Lagrange.

    Parâmetros:
    - x: Lista dos valores x conhecidos.
    - y: Lista dos valores correspondentes de f(x).
    - x_interp: O valor de x para o qual queremos encontrar a aproximação de f(x).

    Retorna:
    - A aproximação de f(x) para o valor x_interp.
    """
    result = 0.0
    n = len(x)

    for i in range(n):
        term = y[i]
        for j in range(n):
            if j != i:
                term = term * (x_interp - x[j]) / (x[i] - x[j])
        result += term

    return result

# Exemplo de uso:
# Dados de exemplo
x_dados = [0.15, 0.2, 0.25, 0.3, 0.35, 0.4]
y_dados = [0.12, 0.16, 0.19, 0.22, 0.25, 0.27]

# Valor de x para o qual queremos aproximar f(x)
x_interp = 0.23

# Realiza a interpolação
resultado_interp = lagrange_interpolation(x_dados, y_dados, x_interp)

# Exibe o resultado
print(f"Aproximação de f({x_interp}) é {resultado_interp}")
