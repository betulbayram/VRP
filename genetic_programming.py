import random
import time
start_time = time.time()
# Define the number of vehicles and their capacity
num_vehicles = 1
vehicle_capacity = 100

# Define the locations of the customers and their demand
demands = [20, 30, 40, 10]

locations = ["Takkali-1", "Takkali-29", "Emek-4", "Şarhöyük"]
distances = {("Takkali-1", "Takkali-29"): 2.8,
             ("Takkali-1", "Emek-4"): 3.9,
             ("Takkali-1", "Şarhöyük"): 1.5,
             ("Takkali-29", "Takkali-1"):  2.8,
             ("Takkali-29", "Emek-4"): 0.8,
             ("Takkali-29", "Şarhöyük"): 4.0,
             ("Emek-4", "Takkali-1"): 3.9,
             ("Emek-4", "Takkali-29"): 0.8,
             ("Emek-4", "Şarhöyük"): 4.1,
             ("Şarhöyük", "Takkali-1"): 1.5,
             ("Şarhöyük", "Takkali-29"): 4.0,
             ("Şarhöyük", "Emek-4"): 4.1}

# Define the population size and the number of generations
pop_size = 50
num_generations = 50

# Initialize the population with random routes for each vehicle
population = []
for i in range(pop_size):
    routes = []
    for j in range(num_vehicles):
        route = []
        capacity = vehicle_capacity
        for a in range(0, len(demands)):
            for k in locations:
                if capacity - demands[a] >= 0:
                    route.append(k)
                    capacity -= demands[a]
        routes.append(route)
    population.append(routes)

# Evaluate the fitness of each solution by calculating the total distance of the routes
def evaluate_fitness(routes):
    total_distance = 0
    for route in routes:
        distance = 0
        for i in range(len(route) - 1):
            distance += distances[(route[i], route[i+1])]
        total_distance += distance
    return total_distance


fitnesses = [evaluate_fitness(routes) for routes in population]
print(f"Total Distance for genetic programming: {fitnesses[0]} km")
print(f"Algorithm Time: {time.time() - start_time}")