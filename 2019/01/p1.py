import sys, shared
class Total:
    def __init__(self):
        self.total = 0
    def on_fuelreq(self, f):
        self.total += shared.fuel_required(f)
t = Total()
shared.parse(sys.argv[1], t.on_fuelreq)
print(t.total)