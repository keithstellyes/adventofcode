#!/usr/bin/env python3

import sys

import p1
reports = []
with open(sys.argv[1], 'r') as f:
    for line in f.readlines():
        reports.append([int(level) for level in line.split(' ')])

total = 0
for r in reports:
    if p1.is_safe_report(r):
        total += 1
    else:
        for n in range(len(r)):
            if p1.is_safe_report(r[0:n] + r[n+1:len(r)]):
                total += 1
                break
print(total)
