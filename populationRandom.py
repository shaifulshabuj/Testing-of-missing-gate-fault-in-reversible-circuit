import random
import sys
import os
import math


def population_generate(population_size, chromosome_length):
    population = []
    list1 = []
    for j in range(0, chromosome_length):
        list1.insert(j, random.randrange(0, 2))

    population.insert(0, list1)

    list1 = []
    for j in range(0, chromosome_length):
        list1.insert(j, random.randrange(0, 2))

    for i in range(1, population_size):
        while list1 in population[0:len(population)]:
            list1 = []
            for j in range(0, chromosome_length):
                list1.insert(j, random.randrange(0, 2))
        population.insert(i, list1)
        list1 = []
        for j in range(0, chromosome_length):
            list1.insert(j, random.randrange(0, 2))
    list1 = []

    return population


print('Enter the number of wires: ')
wires = sys.stdin.readline()
print('Enter the number of gates: ')
gates = sys.stdin.readline()

wire = int(wires)
gate = int(gates)
length_chromosome = wire
size_population = int(math.ceil(0.2*(2**wire)))

generated_population = population_generate(size_population, length_chromosome)

print(length_chromosome)
print(size_population)
print('Population')
print(generated_population)
