import random
import sys
import os
import math


def test_candidate_array(population_size, number_of_gate):
    test_candidate = [[0] * number_of_gate for i in range(population_size)]

    for i in range(0, population_size):
        for j in range(0, number_of_gate):
            test_candidate[i][j] = 0
    return test_candidate


test = test_candidate_array(5, 4)

print(test)
