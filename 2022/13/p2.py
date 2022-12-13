import sys, shared
import heapq

# wrapper for playing nice with Python's heap library
class Packet:
    def __init__(self, l):
        self.l = l
    def __lt__(self, rhs):
        result = cmp_list(self.l, rhs.l)
        return result == -1
    def __eq__(self, rhs):
        return self.l == rhs.l

# -1 left bigger 0 same 1 right bigger
def cmp_list(left, right):
    if len(left) == 0:
        if len(right) == 0:
            return 0
        return -1
    elif len(right) == 0:
        return 1
    for n in range(min(len(left), len(right))):
        lel = left[n]
        rel = right[n]
        if type(lel) != type(rel):
            # 1 is int, 1 is list
            if type(lel) == int:
                lel = [lel]
            elif type(rel) == int:
                rel = [rel]
            result = cmp_list(lel, rel)
            if result != 0:
                return result
        elif type(lel) == int:
            if lel != rel:
                return -1 if lel < rel else 1
        elif type(lel) == list:
            result = cmp_list(lel, rel)
            if result != 0:
                return result
        else:
            assert False
    if len(left) != len(right):
        return -1 if len(left) < len(right) else 1
    return 0

class PacketPairComparator:
    def __init__(self):
        self.packets = []
    def on_packetpair(self, packetpair):
        self.add_packet(Packet(packetpair[0]))
        self.add_packet(Packet(packetpair[1]))
        
    def add_packet(self, packet):
        heapq.heappush(self.packets, packet)
    def pop_packet(self):
        return heapq.heappop(self.packets)
ppc = PacketPairComparator()
shared.parse(sys.argv[1], ppc.on_packetpair)
p0, p1 = Packet([[2]]), Packet([[6]])
p0found, p1found = False, False
ppc.add_packet(p0)
ppc.add_packet(p1)
index = 1
code = 1
while len(ppc.packets) > 0:
    packet = ppc.pop_packet()
    if packet == p0:
        p0found = True
        code *= index
    elif packet == p1:
        p1found = True
        code *= index
    if p0found and p1found:
        print(code)
        break
    index += 1