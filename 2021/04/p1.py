import sys, shared
moves, boards = shared.parse(sys.argv[1])

for move in moves:
    for board in boards:
        if board.on_num(move):
            print('Bingo!')
            unmarked_sum = 0
            for row in board.rowremaining:
                for n in row:
                    unmarked_sum += n
            print('{} * {} = {}'.format(unmarked_sum, move, unmarked_sum * move))
            sys.exit(0)
print('No winners!')