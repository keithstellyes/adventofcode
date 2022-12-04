import sys, shared

class Submarine:
    def __init__(self):
        self.coord = (0, 0)
    def on_move(self, move):
        self.coord = move.apply(self.coord)

s = Submarine()
shared.parse(sys.argv[1], s.on_move)
print(s.coord[0] * s.coord[1])
