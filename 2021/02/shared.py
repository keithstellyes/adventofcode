class Submarine:
    def __init__(self):
        self.horizontal = 0
        self.depth = 0
        self.aim = 0

class Instr:
    def __init__(self, d, x):
        self.d = d
        self.x = x
def parse(fname, on_instr):
    for line in open(fname, 'r'):
        if line == '':
            continue
        line = line.strip()
        direct, dist = line.split(' ')
        dist = int(dist)
        on_instr(Instr(direct, dist))
