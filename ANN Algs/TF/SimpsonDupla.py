def funcao(x, y):
    return x ** 2 + y ** 2


def metodo_simpson_duplo(funcao, a_x, b_x, a_y, b_y, n_x, n_y):
    # Parâmetros:
    #   funcao: a função bidimensional a ser integrada
    #   a_x, b_x, a_y, b_y: os limites inferior e superior de integração em ambas as dimensões
    #   n_x, n_y: o número de subintervalos em ambas as dimensões (deve ser um número par)

    if n_x % 2 != 0 or n_y % 2 != 0:
        raise ValueError(
            "O número de subintervalos em ambas as dimensões (n_x e n_y) deve ser par para o método de Simpson.")

    h_x = (b_x - a_x) / n_x  # Tamanho do intervalo em x
    h_y = (b_y - a_y) / n_y  # Tamanho do intervalo em y

    resultado = 0.0

    # Loop sobre os subintervalos em ambas as dimensões
    for i in range(0, n_x, 2):
        for j in range(0, n_y, 2):
            # Coordenadas dos vértices do subintervalo
            x0, x1 = a_x + i * h_x, a_x + (i + 2) * h_x
            y0, y1 = a_y + j * h_y, a_y + (j + 2) * h_y

            # Área do subintervalo multiplicada pelo valor da função no ponto médio
            resultado += (h_x / 3) * (h_y / 3) * (
                    funcao(x0, y0) + 4 * funcao(x0 + h_x, y0) + funcao(x0 + 2 * h_x, y0) +
                    4 * funcao(x0, y0 + h_y) + 16 * funcao(x0 + h_x, y0 + h_y) + 4 * funcao(x0 + 2 * h_x, y0 + h_y) +
                    funcao(x0, y0 + 2 * h_y) + 4 * funcao(x0 + h_x, y0 + 2 * h_y) + funcao(x0 + 2 * h_x, y0 + 2 * h_y)
            )

    return resultado


limite_inferior_x = 0
limite_superior_x = 3
limite_inferior_y = 0
limite_superior_y = 3
numero_subintervalos_x = 100
numero_subintervalos_y = 100

resultado_integral_dupla_simpson = metodo_simpson_duplo(funcao, limite_inferior_x, limite_superior_x, limite_inferior_y, limite_superior_y, numero_subintervalos_x, numero_subintervalos_y)
print(f"Resultado da integral dupla usando o método de Simpson: {resultado_integral_dupla_simpson}")
