import collections, sys, shared

class LineTrack:
    def __init__(self):
        self.points = collections.defaultdict(lambda: 0)
    def on_line(self, line):
        origin, dest = line
        xstart, ystart = origin
        xend, yend = dest
        if not(xstart == xend or ystart == yend):
            return
        if xend < xstart or yend < ystart:
            tmp = origin
            origin = dest
            dest = tmp
            xstart, ystart = origin
            xend, yend = dest

        while True:
            self.points[xstart, ystart] += 1
            if xstart == xend and ystart == yend:
                break
            if xstart < xend:
                xstart += 1
            if ystart < yend:
                ystart += 1

lt = LineTrack()
shared.parse(sys.argv[1], lt.on_line)
print(sum([1 if v >= 2 else 0 for v in lt.points.values()]))