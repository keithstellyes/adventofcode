def parse(fname, callback):
    for line in open(fname, 'r'):
        line = line.strip()
        if line == '':
            continue