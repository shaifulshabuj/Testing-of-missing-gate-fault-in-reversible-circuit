import random
import sys
import os
import math


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


a = [[0, 0, 0, 0], [1, 1, 1, 1]]

result = mutation(a, 4)
print(result)
