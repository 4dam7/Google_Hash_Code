#!/usr/bin/python3

import sys
from simulation import *

def create_grid(rows, cols):
    grid = []
    for i in range(0, cols):
        grid.append(list());
        for n in range(0, rows):
            grid[i].append(0);
    return (grid)

class Vehicule:
    def __init__(self):
        self.pos = [0, 0]
        self.status = "free"
        self.dest_1 = 0
        self.dest_2 = 0
        self.rides_done = []

    def get_vector(self, dest):
        vect = []
        vect.append(dest[0] - self.pos[0])
        vect.append(dest[1] - self.pos[1])
        return (vect)

    def move(self, vect):
        if self.status == "free":
            return
        vect1 = self.get_vector(self.dest_1)
        vect2 = self.get_vector(self.dest_2)
        if vect1 != [0, 0]:
            if vect1[0] != 0:
                if vect1[0] < 0:
                    self.pos[0] -= 1
                else:
                    self.pos[0] += 1
            else:
                if vect1[1] < 0:
                    self.pos[1] -= 1
                else:
                    self.pos[1] += 1
        else:
            if vect2[0] != 0:
                if vect2[0] < 0:
                    self.pos[0] -= 1
                else:
                    self.pos[0] += 1
            else:
                if vect2[1] < 0:
                    self.pos[1] -= 1
                else:
                    self.pos[1] += 1

        if vect1 == [0, 0] and vect2 == [0, 0]:
            self.status = "free"

class Ride:
    def __init__(self, line, i):
        array = line.split(' ')
        self.riding = 0
        self.start = [int(array[0]), int(array[1])]
        self.stop = [int(array[2]), int(array[3])]
        self.early = int(array[4])
        self.late = int(array[5])
        self.start = []
        self.stop = []
        self.id = i

class Stat:
    def __init__(self, line):
        array = line.split(' ')
        self.vehicles = []
        grid = create_grid(int(array[0]), int(array[1]))
        for i in range(0, int(array[2])):
            self.vehicles.append(Vehicule())
        self.bonus = int(array[4])
        self.steps = int(array[5])

def end(busy, rides):
    if not busy and not rides:
        return 0
    else:
        return 1
