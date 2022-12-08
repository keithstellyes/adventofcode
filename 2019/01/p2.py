import sys, shared

import sys, shared
class Total:
    def __init__(self):
        self.total = 0
    def on_fuelreq(self, f):
        req = shared.fuel_required(f)
        if req <= 0:
            return
        self.total += req
        self.on_fuelreq(req)
t = Total()
shared.parse(sys.argv[1], t.on_fuelreq)
print(t.total)