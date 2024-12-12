#!/usr/bin/env python3

import sys
from collections import Counter

lines = [list(l.strip()) for l in open(sys.argv[1], 'r').readlines()]
total = 0
xmasctr = Counter(['M', 'M', 'S', 'S'])
for y in range(1, len(lines) - 1):
    for x in range(1, len(lines[0]) - 1):
        if lines[y][x] != 'A':
            continue
        c = Counter([lines[y-1][x-1], lines[y-1][x+1], lines[y+1][x+1], lines[y+1][x-1]])
        if c != xmasctr:
            continue

        if lines[y-1][x-1] != lines[y+1][x+1] and lines[y-1][x+1] != lines[y+1][x-1]:
            total += 1
print(total)
