#!/usr/bin/env python3
import sys
from shared import *

def reduce_seed_groups(seed_groups, almanac):
    new_groups = []
    if len(seed_groups) == 0:
        return [] # other base case
    for sg in seed_groups:
        if type(sg) == int:
            new_groups.append(sg)
        elif sg[0] == sg[1]:
            new_groups.append(sg[0])
        elif almanac.trace(sg[0]) == almanac.trace(sg[1]):
            new_groups.append(sg[0])
        elif sg[0] == sg[1] - 1:
            new_groups += [sg[0], sg[1]]
        else:
            assert sg[0] < sg[1]
            length = 1 + (sg[1] - sg[0])
            preg = (sg[0], sg[0] + length // 2)
            postg = (sg[0] + length // 2 + 1, sg[1])
            new_groups += reduce_seed_groups((preg, postg), almanac)
    return new_groups
with open(sys.argv[1], 'r') as f:
    seed_pre_pairs = [int(s) for s in f.readline().strip()[len('seeds: '):].split(' ')]
    seed_groups = []
    for i in range(0, len(seed_pre_pairs), 2):
        startinclusive = seed_pre_pairs[i]
        endinclusive = startinclusive + seed_pre_pairs[i + 1] - 1
        seed_groups.append((startinclusive, endinclusive))
    f.readline()
    f.readline()
    almanac = parse_almanac(f)
    seed_groups = reduce_seed_groups(seed_groups, almanac)
    smallest = float('inf')
    for seed in seed_groups:
        loc = almanac.convert_seed_to_location(seed)
        if loc < smallest:
            smallest = loc
    print(smallest)
