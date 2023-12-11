#!/usr/bin/env python3
import sys

f = open(sys.argv[1], 'r')
lines = [l.strip() for l in f.readlines()]
f.close()
root = None

for y in range(len(lines)):
    index = lines[y].find('S')
    if index != -1:
        root = (index, y, 0)
        break
if root is None:
    print('Did not find root `S`!', file=sys.stderr)
    sys.exit(1)

explored = set()
mx = -1
q = [root]

while len(q) > 0:
    v = q.pop(0)
    #if v[0] < 0 or v[1] < 0 or v[0] >= len(lines[0]) or v[1] >= len(lines):
    #    continue
    node = lines[v[1]][v[0]]
    print(v, node)
    if (v[0], v[1]) in explored:
        continue
    explored.add((v[0], v[1]))
    if node == '.':
        # non starter
        continue
    if v[2] > mx:
        mx = v[2]
    # north
    if node in '|LJ' and v[1] > 0 and lines[v[1] - 1][v[0]] in '|7F':
        q.append((v[0], v[1] - 1, v[2] + 1))
    # south
    if node in '|7F' and v[1] < len(lines) - 1 and lines[v[1] + 1][v[0]] in '|LJ':
        q.append((v[0], v[1] + 1, v[2] + 1))
    # east
    if node in '-LF' and v[0] < len(lines[0]) - 1 and lines[v[1]][v[0] + 1] in '-J7':
        q.append((v[0] + 1, v[1], v[2] + 1))
    # west
    if node in '-J7' and v[0] > 0 and lines[v[1]][v[0] - 1] in '-LF':
        q.append((v[0] - 1, v[1], v[2] + 1))
    if node == 'S':
        # try going north
        if v[1] > 0 and lines[v[1] - 1][v[0]] in '|7F':
            q.append((v[0], v[1] - 1, 1))
        # try goign south
        if v[1] < len(lines) - 1 and lines[v[1] + 1][v[0]] in '|LJ':
            q.append((v[0], v[1] + 1, 1))
        # try going east
        if v[0] < len(lines[0]) - 1 and lines[v[1]][v[0] + 1] in '-J7':
            q.append((v[0] + 1, v[1], 1))
        if v[0] > 0 and lines[v[1]][v[0] - 1] in '-LF':
            q.append((v[0] - 1, v[1], 1))
    assert node in '|-LJ7F.S'
print(mx)
# too low: 6677
# too low: 6678
