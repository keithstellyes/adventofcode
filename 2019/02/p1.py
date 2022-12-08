import sys
sys.path.append('..')
from intcode import intcode
c = intcode.Computer()
c.data = intcode.parse_file(sys.argv[1])
c.data[1] = 12
c.data[2] = 2
c.run()
print(c.data[0])