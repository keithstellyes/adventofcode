class HeightMap:
    def __init__(self, rows, start, end):
        self.rows = rows
        self.start = start
        self.end = end
    def neighbors(self, coord, going_up=True):
        row = coord[0]
        col = coord[1]
        n = []
        # up, right, down, left
        n.append((row - 1, col))
        n.append((row, col + 1))
        n.append((row + 1, col))
        n.append((row, col - 1))
        candidates = [neigh for neigh in n if self.legal(neigh)]
        if coord == self.start:
            return candidates
        if going_up:
            maxheight = ord(self[coord]) + 1
            # showing off with a little optimization
            assert ord('S') < ord('a') and ord('E') < ord('z')
            return [neigh for neigh in candidates if ord(self[neigh]) <= maxheight]
        else:
            minheight = ord(self[coord]) - 1
            return [neigh for neigh in candidates if ord(self[neigh]) >= minheight]
    def rowc(self):
        return len(self.rows)
    def colc(self):
        return len(self.rows[0])
    
    def legal(self, coord):
        row = coord[0]
        col = coord[1]
        legality = row >= 0 and row < self.rowc() and col >= 0 and col < self.colc()
        return legality
    def __getitem__(self, it):
        return self.rows[it[0]][it[1]]

def parse(fname):
    rows = []
    start = None
    end = None
    for line in open(fname, 'r'):
        line = line.strip()
        if 'E' in line:
            end = (len(rows), line.index('E'))
            line = line.replace('E', 'z')
        if 'S' in line:
            start = (len(rows), line.index('S'))
            line = line.replace('S', 'a')
        rows.append(line)
    return HeightMap(rows, start, end)
