import sys, shared

class NumFinder:
    def __init__(self, tgt=2020):
        self.nums = {}
        self.tgt = 2020
        self.results = None
    def on_number(self, n):
        if n in self.nums.keys():
            self.results = (self.nums[n], n)
        self.nums[self.tgt - n] = n

nf = NumFinder()
shared.parse(sys.argv[1], nf.on_number)
r0, r1 = nf.results
print('{} * {} = {}'.format(r0, r1, r0*r1))