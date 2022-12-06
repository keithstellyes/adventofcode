def parse(fname, on_number):
    for line in open(fname, 'r'):
        line = line.strip()
        if line == '':
            continue
        on_number(line.strip())
