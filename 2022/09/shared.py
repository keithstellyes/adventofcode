import typing

# (x, y)
dir_map = {'U':(0, 1), 'D':(0, -1), 'R': (1, 0), 'L': (-1, 0)}

class Command(typing.NamedTuple):
    dir: typing.Tuple[int, int]
    dist: int

def parse(fname, on_command):
    for line in open(fname, 'r'):
        line = line.strip()
        if line == '':
            continue
        dir, dist = line.split(' ')
        on_command(Command(dir_map[dir], int(dist)))