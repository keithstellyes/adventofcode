def parse(fname):
    fishes = [int(fish) for fish in open(fname, 'r').read().strip().split(',')]
    pop = [0] * 9
    for f in fishes:
        pop[f] += 1
    return pop

def tick(pop):
    retpop = pop.copy()
    motherc = pop[0]
    for n in range(1, 9):
        retpop[n-1] = pop[n]
    retpop[6] += motherc
    retpop[8] = motherc
    return retpop