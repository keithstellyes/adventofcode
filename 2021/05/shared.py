import collections

class LineTrack:
    def __init__(self, diagonal=False):
        self.points = collections.defaultdict(lambda: 0)
        self.diagonal = diagonal
    def on_line(self, line):
        origin, dest = line
        xstart, ystart = origin
        xend, yend = dest
        if not(xstart == xend or ystart == yend) and not(self.diagonal):
            return
        while True:
            self.points[xstart, ystart] += 1
            if xstart == xend and ystart == yend:
                break
            if xstart < xend:
                xstart += 1
            if ystart < yend:
                ystart += 1
            if xstart > xend:
                xstart -= 1
            if ystart > yend:
                ystart -= 1

def parse(fname, on_line):
    for line in open(fname, 'r'):
        line = line.strip()
        if line == '':
            continue
        line = line.split(' -> ')
        origin = tuple([int(n) for n in line[0].split(',')])
        dest = tuple([int(n) for n in line[1].split(',')])
        on_line((origin, dest))