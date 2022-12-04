#!/usr/bin/env python3
import os, os.path, sys

def open_f(d, fname):
    return open(d + '/' + fname, 'w')

year = int(input('year:'))
day = int(input('day:'))

assert year >= 2015 and year <= 2022
assert day >= 1 and day <= 25

new_dir = './{y}/{d:02d}/'.format(y=year, d=day)
if os.path.exists(new_dir):
    print('{} already exists!'.format(new_dir))
    sys.exit(1)

os.makedirs(new_dir)

shared_file = open_f(new_dir, 'shared.py')
shared_file.write('def parse(fname, callback):\n')
shared_file.write('    for line in open(fname, \'r\'):\n')
shared_file.write('        line = line.strip()\n')
shared_file.write('        if line == \'\':\n')
shared_file.write('            continue')
shared_file.close()
for p in 'p1.py', 'p2.py':
    p_file = open_f(new_dir, p)
    p_file.write('import sys, shared\n')
    p_file.write('shared.parse(sys.argv[1])')
    p_file.close()
