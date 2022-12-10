import sys, shared

class CrtCpu:
    def __init__(self):
        self.x = 1
        self.cyclectr = 0
        self.signalstrengths = []
    def cycle(self, cnt):
        for _ in range(cnt):
            self.cyclectr += 1
            self.signalstrengths.append(self.signalstrength())
    def signalstrength(self):
        return self.x * self.cyclectr
    def on_instr(self, instr):
        if instr.op == 'noop':
            self.cycle(1)
        elif instr.op == 'addx':
            self.cycle(2)
            self.x += instr.arg

cpu = CrtCpu()
shared.parse(sys.argv[1], cpu.on_instr)
cpu.cycle(1)
print(', '.join([str(s) for s in cpu.signalstrengths]))

total = 0
for n in range(6):
    idx = (n*40) + 19
    s = cpu.signalstrengths[idx]
    print('{:03d}|'.format(idx + 1), s)
    total += s

print('Sum:', total)