# we rely heavily on set union and intersection here, if we wanted to get our
# hands dirty, we could use Bloom Filter or a Skip List
# https://stackoverflow.com/questions/39154817/data-structures-for-fast-intersection-operationsimport sys, shared
ELF_GROUP_SIZE = 3

class BadgeFinder:
    def __init__(self, group_size=ELF_GROUP_SIZE):
        self.total = 0
        self.possible_badges = set()
        self.elf_ctr = 0
        self.group_size = group_size
    def on_rucksack(self, r):
        # first elf
        if self.elf_ctr == 0:
            self.possible_badges = r.allitems()
        # after first elf
        elif self.elf_ctr <= self.group_size - 1:
            self.possible_badges = set.intersection(self.possible_badges,
                                                    r.allitems())
        # not last elf in group
        if self.elf_ctr < self.group_size - 1:
           self.elf_ctr += 1
        else:
            self.elf_ctr = 0
            assert len(self.possible_badges) == 1
            badge = [b for b in self.possible_badges][0]
            self.total += shared.get_priority(badge)

bf = BadgeFinder()
shared.parse(sys.argv[1], bf.on_rucksack)
print(bf.total)
