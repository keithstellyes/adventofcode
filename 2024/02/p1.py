#!/usr/bin/env python3

import sys

def is_safe_report(report):
    steps = [step for step in zip(report, report[1:])]
    deltas = [post - pre for pre, post in steps]
    increases = any([pre < post for pre, post in steps])
    decreases = any([pre > post for pre, post in steps])
    if increases and decreases:
        return False
    return not(any([abs(d) > 3 or d == 0 for d in deltas]))

if __name__ == '__main__':
    reports = []
    total = 0
    with open(sys.argv[1], 'r') as f:
        for line in f.readlines():
            reports.append([int(level) for level in line.split(' ')])
    print(sum([1 if is_safe_report(r) else 0 for r in reports]))
