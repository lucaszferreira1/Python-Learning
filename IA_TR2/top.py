import random
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.animation import FuncAnimation

N_CIDADES = 100
FILE_NAME = f'{N_CIDADES}_cities.txt'

INI_TEMP = 10000
MAX_CYCLE = 100000
SA_MAX = 1

class City:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
    
    def distance(self, city):
        return ((self.x - city.x) ** 2 + (self.y - city.y) ** 2) ** 0.5


class Map:
    def __init__(self, cities):
        self.cities = cities
        self.distance_matrix = [[0 for _ in range(len(cities))] for _ in range(len(cities))]
        for i in range(len(cities)):
            for j in range(len(cities)):
                if i != j:
                    self.distance_matrix[i][j] = cities[i].distance(cities[j])
    
    def get_distance(self, city1, city2):
        return self.distance_matrix[city1][city2]

    def plot_cities(self, values=None, output_file='city_map.png'):
        x_coords = [city.x for city in self.cities]
        y_coords = [city.y for city in self.cities]
        plt.scatter(x_coords, y_coords, c='blue', marker='o')
        for city in self.cities:
            plt.text(city.x, city.y, str(city.id), fontsize=8, ha='right')
        
        if values:
            path_x = [self.cities[i].x for i in values] + [self.cities[values[0]].x]
            path_y = [self.cities[i].y for i in values] + [self.cities[values[0]].y]
            plt.plot(path_x, path_y, c='red', linestyle='-', linewidth=1, marker='o')
        
        plt.title("Mapa da Cidade")
        plt.xlabel("X")
        plt.ylabel("Y")
        plt.savefig(output_file)
        plt.close()
    
    def create_gif(self, results, interval=200, output_file='path_evolution.gif'):
        fig, ax = plt.subplots()
        x_coords = [city.x for city in self.cities]
        y_coords = [city.y for city in self.cities]
        ax.scatter(x_coords, y_coords, c='blue', marker='o')
        for city in self.cities:
            ax.text(city.x, city.y, str(city.id), fontsize=8, ha='right')
        
        line, = ax.plot([], [], c='red', linestyle='-', linewidth=1, marker='o')

        def update(frame):
            path = results[frame]
            path_x = [self.cities[i].x for i in path] + [self.cities[path[0]].x]
            path_y = [self.cities[i].y for i in path] + [self.cities[path[0]].y]
            line.set_data(path_x, path_y)
            return line,

        ani = FuncAnimation(fig, update, frames=len(results), interval=interval, blit=True)
        ani.save(output_file, writer='imagemagick')
        plt.close()


def calc(values, mapa):
    e = 0
    for i in range(len(values) - 1):
        if values[i] and values[i + 1]:
            e += mapa.get_distance(values[i], values[i + 1])
    e += mapa.get_distance(values[0], values[i])
    return e


def temp_calc1(i):
    return INI_TEMP - i * ((INI_TEMP - 0.01) / MAX_CYCLE)

def temp_calc2(i):
    return INI_TEMP * ((0.01 / INI_TEMP) ** (i / MAX_CYCLE))

def temp_calc3(i):
    A = (1 / (MAX_CYCLE ** 2)) * np.log(INI_TEMP / 0.01)
    return INI_TEMP * np.exp(-A * (i ** 2))

def get_random_neighbour(values):
    neighbour = values.copy()
    i, j = random.sample(range(len(neighbour)), 2)
    neighbour[i], neighbour[j] = neighbour[j], neighbour[i]
    return neighbour

def simulated_annealing(values, mapa):
    cont = 0
    temp = INI_TEMP
    while(True):
        if (temp <= 0.001 or cont >= MAX_CYCLE):
            return values
        for i in range(0, SA_MAX):
            neighbour = get_random_neighbour(values)
            current_score = calc(values, mapa)
            neighbor_score = calc(neighbour, mapa)
            deltaE = neighbor_score - current_score
            if deltaE <= 0:
                paths.append(values.copy())
                values = neighbour
            else:
                chance = np.exp(-deltaE / temp)
                dado = random.random()
                if dado <= chance:
                    values = neighbour
        temp = temp_calc2(cont)
        cont += 1
        results.append(current_score)
        if cont % (MAX_CYCLE / 10) == 0:
            print(f'Cont: {cont}')


def get_cities_from_file(file):
    cities = []
    for line in file:
        params = line.split(' ')
        city = City(int(params[0]), int(params[1]), int(params[2]))
        cities.append(city)
    return cities


def plot_results(output_file='results.png'):
    plt.title("Gráfico de Convergência")
    plt.legend()
    plt.xlabel("Iteração")
    plt.ylabel("Distância")
    plt.savefig(output_file)
    plt.close()

def create_boxplot(results, output_file='boxplot.png'):
    plt.boxplot(results)
    plt.xticks([1, 2, 3], ['SA_MAX = 1', 'SA_MAX = 5', 'SA_MAX = 10'])
    plt.title("Gráfico Boxplot")
    plt.xlabel("SA_MAX")
    plt.ylabel("Distância")
    plt.savefig(output_file)
    plt.close()


if __name__ == '__main__':
    file = open(FILE_NAME, 'r')
    mapa = Map(get_cities_from_file(file))
    file.close()
    results_finais = []
    results = []
    for i in [1, 5, 10]:
        SA_MAX = i
        paths = []
        values = [i for i in range(len(mapa.cities))]
        random.shuffle(values)
        result = simulated_annealing(values, mapa)
        print(f'Distância: {calc(result, mapa)}')
        results_finais.append(results.copy())
        plt.plot(results, label=f'SA_MAX = {SA_MAX}')
        results.clear()
    plot_results(output_file=f'Conv_{N_CIDADES}.png')
    create_boxplot(results_finais, output_file=f'Boxp_{N_CIDADES}.png')
    mapa.plot_cities(result, output_file=f'Caminho_{N_CIDADES}.png')
    # mapa.create_gif(paths, interval=50, output_file='path_evolution.gif')
