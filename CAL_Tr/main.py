import heapq
import networkx as nx
import matplotlib.pyplot as plt
from random import choices, choice
from math import radians, sin, cos, sqrt, atan2

city_positions = {
        'Boa Vista': (-60.6735, 2.8178),
        'Manaus': (-60.0252, -3.1019),
        'Macapá': (-51.1811, 0.0464),
        'Belém': (-48.4782, -1.4557),
        'Porto Velho': (-63.9039, -8.7619),
        'Cuiabá': (-56.0967, -15.5994),
        'Brasília': (-47.9297, -15.7801),
        'Goiânia': (-49.2718, -16.686),
        'Campo Grande': (-54.6146, -20.4683),
        'Belo Horizonte': (-43.9385, -19.9176),
        'São Paulo': (-46.6334, -23.5505),
        'São Luís': (-44.3032, -2.5290),
        'Teresina': (-42.8019, -5.0919),
        'Fortaleza': (-38.5023, -3.7172),
        'Natal': (-35.2094, -5.7945),
        'João Pessoa': (-34.8631, -7.115),
        'Recife': (-34.8771, -8.0476),
        'Maceió': (-35.7419, -9.665),
        'Aracaju': (-37.0714, -10.9472),
        'Salvador': (-38.5023, -12.9716),
        'Feira de Santana': (-39.2803, -12.2575),
        'Rio de Janeiro': (-43.1729, -22.9083),
        'Vitória': (-40.3155, -20.3155),
        'Curitiba': (-49.2583, -25.4209),
        'Florianópolis': (-48.5471, -27.5954),
        'Porto Alegre': (-51.2177, -30.0346),
        'Palmas': (-48.3378, -10.1844)
    }

distances_cities = {
    'Aracaju': {
        'Maceió': 271,
        'Salvador': 325,
    },
    'Belém': {
        'Macapá': 539,
        'Manaus': 1636,
        'Porto Velho': 2569,
        'São Luís': 576,
        'Palmas': 1207,
    },
    'Belo Horizonte': {
        'Brasília': 740,
        'Campo Grande': 1262,
        'Rio de Janeiro': 442,
        'São Paulo': 583,
        'Salvador': 1284,
        'Vitória': 515,
    },
    'Boa Vista': {
        'Manaus': 782,
    },
    'Brasília': {
        'Belo Horizonte': 740,
        'Goiânia': 211,
        'Palmas': 843,
        'Salvador': 1444,
    },
    'Campo Grande': {
        'Belo Horizonte': 1262,
        'Cuiabá': 704,
        'Curitiba': 977,
        'Goiânia': 839,
        'São Paulo': 984,
    },
    'Cuiabá': {
        'Campo Grande': 704,
        'Goiânia': 898,
        'Palmas': 1500,
        'Porto Velho': 1460,
    },
    'Curitiba': {
        'Campo Grande': 977,
        'Florianópolis': 317,
        'São Paulo': 416,
    },
    'Florianópolis': {
        'Curitiba': 317,
        'Porto Alegre': 463,
    },
    'Fortaleza': {
        'Natal': 523,
        'São Luís': 897,
        'Teresina': 599,
    },
    'Goiânia': {
        'Brasília': 211,
        'Campo Grande': 839,
        'Cuiabá': 898,
    },
    'João Pessoa': {
        'Natal': 179,
        'Recife': 115,
    },
    'Macapá': {
        'Belém': 539,
    },
    'Maceió': {
        'Aracaju': 201,
        'Recife': 258,
    },
    'Manaus': {
        'Belém': 1636,
        'Boa Vista': 782,
        'Porto Velho': 889,
    },
    'Natal': {
        'Fortaleza': 523,
        'João Pessoa': 179,
    },
    'Palmas': {
        'Belém': 1207,
        'Brasília': 843,
        'Cuiabá': 1500,
        'Salvador': 1439,
        'Teresina': 1113,
    },
    'Porto Alegre': {
        'Florianópolis': 463,
    },
    'Porto Velho': {
        'Belém': 2569,
        'Cuiabá': 1460,
        'Manaus': 889,
    },
    'Recife': {
        'João Pessoa': 115,
        'Maceió': 258,
    },
    'Rio de Janeiro': {
        'Belo Horizonte': 442,
        'São Paulo': 429,
        'Vitória': 1172,
    },
    'Salvador': {
        'Aracaju': 256,
        'Belo Horizonte': 1284,
        'Brasília': 1444,
        'Palmas': 1439,
        'Teresina': 1157,
        'Vitória': 1168,
    },
    'São Luís': {
        'Belém': 576,
        'Fortaleza': 897,
        'Teresina': 441,
    },
    'São Paulo': {
        'Belo Horizonte': 583,
        'Campo Grande': 984,
        'Curitiba': 416,
        'Rio de Janeiro': 429,
    },
    'Teresina': {
        'Fortaleza': 599,
        'Palmas': 1113,
        'Salvador': 1157,
        'São Luís': 441,
    },
    'Vitória': {
        'Belo Horizonte': 515,
        'Rio de Janeiro': 1172,
        'Salvador': 1168,
    },
}


