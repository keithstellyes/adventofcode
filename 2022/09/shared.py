import typing

# (x, y)
dir_map = {'U':(0, 1), 'D':(0, -1), 'R': (1, 0), 'L': (-1, 0)}

class RopeState:
    def __init__(self, knots=2):
        # x, y!
        self.knots = [[0, 0] for _ in range(knots)]
        self.visited = set()

    def _nudgeknotx(self, idx):
        self.knots[idx][0] += 1 if self.knots[idx - 1][0] > self.knots[idx][0] else -1
    def _nudgeknoty(self, idx):
        self.knots[idx][1] += 1 if self.knots[idx - 1][1] > self.knots[idx][1] else -1

    def on_command(self, cmd):
        for _ in range(cmd.dist):
            self.knots[0][0] += cmd.dir[0]
            self.knots[0][1] += cmd.dir[1]

            for k in range(1, len(self.knots)):
                head = self.knots[k - 1]
                tail = self.knots[k]
                x_dist = abs(head[0] - tail[0])
                y_dist = abs(head[1] - tail[1])

                x_close = x_dist <= 1
                y_close = y_dist <= 1
                same_col = x_dist == 0
                same_row = y_dist == 0

                if x_close and y_close:
                    continue
                if not same_col:
                    self._nudgeknotx(k)
                if not same_row:
                    self._nudgeknoty(k)
            self.visited.add((self.knots[-1][0], self.knots[-1][1]))

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