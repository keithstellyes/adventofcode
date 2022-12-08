'''
Many problems in 2019 use this computer or build upon it. The days are
2, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25

https://esolangs.org/wiki/Intcode
'''

import typing

### Day 1 ops! ###
OP_ADD = 1
OP_MUL = 2
OP_HLT = 99
##################
OP_ARGC = {OP_ADD:3, OP_MUL:3, OP_HLT:0}

class Computer:
    def __init__(self):
        self.data = []
        self.pc = 0
        self.halted = False

    def step(self):
        op = self.data[self.pc]
        args = []
        argc = OP_ARGC[op]
        for n in range(argc):
            args.append(self.data[self.pc + n + 1])
        if op == OP_ADD:
            self.write(args[2], self.data[args[0]] + self.data[args[1]])
        elif op == OP_MUL:
            self.write(args[2], self.data[args[0]] * self.data[args[1]])
        else:
            self.halted = True
        if not self.halted:
            self.pc += 1 + argc
    def write(self, addr:int, val:int):
        if addr >= len(self.data):
            print('OUT OF RANGE?!')
            return
        self.data[addr] = val
    def run(self):
        while not self.halted:
            if self.pc >= len(self.data):
                self.halted = True
                return
            self.step()
def parse_file(fname):
    with open(fname, 'r') as f:
        return [int(n) for n in f.read().split(',')]