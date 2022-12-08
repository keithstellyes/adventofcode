import sys, shared
class Total:
    def __init__(self):
        self.total = 0
    def on_fuelreq(self, f):
        self.total += f // 3 - 2
t = Total()
shared.parse(sys.argv[1], t.on_fuelreq)
print(t.total)