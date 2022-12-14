import sys, shared
cave = shared.parse(sys.argv[1])
cave.run()
for y in range(40):
    for x in range(440, 520):
        if (x, y) in cave.rocks:
            print('#', end='')
        elif (x, y) in cave.settled_sand:
            print('o', end='')
        elif (x, y) == (500, 0):
            print('+', end='')
        else:
            print('.', end='')
    print()
print(len(cave.settled_sand))