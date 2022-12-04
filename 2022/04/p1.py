# given a list of pairs of ranges, how many pairs meet the following condition:
# a range is contained entirely in another
# (for this problem, assignments ARE ranges)

import sys, shared

class ContainCounter:
    def __init__(self):
        self.total = 0
    def on_assignment_pair(self, ap):
        if ap[0] in ap[1] or ap[1] in ap[0]:
            self.total += 1

cc = ContainCounter()
shared.parse(sys.argv[1], cc.on_assignment_pair)
print(cc.total)
