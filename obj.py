#!/usr/bin/python3

import sys
from simulation import *

class Vehicule:
    def __init__(self):
        self.pos = [0, 0]
        self.status = "free"
        self.dest = 0;
    def move(self, vect):
        if self.dest == 0:

class Ride:
    def __init__(self, line):
        array = line.split(' ')
        self.riding = 0
        self.start = [int(array[0]), int(array[1])]
        self.stop = [int(array[2]), int(array[3])]
        self.early = int(array[4])
        self.late = int(array[5])

class Stat:
    def __init__(self, line):
        array = line.split(' ')
        self.vehicles = []
        grid = create_grid(array[0], array[1])
        for i in range(0, array[2]):
            self.vehicles.append(Vehicule())
        self.bonus = array[4]
        self.steps = array[5]
