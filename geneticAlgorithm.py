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


def test_candidate_array(population_size, number_of_gate):
    test_candidate = [[0] * number_of_gate for i in range(population_size)]

    for i in range(0, population_size):
        for j in range(0, number_of_gate):
            test_candidate[i][j] = 0
    return test_candidate


def circuit_define(wire_number, gate_number):
    col = 2 * gate_number + 1
    circuit = [[0] * col for i in range(wire_number)]

    for i in range(0, col):
        if i % 2 != 0:
            print("Gate No: %d" % ((i / 2) + 1))
            for j in range(0, wire_number):
                circuit[j][i] = int(sys.stdin.readline())
        else:
            for j in range(0, wire_number):
                circuit[j][i] = 4

    return circuit


def rev_simulator(circuit, population, gate_detection, wire, gate):
    col = 2 * gate + 1
    temp = []
    fitness = []
    d = 0

    for m in range(0, len(population)):
        for i in range(0, wire):
            circuit[i][0] = population[m][i]

        for i in range(0, wire+1):
            temp.insert(i, 5)

        for i in range(0, col):
            if i % 2 != 0:
                for j in range(0, wire):
                    if circuit[j][i] == 0:
                        if circuit[j][i-1] == 0:
                            temp.insert(j, 1)
                        elif circuit[j][i-1] == 1:
                            temp.insert(j, 0)
                    elif circuit[j][i] == 1:
                        if circuit[j][i-1] == 0:
                            temp.insert(j, 0)
                        elif circuit[j][i-1] == 1:
                            temp.insert(j, 1)
                    elif circuit[j][i] == 2:
                        temp.insert(j, circuit[j][i-1])

                c = 0
                for j in range(0, wire):
                    if circuit[j][i] == 2:
                        for k in range(0, wire):
                            if k != j and circuit[k][i] == 3:
                                c = c+1

                            if c != wire-1:
                                if k != j and circuit[k][i] != 3:
                                    temp.insert(wire, temp[k])
                                    for p in range(0, wire):
                                        if p != j and p != k and circuit[p][i] != 3:
                                            temp.insert(wire, temp[wire] & temp[p])
                                    break
                            else:
                                break

                        if c != wire-1:
                            temp[j] = temp[j] ^ temp[wire]
                            circuit[j][i+1] = temp[j]
                        else:
                            if circuit[j][i-1] == 0:
                                circuit[j][i+1] = 1
                            else:
                                circuit[j][i+1] = 0

                for j in range(0, wire):
                    if circuit[j][i] == 0:
                        if circuit[j][i-1] == 0:
                            circuit[j][i+1] = 0
                        elif circuit[j][i-1] == 1:
                            circuit[j][i+1] = 1
                    elif circuit[j][i] == 1:
                        if circuit[j][i-1] == 1:
                            circuit[j][i+1] = 1
                        elif circuit[j][i-1] == 0:
                            circuit[j][i+1] = 0
                    elif circuit[j][i] == 3:
                        circuit[j][i+1] = circuit[j][i-1]

        for i in range(0, col):
            if i % 2 != 0:
                change = False
                for j in range(0, wire):
                    if circuit[j][i] != 2 and circuit[j][i] != circuit[j][i-1] and circuit[j][i] != 3:
                        change = True
                        break
                if change is False:
                    gate_detection[m][i//2] = 1
                    d = d + 1

        fitness.insert(m, d)

        d = 0

    return fitness


def binary_tournament_selection(array_name, length_pop):
    fit_one = random.randrange(0, length_pop)

    for i in [0]:
        fit_two = random.randrange(0, length_pop)
        if fit_one != fit_two:
            break

    if array_name[fit_one] > array_name[fit_two]:
        return fit_one
    else:
        return fit_two


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


def mutation(array_name, length):
    position = random.randrange(0, length)

    for i in range(0, 2):
        for j in range(0, length):
            if j == position:
                if array_name[i][j] == 0:
                    array_name[i][j] = 1
                else:
                    array_name[i][j] = 0

    return array_name


print('Enter the number of wires: ')
wires = int(sys.stdin.readline())
print('Enter the number of gates: ')
gates = int(sys.stdin.readline())

length_chromosome = wires
size_population = int(math.ceil(0.2*(2**wires)))

generated_population = population_generate(size_population, length_chromosome)
defined_circuit = circuit_define(wires, gates)
defined_test_candidate = test_candidate_array(size_population, gates)
fitness_population = rev_simulator(defined_circuit, generated_population, defined_test_candidate, wires, gates)

print(length_chromosome)
print(size_population)
print('Population')
print(generated_population)
print('Circuit')
print(defined_circuit)
print('Simulation and fitness')
print(fitness_population)
print('Max Fitness: ', end=" ")
print(max(fitness_population))
print('\n')

vector = {0: ""}
vector_analysis = {0: ""}

for i in range(size_population):
    vector[i] = generated_population[i], defined_test_candidate[i], fitness_population[i]

for j in range(0, len(vector_analysis)):
    for i in range(size_population):
        if vector[i][2] == max(fitness_population):
            vector_analysis[j] = vector[i]

print('Population with gate detection array and fitness :')
for i in range(size_population):
    print(vector[i])

print('\nVector Analysis :')
for i in range(len(vector_analysis)):
    print(vector_analysis[i])


