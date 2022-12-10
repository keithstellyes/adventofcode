import typing

class Instr(typing.NamedTuple):
    op: str
    arg: typing.Optional[int]

def parse(fname, on_instr):
    for line in open(fname, 'r'):
        line = line.strip()
        if line == '':
            continue
        line = line.split(' ')
        op = line[0]
        arg = int(line[1]) if len(line) > 1 else None
        on_instr(Instr(op, arg))

class CrtCpu:
    def __init__(self, on_cycle):
        self.x = 1
        self.cyclectr = 0
        self.on_cycle = on_cycle
    def cycle(self, cnt):
        for _ in range(cnt):
            self.cyclectr += 1
            self.on_cycle(self)
    def signalstrength(self):
        return self.x * self.cyclectr
    def on_instr(self, instr):
        if instr.op == 'noop':
            self.cycle(1)
        elif instr.op == 'addx':
            self.cycle(2)
            self.x += instr.arg