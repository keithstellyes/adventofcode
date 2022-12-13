import string

# Recursive descent parser
class Parser:
    def __init__(self, s):
        self.s = s
        self.index = 0
    def eof(self):
        return self.index >= len(self.s)
    def parse_packet_pair(self):
        return self.consume_packet(), self.consume_packet()
    def skipws(self):
        while not self.eof() and self.s[self.index] in string.whitespace:
            self.index += 1
    # a standard method in recursive descent parsers, when something
    # (char, string, token, grammar item, etc)
    # is expected at current index, and moves index past it.
    def expect(self, s):
        assert self.s[self.index:self.index+len(s)] == s
        self.index += len(s)

    # next() or cur() is another standard method, just gets current token
    def next(self):
        return self.s[self.index] if not self.eof() else None
    # consume methods return the value while moving index past it
    def consume_packet(self):
        l = self.consume_list()
        self.skipws()
        return l
    def consume_ch(self):
        c = self.s[self.index]
        self.index += 1
        return c
    def consume_list(self):
        self.expect('[')
        data = []
        while not self.eof():
            # alternatively a recursive descent parser may use an accept() method,
            # but here just easier to just elif it
            if self.next() in string.digits:
                data.append(self.consume_int())
            elif self.next() == '[':
                data.append(self.consume_list())
            elif self.next() == ',':
                self.consume_ch()
            elif self.next() == ']':
                self.consume_ch()
                break
            else:
                raise Exception('Unexpected token ({})'.format(self.s[self.index]))
        
        return data
    def consume_int(self):
        s = ''
        while not self.eof() and self.s[self.index] in string.digits:
            s += self.consume_ch()
        return int(s)
            

def parse(fname, on_packetpair):
    f = open(fname, 'r')
    s = f.read()
    f.close()
    parser = Parser(s)
    while not parser.eof():
        on_packetpair(parser.parse_packet_pair())