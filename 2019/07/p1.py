import itertools
import sys
sys.path.append('..')
from intcode import intcode
data = intcode.parse_file(sys.argv[1])
class OutRecv:
    def __init__(self):
        self.val = None 
    def on_out(self, val):
        self.val = val

mx = float('-inf')
mx_comb = None
for comb in itertools.permutations((0, 1, 2, 3, 4)):
    last_out = [0]
    outrecv = OutRecv()
    for n in range(len(comb)):
        c = intcode.Computer(on_out=outrecv.on_out)
        c.inputq.append(comb[n])
        c.inputq.append(last_out[-1])
        c.data = data.copy()
        c.run()
        last_out.append(outrecv.val)
    if outrecv.val is not None and outrecv.val > mx:
        mx = outrecv.val
        mx_comb = comb
print(mx, mx_comb)