#!/usr/bin/env python3
def historystep(l):
    if set(l) == set([0]):
        return l
    result = []
    for i in range(0, len(l) - 1):
        result.append(l[i + 1] - l[i])
    return result

def extrapolate(l):
    lists = [l]
    while set(lists[-1]) != set([0]):
        lists.append(historystep(lists[-1]))
    return sum([ex[-1] for ex in lists])

def parsefn(fn):
    lines = []
    for line in open(fn):
        lines.append([int(n) for n in line.split(' ')])
    return lines
