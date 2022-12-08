import sys, shared

class NumFinder:
    def __init__(self, tgt=2020):
        self.nums = set()
        self.awaiting_final = {}
        self.tgt = 2020
        self.results = None
    def on_number(self, n):
        if n in self.awaiting_final.keys():
            self.results = self.awaiting_final[n] + [n]
        if n in self.nums:
            return
        for other in self.nums:
            self.awaiting_final[2020 - (n + other)] = [n, other]
        self.nums.add(n)

nf = NumFinder()
shared.parse(sys.argv[1], nf.on_number)
r0, r1, r2 = nf.results
print('{} * {} * {} = {}'.format(r0, r1, r2, r0*r1*r2))