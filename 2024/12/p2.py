#!/usr/bin/env python3

import sys

rows = [list(l.strip()) for l in open(sys.argv[1], 'r').readlines()]

def delete_cell(segs, cell):
    index = segs.index(cell)
    return segs[0:index] + segs[index+1:]

def region_perim(region):
    sidesegs = []
    for cell in region[1]:
        # up
        if cell[0] == 0 or (cell[0] - 1, cell[1]) not in region[1]:
            sidesegs.append((cell, 'u'))
        # right
        if cell[1] == maxx or (cell[0], cell[1] + 1) not in region[1]:
            sidesegs.append((cell, 'r'))
        # down
        if cell[0] == maxy or (cell[0] + 1, cell[1]) not in region[1]:
            sidesegs.append((cell, 'd'))
        # left
        if cell[1] == 0 or (cell[0], cell[1] - 1) not in region[1]:
            sidesegs.append((cell, 'l'))
    perimeter = len(sidesegs)
    sides = []
    while len(sidesegs) > 0:
        seg = sidesegs.pop()
        sidelen = 1
        if seg[1] == 'u':
            # segment is above the cell, all neighbor segments
            # should also be above cells
            ptrright = (seg[0][0], seg[0][1] + 1)
            ptrleft = (seg[0][0], seg[0][1] - 1)
            while (ptrright, 'u') in sidesegs:
                sidesegs = delete_cell(sidesegs, (ptrright, 'u'))
                sidelen += 1
                ptrright = (ptrright[0], ptrright[1] + 1)
            while (ptrleft, 'u') in sidesegs:
                sidesegs = delete_cell(sidesegs, (ptrleft, 'u'))
                sidelen += 1
                ptrleft = (ptrleft[0], ptrleft[1] - 1)
        elif seg[1] == 'd':
            # segment is below the cell, all neighbor segments
            # should also be below cells
            ptrright = (seg[0][0], seg[0][1] + 1)
            ptrleft = (seg[0][0], seg[0][1] - 1)
            while (ptrright, 'd') in sidesegs:
                sidesegs = delete_cell(sidesegs, (ptrright, 'd'))
                sidelen += 1
                ptrright = (ptrright[0], ptrright[1] + 1)
            while (ptrleft, 'd') in sidesegs:
                sidesegs = delete_cell(sidesegs, (ptrleft, 'd'))
                sidelen += 1
                ptrleft = (ptrleft[0], ptrleft[1] - 1)
        elif seg[1] == 'l':
            # segment is left of the cell, all neighbor segments
            # should also be left of cells
            ptrup = (seg[0][0] - 1, seg[0][1])
            ptrdown = (seg[0][0] + 1, seg[0][1])
            while (ptrup, 'l') in sidesegs:
                sidesegs = delete_cell(sidesegs, (ptrup, 'l'))
                sidelen += 1
                ptrup = (ptrup[0] - 1, ptrup[1])
            while (ptrdown, 'l') in sidesegs:
                sidesegs = delete_cell(sidesegs, (ptrdown, 'l'))
                sidelen += 1
                ptrdown = (ptrdown[0] + 1, ptrdown[1])
        elif seg[1] == 'r':
            # segment is right of the cell, all neighbor segments
            # should also be right of cells
            ptrup = (seg[0][0] - 1, seg[0][1])
            ptrdown = (seg[0][0] + 1, seg[0][1])
            while (ptrup, 'r') in sidesegs:
                sidesegs = delete_cell(sidesegs, (ptrup, 'r'))
                sidelen += 1
                ptrup = (ptrup[0] - 1, ptrup[1])
            while (ptrdown, 'r') in sidesegs:
                sidesegs = delete_cell(sidesegs, (ptrdown, 'r'))
                sidelen += 1
                ptrdown = (ptrdown[0] + 1, ptrdown[1])
        else:
            assert(False)
        sides.append(sidelen)
    if sum(sides) != perimeter:
        raise AssertionError("The sum of side lengths should be eq to perimeter")
    return len(sides)
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
    area = len(r[1])
    sides = region_perim(r)
    total += area * sides
print(total)
