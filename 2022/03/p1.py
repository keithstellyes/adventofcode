import sys, shared

class Counter:
    def __init__(self):
        self.total = 0
    def on_rucksack(self, r):
        for v in r.c1.keys():
            if v in r.c2.keys():
                self.total += shared.get_priority(v)

c = Counter()
shared.parse(sys.argv[1], c.on_rucksack)
print(c.total)
