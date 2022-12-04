import sys, shared
class DepthTracker:
    def __init__(self):
        self.last_depth = float('inf')
        self.total = 0
    def on_depth(self, depth):
        if depth > self.last_depth:
            self.total += 1
        self.last_depth = depth

dd = DepthTracker()
shared.parse(sys.argv[1], dd.on_depth)
print(dd.total)
