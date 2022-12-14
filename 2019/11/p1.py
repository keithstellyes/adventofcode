import sys, shared
import collections
sys.path.append('..')
from intcode import intcode

r = shared.Robot()
c = intcode.Computer(on_in=r.on_in, on_out=r.on_out)
c.data = intcode.parse_file(sys.argv[1])
c.run()
print(len(r.painted.values()))