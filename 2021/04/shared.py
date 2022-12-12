class Board:
    def __init__(self, rows):
        self.rows = rows
        self.rowremaining = [set() for _ in range(len(rows))]
        self.colremaining = [set() for _ in range(len(rows[0]))]
        for r in range(len(rows)):
            for c in range(len(rows[0])):
                self.rowremaining[r].add(rows[r][c])
                self.colremaining[c].add(rows[r][c])
        self.has_won = False
    def on_num(self, num):
        win = False
        for row in self.rowremaining:
            row.discard(num)
            if len(row) == 0:
                win = True
        for col in self.colremaining:
            col.discard(num)
            if len(col) == 0:
                win = True
        self.has_won = self.has_won or win
        return win
    def __hash__(self):
        return hash(str(self))
    def __eq__(self, rhs):
        return str(self) == str(rhs)

def parse(fname):
    moves = None
    number_of_columns = 5
    number_of_rows = 5
    boards = []
    def parse_row(row):
        vals = []
        for n in range(number_of_columns):
            vals.append(int(row[n*3:n*3+2]))
        return vals
    with open(fname, 'r') as f:
        moves = [int(n) for n in f.readline().strip().split(',')]
        # begin boards
        # every board begins with a \n, then 5 rows of integers
        while True:
            l = f.readline()
            assert l == '' or l == '\n'
            if l == '':
                break
            rows = []
            for _ in range(number_of_rows):
                rows.append(parse_row(f.readline()))
            boards.append(Board(rows))
    return moves, boards