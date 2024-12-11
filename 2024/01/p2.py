#!/usr/bin/env python3

import heapq, sys

lines = None

with open(sys.argv[1], 'r') as f:
    lines = f.readlines()

lns = []
rns = {}
for l in lines:
   lnstr, rnstr = l.split('   ')
   lns.append(int(lnstr))
   rn = int(rnstr)
   rns[rn] = rns.get(rn, 0) + 1

print(sum([rns.get(ln, 0) * ln for ln in lns]))
