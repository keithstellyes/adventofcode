NEW_SAND = 0
SAND_SETTLED = 1
SAND_DOWN = 2
SAND_ABYSS = 3
SAND_CANNOT_SPAWN = 4
TERMINATING_STATES = (SAND_ABYSS, SAND_CANNOT_SPAWN)

class Cave:
    def __init__(self, has_floor=False):
        self.rocks = set()
        self.settled_sand = set()
        self.highest_y = float('-inf')
        self.active_sand = None
        self.sand_origin = (500, 0)
        self.has_floor = has_floor
    def add_rock(self, pt):
        self.rocks.add(pt)
        if pt[1] > self.highest_y:
            self.highest_y = pt[1]
    def pt_clear(self, pt):
        rocksand_check = pt not in self.rocks and pt not in self.settled_sand
        floor_check = not(self.has_floor) or pt[1] < self.floor()
        return rocksand_check and floor_check
    def floor(self):
        return self.highest_y + 2
    def step(self):
        if self.active_sand is None:
            self.active_sand = self.sand_origin
            return NEW_SAND
        straight_down = self.active_sand[0], self.active_sand[1] + 1
        if self.pt_clear(straight_down):
            self.active_sand = straight_down
            return SAND_DOWN if self.active_sand[1] <= self.highest_y or self.has_floor else SAND_ABYSS
        down_left = straight_down[0] - 1, straight_down[1]
        if self.pt_clear(down_left):
            self.active_sand = down_left
            return SAND_DOWN
        down_right = straight_down[0] + 1, straight_down[1]
        if self.pt_clear(down_right):
            self.active_sand = down_right
            return SAND_DOWN
        self.settled_sand.add(self.active_sand)
        if self.active_sand == self.sand_origin:
            return SAND_CANNOT_SPAWN
        self.active_sand = None
        return SAND_SETTLED
    def run(self):
        for n in range(1000):
            self.step()
        result = self.step()
        while result not in TERMINATING_STATES:
            result = self.step()
def parse(fname):
    cave = Cave()
    for line in open(fname, 'r'):
        line = line.strip()
        if line == '':
            continue
        path = [[int(pt[0]), int(pt[1])] for pt in [pt.split(',') for pt in line.split(' -> ')]]
        curpt = path[0]
        for n in range(1, len(path)):
            tgtpt = path[n]
            while curpt[0] != tgtpt[0] or curpt[1] != tgtpt[1]:
                cave.add_rock(tuple(curpt))
                if curpt[0] != tgtpt[0]:
                    if curpt[0] < tgtpt[0]:
                        curpt[0] += 1
                    else:
                        curpt[0] -= 1
                if curpt[1] != tgtpt[1]:
                    if curpt[1] < tgtpt[1]:
                        curpt[1] += 1
                    else:
                        curpt[1] -= 1
            cave.add_rock(tuple(curpt))
    return cave