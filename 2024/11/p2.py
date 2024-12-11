#!/usr/bin/env python3

# too low: 220295289181291
import sys
from collections import Counter

def blink(stone):
    if type(stone) != int:
        raise TypeError('should be an int')
    new_stones = []
    if stone == 0:
        return Counter([1])
    stonestr = str(stone)
    if len(stonestr) % 2 == 0:
        leftstone = stonestr[:len(stonestr) // 2]
        rightstone = stonestr[len(stonestr) // 2:]
        return Counter([int(leftstone, 10), int(rightstone, 10)])
    return Counter([stone * 2024])

nbcache = {}
def nblinks(stones, blinkc):
    if blinkc < 0:
        raise ValueError('blinkc should be at least 0')
    if blinkc == 0:
        return stones
    if blinkc == 1:
        c = Counter()
        for stone, stonec in stones.items():
            nbcache[(stone, 1)] = blink(stone)
            for _ in range(stonec):
                c.update(nbcache[(stone, 1)])
        return c
    result = Counter()
    for stone, stonec in stones.items():
        key = (stone, blinkc)
        if key not in nbcache:
            nbcache[key] = nblinks(blink(stone), blinkc - 1)
        for _ in range(stonec):
            result.update(nbcache[key])
    return result

if __name__ == '__main__':
    stones = [int(stone) for stone in open(sys.argv[1], 'r').readline().strip().split(' ')]
    blinkc = 75
    if len(sys.argv) > 2:
        blinkc = int(sys.argv[2])
    cache = {}
    result = nblinks(Counter(stones), blinkc)
    #print(result)
    print(result.total())
