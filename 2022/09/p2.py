import sys, shared

rs = shared.RopeState(10)
shared.parse(sys.argv[1], rs.on_command)
print(len(rs.visited))