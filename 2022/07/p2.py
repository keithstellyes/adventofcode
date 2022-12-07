import sys, shared
t = shared.parse(sys.argv[1])
fs_space = 70000000
required_space = 30000000
space_to_free = required_space - (fs_space - t.get_size())
assert space_to_free > 0

best_candidate = t
q = [t]

while len(q) > 0:
    e = q.pop()
    sz = e.get_size()
    if sz < space_to_free:
        continue # not a candidate nor are its children
    if sz < best_candidate.get_size():
        best_candidate = e 
    for d in e.dirs.values():
        q.append(d)

print(best_candidate.get_size())
