import math

def find_min_points_for_error(target_error, a, b):
    max_second_derivative = max(abs(-math.cos(x)) for x in [a, b])
    min_points = math.ceil(math.sqrt((8 * target_error) / ((b - a)**2 * max_second_derivative)))
    return min_points

# Exemplo de uso para f(x) = cos(x) no intervalo [1, 2] com erro alvo de 1e-6
a = 1
b = 2
target_error = 1e-6

min_points = find_min_points_for_error(target_error, a, b)

print(f'O mínimo número de pontos para um erro <= {target_error} é: {min_points}')
