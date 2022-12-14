import sys, shared, curses, collections, time
sys.path.append('..')
from intcode import intcode

TILES = [' ', '█', '#', '=', 'o']

class ArcadeCabinet:
    def __init__(self, pc=None, scr=None):
        self.outctr = 0
        self.tiles = {}
        self.x = None
        self.y = None
        self.score = None
        self.inp = 0
        self.scr = scr
        self.ic = 0
        self.ball_y = float('inf')
        self.pc = pc
        self.max_x = -1
    def on_out(self, val:int):
        if self.outctr % 3 == 0:
            self.x = val
            if self.x > self.max_x:
                self.max_x = self.x
        elif self.outctr % 3 == 1:
            self.y = val
        else:
            if self.x == -1 and self.y == 0:
                self.score = val
                if self.scr is not None:
                    self.scr.addstr(0, self.max_x + 1, 'SCORE:' + str(self.score))
            else:
                self.tiles[self.x, self.y] = val
                if self.scr is not None:
                    self.scr.addstr(self.y, self.x, TILES[val])
        self.outctr += 1
    # pretty difficult and tedious to play the game the "right" way, 
    # so we hack the map to insert walls. This is done dynamically,
    # so should be generalizable to others' inputs, so I don't consider
    # it cheating the challenge, and in the spirit of programming 
    # challenges, as this is additonal programming complexity to
    # investigate code dynamically,then modify to compute the target
    # result.
    def insert_floor(self, data):
        data = data.copy()
        max_x = max([c[0] for c in self.tiles.keys()])
        max_y = max([c[1] for c in self.tiles.keys()])
        segment = []
        for x in range(max_x):
            segment.append(self.tiles[x, max_y])
        has_found_ball = False
        may_find_ball = False
        for n in range(len(self.pc.data) - len(segment)):
            if may_find_ball:
                if 4 in self.pc.data[n:n+len(segment)]:
                    has_found_ball = True
            if data[n:n+len(segment)] == segment:
                if not has_found_ball:
                    may_find_ball = True
                    continue
                for i in range(len(segment)):
                    data[i+n] = 1
        return data

    def on_in(self):
        return 0

def data_with_floor_patch(data):
    cabinet = ArcadeCabinet()
    pc = intcode.Computer(on_in=cabinet.on_in, on_out=cabinet.on_out)
    cabinet.pc = pc
    pc.data = data.copy()
    pc.write(0, 2)
    while cabinet.score is None:
        pc.step()
    return cabinet.insert_floor(data)

cabinet = ArcadeCabinet()
c = intcode.Computer(on_in=cabinet.on_in, on_out=cabinet.on_out)
c.out_debug = True
cabinet.pc = c
c.data = data_with_floor_patch(intcode.parse_file(sys.argv[1]))
c.write(0, 2)

def main(stdscr):
    stdscr.clear()
    stdscr.nodelay(True)
    stdscr.keypad(True)
    cabinet.scr = stdscr
    while cabinet.score is None:
        c.step()
    last = time.time()
    while not c.halted:
        c.step()
        stdscr.refresh()
    stdscr.refresh()
curses.wrapper(main)
print(cabinet.score)