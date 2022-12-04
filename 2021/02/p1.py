import sys, shared
dirs = {'forward':(1,0), 'down':(0,1), 'up':(0,-1)}
class SubmarineTracker:
    def __init__(self):
        self.sub = shared.Submarine()
    def on_instr(self, move):
        d = dirs[move.d]
        horiz = d[0] * move.x
        depth = d[1] * move.x
        self.sub.horizontal += horiz
        self.sub.depth += depth

s = SubmarineTracker()
shared.parse(sys.argv[1], s.on_instr)
print(s.sub.horizontal * s.sub.depth)
