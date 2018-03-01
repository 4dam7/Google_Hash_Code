#!/usr/bin/python3

import sys

class Vehicule:
    def __init__(self):
        self.pos = [0, 0]

class Ride:
    def __init__(self, line):
        array = line.split(' ')
        self.riding = 0
        self.start = [int(array[0]), int(array[1])]
        self.stop = [int(array[2]), int(array[3])]
        self.early = int(array[4])
        self.late = int(array[5])

class stat:
    def __init__(self, line):
        array = line.split(' ')
        self.vehicule = []
        grid = create_grid(array[0], array[1])
        for i in range(0, array[2]):
            self.vehicules.append(Vehicule())
        self.bonus = array[4]
        self.steps = array[5]
i = 0
r_array = []
with open(sys.argv[1]) as f:
    content = f.readlines()
    for line in content:
        if i == 0:

        r_array.append(Ride(line))
        i++

for v in r_array:
    print(v.start, v.stop, v.early, v.late)
