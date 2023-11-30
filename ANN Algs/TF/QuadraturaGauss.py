import numpy as np
from math import e, sqrt


def funcao(x):
    # Defina a função que você deseja integrar aqui
    return 2 * sqrt(e ** x)


def quadratura_gauss(funcao, a, b, grau):
    # Parâmetros:
    #   funcao: a função a ser integrada
    #   a, b: os limites inferior e superior de integração
    #   grau: o grau do polinômio de Legendre (e o número de pontos de quadratura)

    # Calcula os pontos e pesos de quadratura usando a biblioteca NumPy
    pontos, pesos = np.polynomial.legendre.leggauss(grau)

    # Mapeia os pontos de [-1, 1] para [a, limite_superior]
    pontos_mapeados = 0.5 * (b - a) * pontos + 0.5 * (b + a)

    # Calcula a soma ponderada dos valores da função nos pontos de quadratura
    resultado_integral = sum(w * funcao(x) for w, x in zip(pesos, pontos_mapeados))

    # Ajusta pela escala da transformação
    resultado_integral *= 0.5 * (b - a)

    return resultado_integral


# Exemplo de uso:
limite_inferior = -1
limite_superior = 1
grau_quadratura = 4  # O grau é geralmente escolhido de acordo com a precisão desejada

resultado_integral_quadratura_gauss = quadratura_gauss(funcao, limite_inferior, limite_superior, grau_quadratura)
print(f"Resultado da integral usando o método da quadratura de Gauss: {resultado_integral_quadratura_gauss}")
