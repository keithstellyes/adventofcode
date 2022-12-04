# given a list of pairs of ranges, how many pairs meet the following condition:
# a range OVERLAPS with another

import sys, shared

class ContainCounter:
    def __init__(self):
        self.total = 0
    def on_assignment_pair(self, ap):
        # sort the ranges by beginning to simplfiy overlappign logic,
        # this is especially powerful if we want to check MORE than jsut a pair
        # it's a common interview problem to look at many ranges,
        # but for just a pair we can get away WITHOUT sorting
        ap0 = ap[0] if ap[0].begin <= ap[1].begin else ap[1]
        ap1 = ap[1] if ap0 == ap[0] else ap[0]
        # assert because further logic depends on this condition holding true
        # this should theoretically be redundant, however
        assert ap0.begin <= ap1.begin
        if ap1.begin <= ap0.end:
            self.total += 1

cc = ContainCounter()
shared.parse(sys.argv[1], cc.on_assignment_pair)
print(cc.total)
