def parse(fname, on_fuelreq):
    for line in open(fname, 'r'):
        line = line.strip()
        if line == '':
            continue
        on_fuelreq(int(line))
def fuel_required(mass):
    return mass // 3 - 2