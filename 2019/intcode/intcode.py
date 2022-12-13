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
### Day 2 ops! ###
OP_INP = 3
OP_OUT = 4
OP_JT = 5
OP_JF = 6
OP_LT = 7
OP_EQ = 8
##################
OP_ARGC = {OP_ADD:3, OP_MUL:3, OP_INP:1, OP_OUT:1, OP_HLT:0, OP_JT:2, OP_JF:2, OP_LT:3, OP_EQ:3}
JUMPS = (OP_JT, OP_JF)
# day 2
PM_POSITION = 0
PM_IMMEDIATE = 1
PARAMS = (PM_POSITION, PM_IMMEDIATE)
#
class Computer:
    def __init__(self):
        self.data = []
        self.pc = 0
        self.halted = False
        self.inputq = []

    def step(self):
        op = self.data[self.pc]
        opcode = op % 100
        params = op // 100
        parammodes = []
        parammodes.append(params % 10)
        params //= 10
        parammodes.append(params % 10)
        params //= 10
        parammodes.append(params % 10)
        for pm in parammodes:
            assert pm in PARAMS
        assert parammodes[2] != PM_IMMEDIATE
        params = []
        paramc = OP_ARGC[opcode]
        for n in range(paramc):
            params.append(self.data[self.pc + n + 1])
        newpc = self.pc + 1 + paramc
        if paramc == 3 or opcode in JUMPS:
            a = self.data[params[0]] if parammodes[0] == PM_POSITION else params[0]
            b = self.data[params[1]] if parammodes[1] == PM_POSITION else params[1]
        if opcode == OP_ADD:
            self.write(params[2],a + b)
        elif opcode == OP_MUL:
            self.write(params[2], a * b)
        elif opcode == OP_INP:
            self.data[params[0]] = self.inputq.pop(0)
        elif opcode == OP_OUT:
            print('Intcode>', self.data[params[0]])
        elif opcode == OP_JT:
            if a != 0:
                newpc = b
        elif opcode == OP_JF:
            if a == 0:
                newpc = b
        elif opcode == OP_LT:
            self.write(params[2], 1 if a < b else 0)
        elif opcode == OP_EQ:
            self.write(params[2], 1 if a == b else 0)
        else:
            self.halted = True
        if not self.halted:
            self.pc = newpc
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