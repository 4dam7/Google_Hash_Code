#!/usr/bin/python3

import sys


class Vehicle:
    def __init__(self, line):
        array = line.split(' ')
        self.riding = 0;
        self.start = [int(array[0]), int(array[1])]
        self.stop = [int(array[2]), int(array[3])]
        self.early = int(array[4])
        self.late = int(array[5])

"""
v_array = []
with open(sys.argv[1]) as f:
    content = f.readlines()
    for line in content:
        v_array.append(Vehicle(line))

for v in v_array:
    print(v.start, v.stop, v.early, v.late)"""