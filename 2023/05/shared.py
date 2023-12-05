class AlmanacGenericMap:
    def __init__(self, dest_range_starts, source_range_starts, range_lengths):
        self.dest_range_starts = dest_range_starts
        self.source_range_starts = source_range_starts
        self.range_lengths = range_lengths
    def convert(self, val: int):
        for i in range(len(self.source_range_starts)):
            srs = self.source_range_starts[i]
            if val >= srs and val < srs + self.range_lengths[i]:
                return (val - srs) + self.dest_range_starts[i]
        return val
    def trace(self, val: int):
        for i in range(len(self.source_range_starts)):
            srs = self.source_range_starts[i]
            if val >= srs and val < srs + self.range_lengths[i]:
                return i
        return -1

    def __str__(self):
        s = 'Almanac map:'
        for i in range(len(self.source_range_starts)):
            s += f'({self.dest_range_starts[i]} -> +{self.range_lengths[i]}'
            s += f', {self.source_range_starts[i]} -> +{self.range_lengths[i]})'
        return s
class Almanac:
    def __init__(self, seed2soil, soil2fert, fert2water, water2light, light2temp,
                 temp2humid, humid2loc):
        self.seed2soil = seed2soil
        self.soil2fert = soil2fert
        self.fert2water = fert2water
        self.water2light = water2light
        self.light2temp = light2temp
        self.temp2humid = temp2humid
        self.humid2loc = humid2loc
        self.maps = (seed2soil, soil2fert, fert2water, water2light, light2temp,
                     temp2humid, humid2loc)
    def convert_seed_to_location(self, seed: int):
        val = seed
        for m in self.maps:
            val = m.convert(val)
        return val
    def trace(self, seed):
        t = []
        val = seed
        for m in self.maps:
            t.append(m.trace(val))
            val = m.convert(val)
        return t
def parse_almanac_generic_map(f):
    dest_range_starts, source_range_starts, range_lengths = [], [], []
    for line in f:
        line = line.strip()
        if line == '':
            return AlmanacGenericMap(dest_range_starts, source_range_starts, range_lengths)
        drs, srs, rl = [int(part) for part in line.split (' ') if part != '']
        dest_range_starts.append(drs)
        source_range_starts.append(srs)
        range_lengths.append(rl)
    return AlmanacGenericMap(dest_range_starts, source_range_starts, range_lengths)

def parse_almanac(f):
    seed2soil, water2light, light2temp, temp2humid, humid2loc = None, None, \
            None, None, None
    seed2soil = parse_almanac_generic_map(f)
    f.readline()
    soil2fert = parse_almanac_generic_map(f)
    f.readline()
    fert2water = parse_almanac_generic_map(f)
    f.readline()
    water2light = parse_almanac_generic_map(f)
    f.readline()
    light2temp = parse_almanac_generic_map(f)
    f.readline()
    temp2humid = parse_almanac_generic_map(f)
    f.readline()
    humid2loc = parse_almanac_generic_map(f)
    return Almanac(seed2soil, soil2fert, fert2water, water2light, light2temp, temp2humid, humid2loc)
