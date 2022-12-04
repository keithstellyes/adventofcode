def parse(fname, on_depth):
    for line in open(fname, 'r'):
        line = line.strip()
        on_depth(int(line))
