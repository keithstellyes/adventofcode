import sys
sys.path.append('..')
from intcode import intcode
c = intcode.Computer()
c.data = intcode.parse_file(sys.argv[1])
c.inputq.append(1)
c.run()