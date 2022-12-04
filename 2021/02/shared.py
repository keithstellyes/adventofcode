directions = {'forward':(1, 0), 'down':(0, 1), 'up':(0, -1)}

class Move:
    def __init__(self, direction, distance):
        self.direction = direction
        self.distance = distance
    def apply(self, coord):
        return (coord[0] + self.direction[0] * self.distance,
               coord[1] + self.direction[1] * self.distance)

def parse(fname, on_move):
    for line in open(fname, 'r'):
        if line == '':
            continue
        line = line.strip()
        direct, dist = line.split(' ')
        direct = directions[direct]
        dist = int(dist)
        on_move(Move(direct, dist))
