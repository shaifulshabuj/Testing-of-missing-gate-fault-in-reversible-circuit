import random
import sys
import os
import math


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


a1 = [1, 3, 1, 5, 4]

parent1 = binary_tournament_selection(a1, len(a1))

i = 0
while i == 0:
    parent2 = binary_tournament_selection(a1, len(a1))
    if parent1 != parent2:
        break

print(parent1)
print(parent2)

a = [0, 1, 1, 1]
a1 = [0, 1, 0, 0]

del a[2]

print(a)



