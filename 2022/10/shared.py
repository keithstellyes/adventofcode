import typing

class Instr(typing.NamedTuple):
    op: str
    arg: typing.Optional[int]

def parse(fname, on_instr):
    for line in open(fname, 'r'):
        line = line.strip()
        if line == '':
            continue
        line = line.split(' ')
        op = line[0]
        arg = int(line[1]) if len(line) > 1 else None
        on_instr(Instr(op, arg))