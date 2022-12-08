def parse(fname):
    rows = []
    for line in open(fname, 'r'):
        line = line.strip()
        rows.append([int(t) for t in line])
    return rows
