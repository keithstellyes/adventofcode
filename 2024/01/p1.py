#!/usr/bin/env python3

import heapq, sys

lines = None

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

l1 = []
l2 = []

for l in lines:
    id1, id2 = [int(n) for n in l.split('   ')]
    l1.append(id1)
    l2.append(id2)

l1.sort()
l2.sort()
total = 0

for id1, id2 in zip(l1, l2):
    total += abs(id1 - id2)

print(total)

