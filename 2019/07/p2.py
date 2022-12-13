import itertools
import sys
sys.path.append('..')
from intcode import intcode
data = intcode.parse_file(sys.argv[1])
class Wire:
    def __init__(self):
        self.q = []
    def connect(self, recvpc, sendpc):
        self.rpc = recvpc
        self.spc = sendpc
        recvpc.on_in = self.recv
        sendpc.on_out = self.send
    def send(self, val):
        self.q.append(val)
    def recv(self):
        v = self.q.pop(0)
        return v
    
mx = float('-inf')
mx_comb = None
for comb in itertools.permutations((5, 6, 7, 8, 9)):
    last_out = [0]
    computers = [intcode.Computer() for _ in comb]
    wires = [Wire() for _ in comb]
    for n in range(5):
        pc = computers[n]
        pc.data = data.copy()
        pc.id = n
    for n in range(len(comb)):
        # we want so that wires[4].q[-1] is the final thruster level
        wires[n].connect(computers[(n + 1) % 5], computers[n % 5])
        wires[n].send(comb[n])
    wires[4].send(0)
    while True:
        haltc = [pc.halted for pc in computers].count(True)
        if haltc == 5:
            break
        for pc in computers:
            if pc.halted:
                continue
            initial_outc = pc.stat_outc
            while not pc.halted and pc.stat_outc == initial_outc:
                pc.step()
    if wires[-1].q[-1] > mx:
        mx = wires[-1].q[-1]
        mx_comb = comb
print(mx, mx_comb)