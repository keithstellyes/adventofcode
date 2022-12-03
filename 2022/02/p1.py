import sys, shared

class Total:
    def __init__(self):
        self.total = 0
    def callback(self, r):
        self.total += r.score()

total = Total()
shared.parse(sys.argv[1], total.callback)
print(total.total)
