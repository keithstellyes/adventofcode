class Instr:
    def __init__(self, num_crates, origin, dest):
        self.num_crates = int(num_crates)
        self.origin = int(origin)
        self.dest = int(dest)

# 0 is bottom of stack, -1 is top (len(stack) - 1)
def parse(fname, on_stacks, on_instr):
    CHARS_PER_STACK = 4
    with open(fname, 'r') as f:
        stack_lines = []
        while True:
            line = f.readline()
            if '1' in line:
                # end of stacks
                break
            stack_lines.append(line)
        number_stacks = len(stack_lines[0]) // CHARS_PER_STACK 
        stacks = [[] for n in range(number_stacks)]
        for line in stack_lines:
            for n in range(number_stacks):
                box = line[n * CHARS_PER_STACK + 1]
                if box != ' ':
                    stacks[n].insert(0, box)
        on_stacks(stacks)
        # consume empty line separating stacks from instrs
        assert f.readline().strip() == ''
        for instr_line in f:
            instr_line = instr_line.strip()
            _, num_crates, __, origin, ___, dest = instr_line.split(' ')
            on_instr(Instr(num_crates, origin, dest))

def print_stacks(stacks):
    tallest_stack = max([len(s) for s in stacks])
    for n in range(tallest_stack - 1, -1, -1):
        for stack in stacks:
            if n < len(stack):
                print('[{}]'.format(stack[n]), end=' ')
            else:
                print('   ', end=' ')
        print()
