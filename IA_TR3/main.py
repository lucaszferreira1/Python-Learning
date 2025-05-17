import math
import random
import numpy as np
import matplotlib.pyplot as plt

class PSO:
    def __init__(self, function, dimensions, lower_bound, upper_bound, num_particles, max_iter, cognitive, social):
        self.function = function
        self.dimensions = dimensions
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound
        self.num_particles = num_particles
        self.max_iter = max_iter
        self.cognitive = cognitive
        self.social = social
        self.particles = [self.create_particle() for _ in range(num_particles)]
        self.global_best_position = None
        self.global_best_fitness = float('inf')
    
    def create_particle(self):
        return Particle(self.dimensions, self.lower_bound, self.upper_bound, self.function)
    
    def optimize(self):
        for _ in range(self.max_iter):
            best_fitness_iter = float('inf')
            for particle in self.particles:
                if particle.fitness < self.global_best_fitness:
                    self.global_best_fitness = particle.fitness
                    self.global_best_position = particle.position.copy()
            for particle in self.particles:
                particle.update_velocity(self.cognitive, self.social, self.global_best_position)
                particle.position = [max(min(particle.position[i] + particle.velocity[i], self.upper_bound), self.lower_bound) for i in range(self.dimensions)]
                particle.udpate_fitness(self.function)
                if particle.fitness < best_fitness_iter:
                    best_fitness_iter = particle.fitness
            fitnesses.append(best_fitness_iter)
        return self.global_best_position, self.global_best_fitness

class Particle:
    def __init__(self, dimensions, lower_bound, upper_bound, function):
        self.position = [random.uniform(lower_bound, upper_bound) for _ in range(dimensions)]
        self.velocity = [random.uniform(-1, 1) for _ in range(dimensions)]
        self.fitness = function(self.position)
        self.best_position = self.position.copy()
        self.best_fitness = self.fitness

    def update_velocity(self, cognitive, social, global_best_position):
        r1 = [random.random() for _ in range(len(self.position))]
        r2 = [random.random() for _ in range(len(self.position))]
        cognitive_velocity = [cognitive * r1[i] * (self.best_position[i] - self.position[i]) for i in range(len(self.position))]
        social_velocity = [social * r2[i] * (global_best_position[i] - self.position[i]) for i in range(len(self.position))]
        phi = social + cognitive
        constriction = 2 / math.fabs(2 - phi - math.sqrt(phi**2 - 4 * phi))
        self.velocity = [constriction * (self.velocity[i] + cognitive_velocity[i] + social_velocity[i]) for i in range(len(self.position))]
    
    def udpate_fitness(self, function):
        self.fitness = function(self.position)
        if self.fitness < self.best_fitness:
            self.best_position = self.position.copy()
            self.best_fitness = self.fitness
    
def griewank(sol):
    top1 = sum(x**2 for x in sol)
    top2 = math.prod(math.cos((x / math.sqrt(i + 1)) * math.pi / 180) for i, x in enumerate(sol))
    top = (1 / 4000) * top1 - top2 + 1
    return top

def ackley(sol):
    DIM = len(sol)
    aux = sum(x**2 for x in sol)
    aux1 = sum(math.cos(2.0 * math.pi * x) for x in sol)
    result = -20.0 * math.exp(-0.2 * math.sqrt(aux / DIM)) - math.exp(aux1 / DIM) + 20.0 + math.exp(1)
    return result

restrictions = {
    'griewank': {
        'lower_bound': -600,
        'upper_bound': 600,
        'function': griewank
    },
    'ackley': {
        'lower_bound': -32,
        'upper_bound': 32,
        'function': ackley
    }
}

if __name__ == "__main__":
    function_name = 'griewank'
    config = restrictions[function_name]
    fitnesses = []
    pso = PSO(
        function=config['function'],
        dimensions=10,
        lower_bound=config['lower_bound'],
        upper_bound=config['upper_bound'],
        num_particles=30,
        max_iter=1000,
        cognitive=2.05,
        social=2.05
    )
    
    num_runs = 30
    best_fitness_values = []
    all_fitnesses = []
    for i in range(num_runs):
        fitnesses = []
        pso = PSO(
            function=config['function'],
            dimensions=10,
            lower_bound=config['lower_bound'],
            upper_bound=config['upper_bound'],
            num_particles=30,
            max_iter=1000,
            cognitive=2.05,
            social=2.05
        )
        best_position, best_fitness = pso.optimize()
        best_fitness_values.append(best_fitness)
        all_fitnesses.append(fitnesses)
        print(f"Run {i+1}: Best fitness = {best_fitness}")

    std_dev = np.std(best_fitness_values)
    avg_fitness = np.mean(best_fitness_values)
    min_fitness = np.min(best_fitness_values)

    print(f"\nAnalysis of {num_runs} runs:")
    print(f"Standard Deviation: {std_dev}")
    print(f"Average Fitness: {avg_fitness}")
    print(f"Minimum Fitness: {min_fitness}")
