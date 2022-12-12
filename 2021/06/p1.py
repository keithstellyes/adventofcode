import sys, shared
pop = shared.parse(sys.argv[1])
for _ in range(80):
    pop = shared.tick(pop)
print(pop, sum(pop))