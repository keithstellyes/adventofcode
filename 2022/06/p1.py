import sys, shared
f = open(sys.argv[1], 'r')

WINDOW_SIZE = 4

index = 0
ring_buffer = [None] * WINDOW_SIZE
counts = {}
while len(counts.keys()) != WINDOW_SIZE:
    c = f.read(1)
    if index >= WINDOW_SIZE:
        old = ring_buffer[index % 4]
        counts[old] -= 1
        if counts[old] == 0:
            del counts[old]
    ring_buffer[index % 4] = c
    counts[c] = counts.get(c, 0) + 1
    index += 1

print(index)
