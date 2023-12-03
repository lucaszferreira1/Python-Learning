def funcao(x, y):
    return x ** 2 + y ** 2


def metodo_trapezios_duplo(funcao, a_x, b_x, a_y, b_y, n_x, n_y):
    # Parâmetros:
    #   funcao: a função bidimensional a ser integrada
    #   a_x, b_x, a_y, b_y: os limites inferior e superior de integração em ambas as dimensões
    #   n_x, n_y: o número de trapézios em ambas as dimensões

    h_x = (b_x - a_x) / n_x  # Tamanho do intervalo em x
    h_y = (b_y - a_y) / n_y  # Tamanho do intervalo em y

    resultado = 0.0

    # Loop sobre os trapézios em ambas as dimensões
    for i in range(n_x):
        for j in range(n_y):
            # Coordenadas dos vértices do trapézio
            x0, x1 = a_x + i * h_x, a_x + (i + 1) * h_x
            y0, y1 = a_y + j * h_y, a_y + (j + 1) * h_y

            # Área do trapézio multiplicada pelo valor da função no ponto médio
            resultado += 0.25 * h_x * h_y * (funcao(x0, y0) + funcao(x1, y0) + funcao(x0, y1) + funcao(x1, y1))

    return resultado


limite_inferior_x = 0
limite_superior_x = 3
limite_inferior_y = 0
limite_superior_y = 3
numero_trapezios_x = 100
numero_trapezios_y = 100

resultado_integral_dupla_trapezios = metodo_trapezios_duplo(funcao, limite_inferior_x, limite_superior_x, limite_inferior_y, limite_superior_y, numero_trapezios_x, numero_trapezios_y)
print(f"Resultado da integral dupla usando o método dos trapézios: {resultado_integral_dupla_trapezios}")
