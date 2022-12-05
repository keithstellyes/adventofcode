import sys, shared

class StacksState:
    def __init__(self):
        self.stacks = None
    def on_stacks(self, stacks):
        self.stacks = stacks
        print(self.stacks)
    def on_instr(self, instr):
        for _ in range(instr.num_crates):
            crate = self.stacks[instr.origin - 1].pop(0)
            self.stacks[instr.dest - 1].insert(0, crate)

s = StacksState()
shared.parse(sys.argv[1], s.on_stacks, s.on_instr)
shared.print_stacks(s.stacks)
