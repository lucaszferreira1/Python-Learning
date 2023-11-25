import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# Definindo a função que representa o polinômio ajustado
def polynomial_function(x, coefficients):
    return np.polyval(coefficients, x) - 0.23

def polynomial_regression(x_values, y_values, degree):
    """
    Realiza a regressão polinomial para um conjunto de dados.

    Parâmetros:
    - x_values: Lista dos valores x conhecidos.
    - y_values: Lista dos valores correspondentes de f(x).
    - degree: Grau do polinômio desejado.

    Retorna:
    - Os coeficientes do polinômio ajustado.
    """
    coefficients = np.polyfit(x_values, y_values, degree)
    return coefficients

def evaluate_polynomial(coefficients, x):
    """
    Avalia um polinômio dados seus coeficientes e um valor de x.

    Parâmetros:
    - coefficients: Coeficientes do polinômio.
    - x: Valor de x para avaliação.

    Retorna:
    - O valor do polinômio para o dado x.
    """
    return np.polyval(coefficients, x)

# Exemplo de uso:
# Dados de exemplo
x_values = np.array([0.5, 0.75, 1, 1.5, 2, 2.5, 3])
y_values = np.array([-2.8, -0.6, 1, 3.2, 4.8, 6, 7])

# Grau do polinômio desejado
degree = 2

# Realiza a regressão polinomial
coefficients = polynomial_regression(x_values, y_values, degree)

# Valores preditos usando o polinômio ajustado
x_pred = np.linspace(min(x_values), max(x_values), 100)
y_pred = evaluate_polynomial(coefficients, x_pred)

# Encontrar a raiz da equação polinomial - ou seja, onde f(x) é aproximadamente igual a 0.23
x_guess = 0.32
x_solution = fsolve(polynomial_function, x_guess, args=(coefficients,))
print(f"{coefficients[0]}x^2 + {coefficients[1]}x + {coefficients[2]}")
print(f'O valor de x para o qual f(x) é aproximadamente 0.23 é {x_solution[0]:.2f}')

# Plota os dados originais e o polinômio ajustado
plt.scatter(x_values, y_values, label='Dados Originais')
plt.plot(x_pred, y_pred, color='red', label=f'Regressão Polinomial (Grau {degree})')
plt.legend()
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Regressão Polinomial')
plt.show()


