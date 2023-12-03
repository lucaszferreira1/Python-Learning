import random
from math import e, sqrt


def funcao(x):
    return 2 * sqrt(e ** x)


def metodo_monte_carlo(funcao, a, b, n):
    # Parâmetros:
    #   funcao: a função a ser integrada
    #   a, b: os limites inferior e superior de integração
    #   n: o número de pontos aleatórios a serem gerados

    total_pontos = 0
    pontos_dentro = 0

    for _ in range(n):
        x = random.uniform(a, b)
        y = random.uniform(0, funcao(b))  # Garante que os pontos y estejam abaixo da curva da função

        total_pontos += 1
        if y <= funcao(x):
            pontos_dentro += 1

    # Área da região de integração multiplicada pela média dos valores da função nos pontos gerados
    area_regiao = (b - a) * funcao(b)
    resultado_integral = area_regiao * (pontos_dentro / total_pontos)

    return resultado_integral


limite_inferior = -1
limite_superior = 1
numero_pontos = 1000

resultado_integral_monte_carlo = metodo_monte_carlo(funcao, limite_inferior, limite_superior, numero_pontos)
print(f"Resultado da integral usando o método de Monte Carlo: {resultado_integral_monte_carlo}")
