#!/usr/bin/env python3

import sys

rows = [list(l.strip()) for l in open(sys.argv[1], 'r').readlines()]

def region_perim(region):
    perimeter = 0
    for cell in region[1]:
        # up
        if cell[0] == 0 or (cell[0] - 1, cell[1]) not in region[1]:
            perimeter += 1
        # right
        if cell[1] == maxx or (cell[0], cell[1] + 1) not in region[1]:
            perimeter += 1
        # down
        if cell[0] == maxy or (cell[0] + 1, cell[1]) not in region[1]:
            perimeter += 1
        # left
        if cell[1] == 0 or (cell[0], cell[1] - 1) not in region[1]:
            perimeter += 1
    return perimeter

regions = []
maxy = len(rows) - 1
maxx = len(rows[0]) - 1
for y in range(maxy + 1):
    for x in range(maxx + 1):
        assert(len(rows[y]) == maxx + 1)
        if rows[y][x] == '.':
            continue
        flower = rows[y][x]
        q = [(y, x)]

        region = (flower, [])
        while len(q) > 0:
            cell = q.pop()
            if cell[0] < 0 or cell[0] > maxy:
                continue
            if cell[1] < 0 or cell[1] > maxx:
                continue
            if rows[cell[0]][cell[1]] != flower:
                continue
            region[1].append(cell)
            rows[cell[0]][cell[1]] = '.'
            q.append((cell[0] - 1, cell[1]))
            q.append((cell[0], cell[1] + 1))
            q.append((cell[0] + 1, cell[1]))
            q.append((cell[0], cell[1] - 1))
        regions.append(region)

total = 0
for r in regions:
    total += len(r[1]) * region_perim(r)
print(total)
