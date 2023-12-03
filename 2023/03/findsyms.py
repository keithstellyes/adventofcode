#!/usr/bin/env python3
# quick script to find all used symbols
# for manual inspection
import sys, string

found = set()
for fn in sys.argv[1:]:
    with open(fn) as f:
        for line in f:
            for c in [c for c in line if c not in string.digits + '.' + '\n']:
                found.add(c)

print(''.join([c for c in found]))
