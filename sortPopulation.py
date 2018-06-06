import random
import sys
import os
import math


def sort_population(array_name, fit_array, pop_size):
    sort_array = []

    j = 0
    while j < pop_size:
        for i in range(0, len(array_name)):
            if array_name[i][2] == max(fit_array):
                sort_array.append(array_name[i])
                del array_name[i]
                del fit_array[i]
                break
        j = j + 1

    array_name = sort_array

    return array_name


a = [[[0], [1], 2], [[1], [0], 3], [[1], [1], 2], [[0], [0], 1]]
b = [2, 3, 2, 1]
c = sort_population(a, b, 4)

b = []

for i in range(0, len(c)):
    b.append(c[i][2])

print(c)
print(b)
#####

