import random
import matplotlib.pyplot as plt
import numpy as np
import statistics

N_VARIABLES = 250
FILE_NAME = f'uf{N_VARIABLES}-01.cnf'

MAX_I = 30
INI_TEMP = 1
MAX_CYCLE = 10000
SA_MAX = 1 # Criar um gráfico para 1, 5 e 10

scores = []
temps = []

class Variable:
    def __init__(self, input):
        v = int(input)
        if v < 0:
            self.k = v * -1
            self.n = True
        else:
            self.k = v
            self.n = False


class Expression:
    def __init__(self, v1, v2, v3):
        self.variables = [v1, v2, v3]
    
    def calc(self, values):
        res = False
        for i in self.variables:
            if i.n:
                res = res or not values[i.k - 1]
            else:
                res = res or values[i.k - 1]
        return res

    def __str__(self):
        str = ''
        for i in self.variables:
            if i.n:
                str += '~'
            str += f'{i.k}'
            str += ' V '
        return str[:-3]


class Sat3:
    def __init__(self):
        self.expressions = []
    
    def calc(self, values):
        cont = 0
        for expression in self.expressions:
            ans = expression.calc(values)
            cont += 1 if ans else 0
        return cont

    def check(self, values):
        res = True
        for expression in self.expressions:
            ans = expression.calc(values)
            res = res and ans
        return bool(res)


def temp_calc1(i):
    return INI_TEMP - i * ((INI_TEMP - 0.01) / MAX_CYCLE)

def temp_calc2(i):
    return INI_TEMP * ((0.01 / INI_TEMP) ** (i / MAX_CYCLE))

def temp_calc3(i):
    A = (1 / (MAX_CYCLE ** 2)) * np.log(INI_TEMP / 0.01)
    return INI_TEMP * np.exp(-A * (i ** 2))

def get_random_neighbour(values):
    neighbour = values.copy()
    i = random.randint(0, N_VARIABLES - 1)
    neighbour[i] = True if not neighbour[i] else False
    return neighbour


def simulated_annealing(sat):
    values = [0] * N_VARIABLES
    cont = 0
    temp = INI_TEMP
    val_scores = []
    while(True):
        if (temp <= 0.001 or cont >= MAX_CYCLE):
            scores.append(val_scores)
            return values
        for i in range(0, SA_MAX):
            neighbour = get_random_neighbour(values)
            current_score = sat.calc(values)
            val_scores.append(current_score)
            temps.append(temp)
            neighbor_score = sat.calc(neighbour)
            deltaE = neighbor_score - current_score
            if deltaE >= 0:
                values = neighbour
            else:
                chance = np.exp(deltaE / temp)
                dado = random.random()
                if dado <= chance:
                    values = neighbour
        temp = temp_calc2(cont)
        cont += 1


if __name__ == '__main__':
    file = open(FILE_NAME, 'r')
    sat = Sat3()
    for line in file:
        res = line.split(' ')
        expr = Expression(Variable(res[0]), Variable(res[1]), Variable(res[2]))
        sat.expressions.append(expr)
    
    count = 0
    count_right = 0

    results = []
    boxplot_contents = []
    graph_score = []
    
    sas = [1, 5, 10]
    for sa in sas:
        SA_MAX = sa
        for i in range(0, MAX_I):
            print(i + 1)
            output = simulated_annealing(sat)
            results.append(sat.calc(output))
            if i == 0:
                graph_score = scores[i].copy()
            if sat.check(output):
                graph_score = scores[i].copy()
                count_right += 1
        print(f"{(count_right / (i + 1)) * 100}%")
        
        
        print(f"Média = {statistics.mean(results)}")
        print(f"Desvio Padrão = {statistics.stdev(results)}")
        plt.plot(graph_score)
        boxplot_contents.append(results.copy())
        scores.clear()
        temps.clear()
        results.clear()
        graph_score.clear()
        count = 0
        count_right = 0


    plt.title(f"Gráfico de Convergência\n(N_VARIABLES = {N_VARIABLES}, MAX_I = {MAX_I}, MAX_CYCLE = {MAX_CYCLE}, SA_MAX = {SA_MAX})")
    plt.xlabel("Iteração")
    plt.ylabel("Energia")
    
    filename = f"{N_VARIABLES}_SA{SA_MAX}.png"
    plt.savefig(filename)
    plt.clf()

    # plt.title("Gráfico de temperatura")
    # plt.ylabel("Temperatura")
    # plt.plot(temps)
    # plt.show()

    plt.title(f"Boxplot\n(N_VARIABLES = {N_VARIABLES}, MAX_I = {MAX_I}, MAX_CYCLE = {MAX_CYCLE}, SA_MAX = {SA_MAX})")
    plt.xlabel(f"{N_VARIABLES}")
    plt.ylabel("Energia")
    plt.boxplot(boxplot_contents)
    filename = f"B{N_VARIABLES}_SA{SA_MAX}.png"
    plt.savefig(filename)
