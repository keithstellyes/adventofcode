import sys, shared
aim_dirs = {'down':1, 'up':-1}
class SubmarineTracker:
    def __init__(self):
        self.sub = shared.Submarine()
    def on_instr(self, move):
        if move.d in aim_dirs.keys():
            self.sub.aim += aim_dirs[move.d] * move.x
        elif move.d == 'forward':
            self.sub.horizontal += move.x
            self.sub.depth += self.sub.aim * move.x

s = SubmarineTracker()
shared.parse(sys.argv[1], s.on_instr)
print(s.sub.horizontal * s.sub.depth)
