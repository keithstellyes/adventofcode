import sys, shared
import collections
sys.path.append('..')
from intcode import intcode

class ArcadeCabinet:
    def __init__(self):
        self.outctr = 0
        self.tiles = {}
        self.x = None
        self.y = None
    def on_out(self, val:int):
        if self.outctr % 3 == 0:
            self.x = val
        elif self.outctr % 3 == 1:
            self.y = val
        else:
            self.tiles[self.x, self.y] = val
        self.outctr += 1
cabinet = ArcadeCabinet()
c = intcode.Computer(on_out=cabinet.on_out)
c.data = intcode.parse_file(sys.argv[1])
c.run()
print(list(cabinet.tiles.values()).count(2))