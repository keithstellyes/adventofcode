#!/usr/bin/env python3

import re, sys

memory = open(sys.argv[1], 'r').read()

total = 0
while len(memory) > len('mul(,)'):
    match = re.search(r'mul\(\d+,\d+\)', memory)
    if match is None:
        break
    n1, n2 = re.findall(r'\d+', match.group())
    total += int(n1) * int(n2)
    if match.end() >= len(memory):
        break
    memory = memory[match.end():]

print(total)

