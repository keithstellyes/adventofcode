#!/usr/bin/env python3

import sys

def blink(stones):
    new_stones = []
    for stone in stones:
        if stone == 0:
            new_stones.append(1)
            continue
        stonestr = str(stone)
        if len(stonestr) % 2 == 0:
            leftstone = stonestr[:len(stonestr) // 2]
            rightstone = stonestr[len(stonestr) // 2:]
            new_stones.append(int(leftstone, 10))
            new_stones.append(int(rightstone, 10))
            continue
        new_stones.append(stone * 2024)
    return new_stones

def nblinks(stones, blinkc):
    for _ in range(blinkc):
        stones = blink(stones)
    return stones

if __name__ == '__main__':
    stones = [int(stone) for stone in open(sys.argv[1], 'r').readline().strip().split(' ')]
    blinkc = 25
    if len(sys.argv) > 2:
        blinkc = int(sys.argv[2])
    result = nblinks(stones, blinkc)
    print(len(result))
