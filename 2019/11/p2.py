import sys, shared
import collections
sys.path.append('..')
from intcode import intcode

r = shared.Robot()
r.painted[(0, 0)] = 1
c = intcode.Computer(on_in=r.on_in, on_out=r.on_out)
c.data = intcode.parse_file(sys.argv[1])
c.run()
ytop = max([c[1] for c in r.painted.keys()])
xright = max([c[0] for c in r.painted.keys()])
ybot = min([c[1] for c in r.painted.keys()])
xleft = min([c[0] for c in r.painted.keys()])
y = ytop
while y >= ybot:
    x = xleft
    while x <= xright:
        if (x, y) in r.painted.keys() and r.painted[x, y] == 1:
            print('█', end='')
        else:
            print(' ', end='')
        x += 1
    y -= 1
    print()