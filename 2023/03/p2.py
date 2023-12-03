#!/usr/bin/env python3
import re, sys

symbols = '@*/=-$&+#%'
rows = []
with open(sys.argv[1], 'r') as f:
    rows = [l.strip() for l in f.readlines()]

gear_model_numbers = {}
def add_gear(coord, mn: int):
    if coord not in gear_model_numbers.keys():
        gear_model_numbers[coord] = []
    if mn in gear_model_numbers[coord]:
        return
    gear_model_numbers[coord].append(mn)
nummatch = re.compile('[0-9]+')
x = 0
y = 0
total = 0
while y < len(rows):
    row = rows[y]
    candidates = nummatch.finditer(row)
    for candidate in candidates:
        # clean way of handling the edge case of being on the edges
        # (pun not intended)
        xmin = max(0, candidate.start() - 1)
        # candidate.end() is the first index AFTER the string
        assert candidate.end() <= len(row)
        xmax = min(len(row) - 1, candidate.end())
        cstr = row[candidate.start():candidate.end()]
        mn = int(cstr)
        if y > 0:
            x = xmin
            while x <= xmax:
                if rows[y - 1][x] == '*':
                    add_gear((x, y - 1), mn)
                x += 1
        if row[xmin] == '*':
            add_gear((xmin, y), mn)
        if row[xmax] == '*':
            add_gear((xmax, y), mn)
        if y < len(rows) - 1:
            x = xmin
            while x <= xmax:
                if rows[y + 1][x] == '*':
                    add_gear((x, y + 1), mn)
                x += 1
    y = y + 1
for gear, mns in gear_model_numbers.items():
    if len(mns) == 2:
        total += mns[0] * mns[1]
print(total)
