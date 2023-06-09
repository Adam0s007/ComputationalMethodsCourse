import math
import random

def energy(x):
    return x**2  # funkcja, której minimum chcemy znaleźć

def neighbour_state(x):
    return x + random.uniform(-1, 1)  # generujemy stan sąsiedni

def temperature(i):
    return max(0.01, min(1, 1 - 0.01*i))  # zaczynamy od temperatury 1 i stopniowo ją obniżamy

def simulated_annealing():
    C = random.uniform(-10, 10)  # losowy stan początkowy
    best_C = C

    number_of_iterations = 1000000
    for i in range(number_of_iterations):
        new_C = neighbour_state(C)
        delta_E = energy(new_C) - energy(C)

        if delta_E < 0 or math.exp(-delta_E / temperature(i)) > random.random():
            C = new_C
            if energy(C) < energy(best_C):
                best_C = C

    return best_C

solution = simulated_annealing()
print(f'Minimum of the function is at x = {solution} with value {energy(solution)}')
