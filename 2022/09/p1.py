import sys, shared

class RopeState:
    def __init__(self):
        # x, y!
        self.headpos = [0, 0]
        self.tailpos = [0, 0]
        self.visited = set()

    def _nudgetailx(self):
        self.tailpos[0] += 1 if self.headpos[0] > self.tailpos[0] else -1
    def _nudgetaily(self):
        self.tailpos[1] += 1 if self.headpos[1] > self.tailpos[1] else -1

    def on_command(self, cmd):
        for _ in range(cmd.dist):
            self.headpos[0] += cmd.dir[0]
            self.headpos[1] += cmd.dir[1]

            x_dist = abs(self.headpos[0] - self.tailpos[0])
            y_dist = abs(self.headpos[1] - self.tailpos[1])

            x_close = x_dist <= 1
            y_close = y_dist <= 1
            same_col = x_dist == 0
            same_row = y_dist == 0

            if x_close and y_close:
                pass
            elif same_row:
                self._nudgetailx()
            elif same_col:
                self._nudgetaily()
            else:
                # if abs(cmd.dir[0]) > 0:
                #     self._nudgetailx()
                # elif abs(cmd.dir[1]) > 0:
                #     self._nudgetaily()
                self._nudgetailx()
                self._nudgetaily()
            self.visited.add((self.tailpos[0], self.tailpos[1]))

            # for y in range(10, -1, -1):
            #     for x in range(10):
            #         c = '.'
            #         if self.tailpos[0] == x and self.tailpos[1] == y:
            #             c = 'T'
            #         if self.headpos[0] == x and self.headpos[1] == y:
            #             c = 'H'
            #         print(c, end='')
            #     print()
            # print()

rs = RopeState()
shared.parse(sys.argv[1], rs.on_command)
print(len(rs.visited))