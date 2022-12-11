import sys, shared
import termcolor

keep_away = shared.parse(sys.argv[1])
for _ in range(20):
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