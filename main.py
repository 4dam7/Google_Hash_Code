#!/usr/bin/python3

import sys
from simulation import *
from obj import *


i = 0
rides = []
with open(sys.argv[1]) as f:
    content = f.readlines()
    for line in content:
        if i == 0:
            stat = Stat(line)
        else:
            rides.append(Ride(line))
            i += 1

for v in rides:
    print(v.start, v.stop, v.early, v.late)


def assign_car(free, busy, rides):
    for r in rides:
        best = "NULL"
        for car in free:
            if car.get_vector(r)[0] + car.get_vector(r)[0] < best or best == "NULL":
                best = car
        if best == "NULL":
            return
        free.remove(best)
        busy.append(best)
        best.start = r.start
        best.stop = r.stop
        best.status = "busy"

def not_busy(free, busy):
    for car in busy:
        if car.status == "free":
            busy.append(car)
            free.remove(car)


busy = []
free = []

