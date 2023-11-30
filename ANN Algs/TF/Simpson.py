from math import e, sqrt


def funcao(x):
    # Defina a função que você deseja integrar aqui
    return 2 * sqrt(e ** x)


def metodo_simpson(funcao, a, b, n):
    # Parâmetros:
    #   funcao: a função a ser integrada
    #   a, b: os limites inferior e superior de integração
    #   n: o número de subintervalos (deve ser um número par)

    if n % 2 != 0:
        raise ValueError("O número de subintervalos (n) deve ser par para o método de Simpson.")

    h = (b - a) / n  # Tamanho do intervalo
    resultado = funcao(a) + funcao(b)  # Soma das extremidades

    # Adiciona as contribuições dos termos ímpares multiplicados por 4
    for i in range(1, n, 2):
        resultado += 4 * funcao(a + i * h)

    # Adiciona as contribuições dos termos pares multiplicados por 2
    for i in range(2, n - 1, 2):
        resultado += 2 * funcao(a + i * h)

    # Multiplica pela largura do subintervalo dividido por 3
    resultado *= h / 3

    return resultado


# Exemplo de uso:
limite_inferior = -1
limite_superior = 1
numero_subintervalos = 1000

resultado_integral_simpson = metodo_simpson(funcao, limite_inferior, limite_superior, numero_subintervalos)
print(f"Resultado da integral usando o método de Simpson: {resultado_integral_simpson}")
