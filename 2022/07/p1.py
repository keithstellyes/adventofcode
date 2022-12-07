import sys, shared
t = shared.parse(sys.argv[1])
dirq = [t]
total = 0

shared.print_e(t)
while len(dirq) > 0:
    d = dirq.pop()
    if d.get_size() <= 100000:
        total += d.get_size()
    for ch in d.dirs.values():
        dirq.append(ch)
print(total)
