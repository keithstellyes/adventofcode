import sys, shared

class StacksState:
    def __init__(self):
        self.stacks = None
    def on_stacks(self, stacks):
        self.stacks = stacks
        print(self.stacks)
    def on_instr(self, instr):
        origin_stack_og = self.stacks[instr.origin - 1]
        oglen = len(origin_stack_og)
        nc = instr.num_crates
        crates = origin_stack_og[oglen - nc:]
        self.stacks[instr.origin - 1] = origin_stack_og[:oglen - nc]
        self.stacks[instr.dest - 1] += crates

s = StacksState()
shared.parse(sys.argv[1], s.on_stacks, s.on_instr)
shared.print_stacks(s.stacks)
print(''.join(s[-1] for s in s.stacks))
