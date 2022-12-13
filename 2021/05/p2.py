import sys, shared

lt = shared.LineTrack(True)
shared.parse(sys.argv[1], lt.on_line)
print(sum([1 if v >= 2 else 0 for v in lt.points.values()]))