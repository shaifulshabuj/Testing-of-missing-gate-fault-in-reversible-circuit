import random
import sys
import os
import math


def maximum_covered_index(a):
    maximum = 0
    for i in range(0, len(a)):
        if a[i][2] > maximum:
            maximum = a[i][2]
            address = i
    return address


def covered_array_maker(array_name, undetected_array_list):
    intermediate_list = []
    covered_list = []
    resulted_array = []

    for i in range(0, len(array_name)):
        if array_name[i][2] > 0:
            covered_list.append(array_name[i][0])
            for j in range(0, len(undetected_array_list)):
                if undetected_array_list[j] != -1:
                    intermediate_list.append(array_name[i][1][undetected_array_list[j]])
            covered_list.append(intermediate_list)
            covered_list.append(sum(intermediate_list))
            resulted_array.append(covered_list)
            covered_list = []
            intermediate_list = []

    return resulted_array


def cover_most_algorithm(array_name, number_of_gates):
    resulted_array = []
    undetected_gates = []
    check_gates = []
    for i in range(0, number_of_gates):
        undetected_gates.insert(i, i)
        check_gates.insert(i, 0)

    while sum(check_gates) != number_of_gates:
        covered_array = covered_array_maker(array_name, undetected_gates)
        max_covered_address = maximum_covered_index(covered_array)
        resulted_array.append(array_name[max_covered_address])
        for i in range(0, number_of_gates):
            if array_name[max_covered_address][1][i] == 1:
                undetected_gates[i] = -1
                check_gates[i] = 1
        del array_name[max_covered_address]

    return resulted_array


a1 = [[[1, 0, 0], [0, 0, 0, 1], 1], [[1, 0, 1], [1, 0, 0, 0], 1], [[0, 0, 1], [0, 1, 1, 0], 2],
      [[0, 1, 1], [0, 0, 1, 0], 1]]

result = cover_most_algorithm(a1, 4)
print(result)

