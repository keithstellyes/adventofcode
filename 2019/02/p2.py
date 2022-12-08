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

# for every possible noun, do a binary search
# for a verb that equals the target
for noun in range(1, 100):
    lv = 1
    rv = 99
    while lv < rv:
        v = (lv + rv) // 2
        result = try_nv(noun, v)
        if(result == target):
            print('Noun:', noun, 'Verb:', v)
            print(100 * noun + v)
            sys.exit(0)
        elif result < target:
            lv = v + 1
        else:
            rv = v - 1
print('FAILED TO FIND')
sys.exit(1)