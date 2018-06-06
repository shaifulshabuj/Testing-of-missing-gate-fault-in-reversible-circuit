import random
import sys
import os
import math


def rev_simulator(circuit, population, gate_detection, wire, gate):
    col = 2 * gate + 1
    temp = []
    fitness = []
    d = 0

    for m in range(0, len(population)):
        #print('Vector %d :', m+1)
        for i in range(0, wire):
            circuit[i][0] = population[m][i]

        for i in range(0, wire+1):
            temp.insert(i, 5)

        for i in range(0, col):
            if i % 2 != 0:
                for j in range(0, wire):
                    if circuit[j][i] == 0:
                        if circuit[j][i-1] == 0:
                            temp[j] = 1
                        elif circuit[j][i-1] == 1:
                            temp[j] = 0
                    elif circuit[j][i] == 1:
                        if circuit[j][i-1] == 0:
                            temp[j] = 0
                        elif circuit[j][i-1] == 1:
                            temp[j] = 1
                    elif circuit[j][i] == 2:
                        temp[j] = circuit[j][i-1]

                c = 0
                for j in range(0, wire):
                    if circuit[j][i] == 2:
                        for k in range(0, wire):
                            if k != j and circuit[k][i] == 3:
                                c = c+1

                            if c != wire-1:
                                if k != j and circuit[k][i] != 3:
                                    temp[wire] = temp[k]
                                    for p in range(0, wire):
                                        if p != j and p != k and circuit[p][i] != 3:
                                            temp[wire] = temp[wire] & temp[p]
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

        fitness[m] = d

        d = 0

    return fitness
