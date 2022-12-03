class Rucksack:
    def __init__(self, c1, c2):
        self.c1 = c1
        self.c2 = c2

def parse(fname, on_rucksack):
    def raw_to_dict(raw):
        d = {}
        for c in raw:
            if c not in d.keys():
                d[c] = 0
            d[c] += 1
        return d
    for l in open(fname, 'r'):
        l = l.strip()
        c1_raw = l[:len(l) // 2]
        c2_raw = l[len(l) // 2:]
        on_rucksack(Rucksack(raw_to_dict(c1_raw), raw_to_dict(c2_raw)))

def get_priority(it):
    if it.islower():
        return (ord(it) - ord('a')) + 1
    else:
        return (ord(it) - ord('A')) + 27
