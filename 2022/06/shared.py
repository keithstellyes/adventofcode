def parse(fname, window_size=4):
    f = open(fname, 'r')

    index = 0
    ring_buffer = [None] * window_size
    counts = {}
    while len(counts.keys()) != window_size:
        c = f.read(1)
        if index >= window_size:
            old = ring_buffer[index % window_size]
            counts[old] -= 1
            if counts[old] == 0:
                del counts[old]
        ring_buffer[index % window_size] = c
        counts[c] = counts.get(c, 0) + 1
        index += 1
    f.close()
    return index