def a_star(graph, start, goal):
    open_set = []
    heapq.heappush(open_set, (0, start))

    came_from = {}
    g_score = {city: float('inf') for city in graph}
    g_score[start] = 0

    while open_set:
        current_cost, current_city = heapq.heappop(open_set)

        if current_city == goal:
            return reconstruct_path(came_from, current_city)

        for neighbor, distance in graph[current_city].items():
            tentative_g_score = g_score[current_city] + distance

            if tentative_g_score < g_score[neighbor]:
                came_from[neighbor] = current_city
                g_score[neighbor] = tentative_g_score
                f_score = tentative_g_score + heuristic(neighbor, goal)
                heapq.heappush(open_set, (f_score, neighbor))
    return None


def heuristic(start, goal):
    # Raio médio da Terra em quilômetros
    R = 6371.0
    # Converte as coordenadas de graus para radianos
    lat1, lon1 = map(radians, city_positions[start])
    lat2, lon2 = map(radians, city_positions[goal])
    # Diferença nas coordenadas
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    # Fórmula de Haversine
    a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    # Distância em quilômetros
    distance = R * c
    return distance


def reconstruct_path(came_from, current_city):
    path = [current_city]
    while current_city in came_from:
        current_city = came_from[current_city]
        path.insert(0, current_city)
    return path


def plot_brazil_map(graph, path, closed):
    pos = city_positions
    node_size = 300
    node_color = 'lightblue'
    font_size = 10
    nx.draw(graph, pos, with_labels=True, node_size=node_size, node_color=node_color, font_size=font_size)

    edges = [(path[i], path[i + 1]) for i in range(len(path) - 1)]
    nx.draw_networkx_edges(graph, pos, edgelist=edges, edge_color='orange', width=2)

    edges = [(closed[i][0], closed[i][1]) for i in range(len(closed))]
    nx.draw_networkx_edges(graph, pos, edgelist=edges, edge_color='red', width=2)
    plt.axis('equal')
    plt.show()


def get_closed_roads():
    cities = choices(list(distances_cities.keys()), k=8)
    closed_roads = []
    for city in cities:
        if len(distances_cities[city]) <= 1:
            continue
        close = [city, choice(list(distances_cities[city]))]
        closed_roads.append(close)
        distances_cities[close[0]].pop(close[1])
        distances_cities[close[1]].pop(close[0])
    return closed_roads


if __name__ == '__main__':
    closed_roads = get_closed_roads()

    G = nx.Graph()
    for city, neighbors in distances_cities.items():
        for neighbor, distance in neighbors.items():
            G.add_edge(city, neighbor, weight=distance)

    start_city = 'Porto Alegre'
    goal_city = 'Boa Vista'
    path = a_star(distances_cities, start_city, goal_city)

    if path:
        print("Caminho encontrado:", " -> ".join(path))
        plot_brazil_map(G, path, closed_roads)
    else:
        print("Caminho não encontrado.")
