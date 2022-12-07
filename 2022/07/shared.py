class File:
    def __init__(self, name, length):
        self.name = name
        self.length = int(length)

class ParseState:
    def __init__(self, s):
        self.s = s
        self.index = 0
    def eof(self):
        return self.index >= len(self.s)
    def consume_line(self):
        out = ''
        while not self.eof() and self.s[self.index] != '\n':
            out += self.s[self.index]
            self.index += 1
        self.index += 1
        return out
    def curch(self):
        return self.s[self.index] if not self.eof() else None

global eid
eid = 0
class File:
    def __init__(self, name, size):
        self.name = name
        self.size = int(size)
        global eid
        self.id = eid
        eid += 1
    def get_size(self):
        return self.size

class Directory:
    def __init__(self, name, parent=None):
        self.dirs = {}
        self.files = []
        self.parent = parent
        self.name = name
        global eid
        self.id = eid
        eid += 1
    def add_entry(self, e):
        if type(e) == Directory:
            e.parent = self
            self.dirs[e.name] = e
        elif type(e) == str:
            self.add_entry(Directory(e))
        elif type(e) == File:
            self.files.append(e)
        else:
            assert False
    def children(self):
        return list(self.dirs.values()) + self.files
    def get_shallow_size(self):
        total = 0
        for f in self.files:
            total += f.size()
        return total
    def get_size(self):
        total = 0
        for c in self.children():
            total += c.get_size()
        return total

def print_e(e, indent=0):
    if dir is None:
        return
    print(e.id, ('-' * indent), e.name, end='')
    if type(e) == Directory:
        print('/', e.get_size())
        children = e.children()
        for c in children:
            print_e(c, indent+1)
    else:
        print('', e.get_size())

def parse(fname):
    s = ParseState(open(fname, 'r').read())
    assert s.consume_line() == '$ cd /'
    dir_tree = Directory('/')
    dirptr = dir_tree
    while not s.eof():
        l = s.consume_line()
        assert l.startswith('$ ')
        parts = l[2:].split(' ')
        cmd = parts[0]
        arg = parts[1] if len(parts) > 1 else None
        if cmd == 'cd':
            if arg == '..':
                dirptr = dirptr.parent
            else:
                dirptr = dirptr.dirs[arg]
        elif cmd == 'ls':
            while not s.eof() and s.curch() != '$':
                entry = s.consume_line()
                print(entry)
                len_or_dir, name = entry.split(' ')
                if len_or_dir == 'dir':
                    dirptr.add_entry(name)
                else:
                    dirptr.add_entry(File(name, len_or_dir))
    return dir_tree
