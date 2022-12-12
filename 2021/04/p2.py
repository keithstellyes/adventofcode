import sys, shared
moves, boards = shared.parse(sys.argv[1])
last_board = None, None, None
for move in moves:
    l = [b for b in boards if not b.has_won]
    for board in l:
        if board.on_num(move):
            unmarked_sum = 0
            for row in board.rowremaining:
                for n in row:
                    unmarked_sum += n
            last_board = board, unmarked_sum, move
_, us, mv = last_board
print('{} * {} = {}'.format(us, mv, us * mv))