from math import e, sqrt


def funcao(x):
    return 2 * sqrt(e ** x)


def metodo_trapezios(funcao, a, b, n):
    # Parâmetros:
    #   funcao: a função a ser integrada
    #   a, b: os limites inferior e superior de integração
    #   n: o número de trapézios a serem utilizados

    h = (b - a) / n  # Tamanho do intervalo
    resultado = 0.5 * (funcao(a) + funcao(b))  # Soma das extremidades

    # Adiciona as contribuições dos trapézios internos
    for i in range(1, n):
        resultado += funcao(a + i * h)

    # Multiplica pela largura do trapézio
    resultado *= h

    return resultado


limite_inferior = -1
limite_superior = 1
numero_trapezios = 1000

resultado_integral = metodo_trapezios(funcao, limite_inferior, limite_superior, numero_trapezios)
print(f"Resultado da integral: {resultado_integral}")
