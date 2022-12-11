import sys, shared
import termcolor

# I hypothesized there was a cycle that I could figure out, to then
# compute a monkey's inspect count at some arbitrary round,
# however, this hypothesis proved false. I leave this here as documentation of 
# that failed hypothesis.
def detect_cycle(nums):
    cycle = nums[:1]
    cycle_idx = 0
    for n in range(1, len(nums)):
        cycle_idx %= len(cycle)
        if cycle[cycle_idx] != nums:
            # cycle broken
            cycle = nums[:n]
            cycle_idx += 1
        else:
            cycle_idx += 1
    return cycle

keep_away = shared.parse(sys.argv[1], False)
# prev_rounds = [[0] * len(keep_away.monkeys)]
for n in range(10_000):
    keep_away.round()

monkeys_top = [m.inspect_ctr for m in keep_away.monkeys]
monkeys_top.sort()
top2 = monkeys_top[::-1][:2]

for n in range(len(keep_away.monkeys)):
    m = keep_away.monkeys[n]
    s = 'Monkey {} inspected items {} times'.format(n, m.inspect_ctr)
    if m.inspect_ctr in top2:
        termcolor.cprint(s, attrs=['bold'])
    else:
        print(s)

print('Monkey business:', top2[0] * top2[1])