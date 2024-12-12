#!/usr/bin/env python3

import sys

lines = [list(l.strip()) for l in open(sys.argv[1], 'r').readlines()]

total = 0

for y in range(len(lines)):
    cangodown = y + 3 < len(lines)
    cangoup = y - 3 >= 0
    for x in range(len(lines[0])):
        l = lines[y]
        cangoright = x + 3 < len(l)
        cangoleft = x - 3 >= 0

        if l[x] != 'X':
            continue
        # backwards
        if x >= 3 and lines[y][x-1] == 'M' and lines[y][x-2] == 'A' and lines[y][x-3] == 'S':
            total += 1
        # forwards horizontal
        if x + 3 < len(l) and l[x+1] == 'M' and l[x+2] == 'A' and l[x+3] == 'S':
            total += 1
        # diagonal to right
        if x + 3 < len(l):
            # diagonal up right
            if y - 3 >= 0 and lines[y-1][x+1] == 'M' and lines[y-2][x+2] == 'A' and lines[y-3][x+3] == 'S':
                total += 1
            # diagonal down right
            if y + 3 < len(lines) and lines[y+1][x+1] == 'M' and lines[y+2][x+2] == 'A' and lines[y+3][x+3] == 'S':
                total += 1
        # diagonal to left
        if cangoleft:
            # diagonal up left
            if cangoup and lines[y-1][x-1] == 'M' and lines[y-2][x-2] == 'A' and lines[y-3][x-3] == 'S':
                total += 1
            # diagonal downleft
            if cangodown and lines[y+1][x-1] == 'M' and lines[y+2][x-2] == 'A' and lines[y+3][x-3] == 'S':
                total += 1
        if cangoup and lines[y-1][x] == 'M' and lines[y-2][x] == 'A' and lines[y-3][x] == 'S':
            total += 1
        if cangodown and lines[y+1][x] == 'M' and lines[y+2][x] == 'A' and lines[y+3][x] == 'S':
            total += 1
print(total)
