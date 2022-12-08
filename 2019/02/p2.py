import sys
sys.path.append('..')
from intcode import intcode
data = intcode.parse_file(sys.argv[1])
def try_nv(n, v):
    c = intcode.Computer()
    c.data = data.copy()
    c.data[1] = n
    c.data[2] = v
    c.run()
    return c.data[0]

target = 19690720

rn, rv = 99, 99
ln, lv = 1, 1
while ln < rn:
    n = ln + ((rn - ln) // 2)
    if try_nv(n, rv) > target:
        rn = ln
    else:
        ln = n

for noun in range(1, 100):
    for verb in range(1, 100):
        if try_nv(noun, verb) == target:
            print(noun, verb)
            print(100 * noun + verb)
            sys.exit(0)

print('FAILED TO FIND')
sys.exit(1)