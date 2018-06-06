import random
import sys
import os
import math


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


print('Enter the number of wires: ')
wires = sys.stdin.readline()
print('Enter the number of gates: ')
gates = sys.stdin.readline()

wire = int(wires)
gate = int(gates)

circuit_def = circuit_define(wire, gate)

print(circuit_def)
