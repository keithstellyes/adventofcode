import collections

AWAITING_PAINT = 'AWAITING_PAIR'
AWAITING_TURN = 'AWAITING_TURN'
UP = (0, 1)
RIGHT = (1, 0)
DOWN = (0, -1)
LEFT = (-1, 0)
CLOCKWISE_DIRS = (UP, RIGHT, DOWN, LEFT)
class Robot:
    def __init__(self):
        self.coords = (0, 0)
        self.painted = collections.defaultdict(lambda: 0)
        self.direction = 0
        self.state = AWAITING_PAINT
    def on_in(self):
        return self.painted[self.coords]
    def on_out(self, val:int):
        if self.state == AWAITING_PAINT:
            self.painted[self.coords] = val
            self.state = AWAITING_TURN
        else:
            if val == 0:
                self.direction = (self.direction - 1) % 4
            else:
                self.direction = (self.direction + 1) % 4
            d = CLOCKWISE_DIRS[self.direction]
            self.coords = self.coords[0] + d[0], self.coords[1] + d[1]
            self.state = AWAITING_PAINT