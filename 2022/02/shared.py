'''
This shared.py, I'm trying to have a nice software engineering architecture
(as much as can be done for a single day, in something like Advent of Code)
To that end, parsing and decryption are separated, the assumption being that
cheatsheets will always be:
    - a line per round
    - and 2 columns, separated by a space

Also making heavy use of callbacks, allowing for a running computation, making
this much more space efficient
'''

ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'
MOVE_POINTS = {ROCK: 1, PAPER: 2, SCISSORS: 3}
DECRYPTION_MAP = {'A': ROCK, 'X': ROCK, 'B': PAPER, 'Y': PAPER, 'C': SCISSORS,
                  'Z':SCISSORS}
WIN_MAP = {ROCK:SCISSORS, PAPER:ROCK, SCISSORS:PAPER}
LOSE_MAP = {v: k for k, v in WIN_MAP.items()}

class Round:
    def __init__(self, op_choice, my_choice):
        self.op_choice = op_choice
        self.my_choice = my_choice
    def score(self):
        move_pts = MOVE_POINTS[self.my_choice]
        outcome = 3
        if self.my_choice != self.op_choice:
            if WIN_MAP[self.my_choice] == self.op_choice:
                outcome = 6
            else:
                outcome = 0
        return move_pts + outcome
def parse_base(fname, decrypt, on_round):
    for l in open(fname, 'r'):
        l = l.strip()
        if l == '':
            continue
        col1, col2 = l.split()
        on_round(decrypt(col1, col2))

def parse(fname, on_round):
    parse_base(
        fname, 
        lambda col1, col2: Round(DECRYPTION_MAP[col1], DECRYPTION_MAP[col2]),
        on_round)

def parse2(fname, on_round):
    def decrypt(col1, col2):
        op = DECRYPTION_MAP[col1]
        if col2 == 'X':
            my = WIN_MAP[op]
        elif col2 == 'Y':
            my = op
        elif col2 == 'Z':
            my = LOSE_MAP[op]
        else:
            assert False
        return Round(op, my)
    parse_base(fname, decrypt, on_round)
