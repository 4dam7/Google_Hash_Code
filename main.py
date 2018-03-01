#!/usr/bin/python3

import sys
from simulation import *
from obj import *


i = 0
r_array = []
with open(sys.argv[1]) as f:
    content = f.readlines()
    for line in content:
        if i == 0:
            stat = Stat(line)
        else:
            r_array.append(Ride(line))
            i += 1

for v in r_array:
    print(v.start, v.stop, v.early, v.late)
