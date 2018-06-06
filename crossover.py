import random
import sys
import os
import math


def crossover(array_name, length):
    offspring = [[0] * length for i in range(len(array_name))]

    position = random.randrange(0, length)
    for i in range(0, length):
        if i <= position:
            offspring[0][i] = array_name[0][i]
            offspring[1][i] = array_name[1][i]
        else:
            offspring[0][i] = array_name[1][i]
            offspring[1][i] = array_name[0][i]

    return offspring


a = [[0, 1, 1, 1], [1, 0, 0, 0]]
after_crossover = crossover(a, 4)

print(after_crossover)
