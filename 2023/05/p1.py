#!/usr/bin/env python3
import sys
from shared import *
with open(sys.argv[1], 'r') as f:
    seeds = [int(s) for s in f.readline().strip()[len('seeds: '):].split(' ')]
    f.readline()
    f.readline()
    almanac = parse_almanac(f)
    smallest = float('inf')
    for seed in seeds:
        loc = almanac.convert_seed_to_location(seed)
        if loc < smallest:
            smallest = loc
    # too high:
    # 682713968
    print(smallest)
