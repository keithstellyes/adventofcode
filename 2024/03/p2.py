#!/usr/bin/env python3

import re, sys

memory = open(sys.argv[1], 'r').read()

total = 0
mul_enabled = True
while len(memory) > len('mul(,)'):
    match = re.search(r'(mul\(\d+,\d+\)|do\(\)|don\'t\(\))', memory)
    if match is None:
        break
    command = match.group()
    if command == 'do()':
        mul_enabled = True
    elif command == "don't()":
        mul_enabled = False
    elif command.startswith('mul') and mul_enabled:
        n1, n2 = re.findall(r'\d+', match.group())
        total += int(n1) * int(n2)
    memory = memory[match.end():]

print(total)

