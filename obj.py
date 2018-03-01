#!/usr/bin/python3

import sys
from simulation import *

class Vehicule:
    def __init__(self):
        self.pos = [0, 0]
        self.status = "free"
        self.dest = 0

    def get_vector(self, dest):
        vect = []
        vect.append(dest[0] - self.pos[0])
        vect.append(dest[1] - self.pos[1])
        return (vect)

    def move(self, vect):
        if self.dest == 0:
            return
        vect = self.get_vector(self.dest)
        if vect[0] != 0:
            if vect[0] < 0:
                self.pos[0] -= 1;
            else:
                self.pos[0] += 1
        else:
            if vect[1] < 0:
                self.pos[1] -= 1;
            else:
                self.pos[1] += 1

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
