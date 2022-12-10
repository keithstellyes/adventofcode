import sys, shared

class SignalStrengthTracker:
    def __init__(self):
        self.total = 0
    def on_cycle(self, cpu):
        if (cpu.cyclectr - 20) % 40 == 0:
            self.total += cpu.signalstrength()

t = SignalStrengthTracker()
cpu = shared.CrtCpu(t.on_cycle)
shared.parse(sys.argv[1], cpu.on_instr)
cpu.cycle(1)

print('Sum:', t.total)