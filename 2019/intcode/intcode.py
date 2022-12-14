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
OP_REL = 9
##################
OP_ARGC = {OP_ADD:3, OP_MUL:3, OP_INP:1, OP_OUT:1, OP_HLT:0, OP_JT:2, OP_JF:2, OP_LT:3, OP_EQ:3, OP_REL:1}
JUMPS = (OP_JT, OP_JF)
# day 2
PM_POSITION = 0
PM_IMMEDIATE = 1
# day 3
PM_RELATIVE = 2
PARAMS = (PM_POSITION, PM_IMMEDIATE, PM_RELATIVE)
#
def default_on_out(val):
    print('Intcode>', val)

class Computer:
    def __init__(self, on_in=None, on_out=default_on_out, id=None):
        self.data = []
        self.pc = 0
        self.halted = False
        self.inputq = []
        self.on_out = on_out
        self.on_in = self.default_on_in if on_in is None else on_in
        self.id = id
        self.stat_inc = 0
        self.stat_outc = 0
        self.relative_base = 0

    def paramread(self, n, mode):
        if mode == PM_POSITION:
            return self.read(n)
        elif mode == PM_IMMEDIATE:
            return n
        elif mode == PM_RELATIVE:
            return self.read(n + self.relative_base)
        assert False

    def step(self):
        types = set([type(d) for d in self.data])
        if len(types) > 1 or list(types)[0] != int:
            print('Bad data type')
            print(self.data)
            print(types, self.data.index(None))
            assert False
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
        if paramc > 0 and opcode != OP_INP:
            a = self.paramread(params[0], parammodes[0])
            b = self.paramread(params[1], parammodes[1]) if len(params) > 1 else None
            if paramc == 3:
                addr2 = params[2] if parammodes[2] == PM_POSITION else params[2] + self.relative_base
        if opcode == OP_ADD:
            self.write(addr2, a + b)
        elif opcode == OP_MUL:
            self.write(addr2, a * b)
        elif opcode == OP_INP:
            incoming = self.on_in()
            assert type(incoming) == int
            self.data[params[0] if parammodes[0] == PM_POSITION else params[0] + self.relative_base] = incoming
            self.stat_inc += 1
        elif opcode == OP_OUT:
            self.on_out(a)
            self.stat_outc += 1
        elif opcode == OP_JT:
            if a != 0:
                newpc = b
        elif opcode == OP_JF:
            if a == 0:
                newpc = b
        elif opcode == OP_LT:
            self.write(addr2, 1 if a < b else 0)
        elif opcode == OP_EQ:
            self.write(addr2, 1 if a == b else 0)
        elif opcode == OP_REL:
            self.relative_base += a
        else:
            self.halted = True
        if not self.halted:
            self.pc = newpc
    def write(self, addr:int, val:int):
        if addr >= len(self.data):
            self.data += [0] * (1 + (addr - len(self.data)))
        self.data[addr] = val
    def read(self, addr:int):
        assert addr >= 0
        if addr >= len(self.data):
            self.data += [0] * (1 + (addr - len(self.data)))
        return self.data[addr]
    def run(self):
        while not self.halted:
            if self.pc >= len(self.data):
                self.halted = True
                return
            self.step()
    def default_on_in(self):
        return self.inputq.pop(0)
def parse_file(fname):
    with open(fname, 'r') as f:
        return [int(n) for n in f.read().split(',')]