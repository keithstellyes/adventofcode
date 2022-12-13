import sys, shared

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
        self.total = 0
        self.packet_index = 1
        self.in_order = []
        self.out_of_order = []
    def on_packetpair(self, packetpair):
        left, right = packetpair
        result = cmp_list(left, right)
        if result == -1:
            self.in_order.append(self.packet_index)
        elif result == 1:
            self.out_of_order.append(self.packet_index)
        else:
            assert False
        self.packet_index += 1

ppc = PacketPairComparator()
shared.parse(sys.argv[1], ppc.on_packetpair)
print(ppc.in_order, sum(ppc.in_order))