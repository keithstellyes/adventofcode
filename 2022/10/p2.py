import sys, shared

class Crt:
    def __init__(self):
        self.ctr = 0
    def on_cycle(self, cpu):
        col = self.ctr % 40
        sprite_begin = cpu.x - 1
        sprite_end = cpu.x + 1
        if col >= sprite_begin and col <= sprite_end:
            print('#',end='')
        else:
            print('.',end='')
        self.ctr += 1
        if self.ctr % 40 == 0:
            print()

crt = Crt()
cpu = shared.CrtCpu(crt.on_cycle)
shared.parse(sys.argv[1], cpu.on_instr)
