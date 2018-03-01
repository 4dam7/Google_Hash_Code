#!/usr/bin/python3

import sys
from simulation import *
from obj import *


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
        best.rides_done.append(r.id)
        best.start = r.start
        best.stop = r.stop
        best.status = "busy"

def not_busy(free, busy):
    for car in busy:
        if car.status == "free":
            busy.append(car)
            free.remove(car)

i = 0
rides = []
stat = 0

with open(sys.argv[1]) as f:
    content = f.readlines()
    for line in content:
        if i == 0:
            stat = Stat(line)
            i += 1
        else:
            rides.append(Ride(line, i - 1))
            i += 1


busy = []
free = stat.vehicles

print(free, busy, rides)

while (end(busy, rides)):
    not_busy(busy, rides)
    assign_car(free, busy, rides)
    for car in busy:
        car.move()

for car in free:
    print(car.rides_done)
