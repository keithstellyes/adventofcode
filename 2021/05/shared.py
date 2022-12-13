def parse(fname, on_line):
    for line in open(fname, 'r'):
        line = line.strip()
        if line == '':
            continue
        line = line.split(' -> ')
        origin = tuple([int(n) for n in line[0].split(',')])
        dest = tuple([int(n) for n in line[1].split(',')])
        on_line((origin, dest))