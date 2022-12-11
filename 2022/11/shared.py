import string, typing

class Expr:
    def __init__(self, op:str, a0:typing.Union[str, int], a1:typing.Union[str, int]):
        self.op = op
        self.a0 = a0
        self.a1 = a1
    def eval(self, worry):
        a0 = self.a0 if type(self.a0) == int else worry
        a1 = self.a1 if type(self.a1) == int else worry
        if self.op == '+':
            return a0 + a1
        elif self.op == '*':
            return a0 * a1
    def __str__(self):
        return '{} {} {}'.format(self.a0, self.op, self.a1)

class MonkeyMove(typing.NamedTuple):
    recipient: int
    item: int

class Monkey:
    def __init__(self, items:list[int], inspect:Expr, testfactor:int, mt:int, mf:int):
        self.items = items
        self.inspect = inspect
        self.testfactor = testfactor
        self.mt = mt
        self.mf = mf
        self.inspect_ctr = 0
    def turn(self, worry_decay):
        self.inspect_ctr += len(self.items)
        moves = []
        
        while len(self.items) > 0:
            it = self.items.pop(0)
            it = self.inspect.eval(it)
            # monkey gets bored, worry decreases and throws it
            if worry_decay:
                it //= 3
            recipient = self.mt if it % self.testfactor == 0 else self.mf
            moves.append(MonkeyMove(recipient=recipient, item=it))
        return moves
    def __str__(self):
        s = '(Monkey '
        s += 'carrying=[' + ', '.join([str(it) for it in self.items]) + '] '
        s += 'inspect=({}) '.format(self.inspect)
        s += '{} if worry % {} == 0 else {}'.format(self.mt, self.testfactor, self.mf) + ' '
        s += 'inspect_ctr = {})'.format(self.inspect_ctr)
        return s

class KeepAway:
    def __init__(self, monkeys:list[Monkey], worry_decay:bool):
        self.monkeys = monkeys
        self.worry_decay = worry_decay
        self.max_item = 1
        # as is hinted in the problem description for Part 2:
        # "Unfortunately, that relief was all that was keeping your worry levels
        # from reaching ridiculous levels. You'll need to find another way to
        # keep your worry levels manageable."
        # The logic of the problem is only considered by divisibility after throws,
        # not the actual final value of worry levels, without this digits can grow
        # expoentialy!
        for m in monkeys:
            self.max_item *= m.testfactor
    def round(self, count=1):
        for _ in range(count):
            for monkey in self.monkeys:
                for move in monkey.turn(self.worry_decay):
                    self.monkeys[move.recipient].items.append(move.item % self.max_item)
    def __str__(self):
        return '(KeepAway\n  ' + '\n  '.join([str(m) for m in self.monkeys]) + '\n)' 

class ParseState:
    def __init__(self, src):
        self.src = src
        self.index = 0
    def expectstr(self, s):
        assert self.src[self.index:self.index+len(s)] == s
        self.index += len(s)
    def eof(self):
        return self.index >= len(self.src)
    def skipws(self):
        while not self.eof() and self.src[self.index] in string.whitespace:
            self.index += 1
    def consumeline(self):
        line = ''
        while not self.eof() and self.src[self.index] != '\n':
            line += self.src[self.index]
            self.index += 1
        self.index += 1
        return line
    def consumeint(self):
        digits = ''
        while self.src[self.index] in string.digits:
            digits += self.src[self.index]
            self.index += 1
        return int(digits)

def parse(fname, worry_decay=True):
    monkeys = []
    f = open(fname, 'r')
    parse_state = ParseState(f.read())
    f.close()
    while not parse_state.eof():
        parse_state.skipws()
        parse_state.expectstr('Monkey {}:'.format(len(monkeys)))
        parse_state.skipws()
        parse_state.expectstr('Starting items:')
        items = [int(it) for it in parse_state.consumeline().strip().split(',')]
        parse_state.skipws()
        parse_state.expectstr('Operation: new =')
        exprparts = parse_state.consumeline().strip().split(' ')
        assert len(exprparts) == 3
        arg0, op, arg1 = exprparts
        arg0 = int(arg0) if arg0 != 'old' else 'old'
        arg1 = int(arg1) if arg1 != 'old' else 'old'
        parse_state.skipws()
        parse_state.expectstr('Test: divisible by')
        parse_state.skipws()
        testfactor = parse_state.consumeint()
        parse_state.skipws()
        parse_state.expectstr('If true: throw to monkey ')
        mt = parse_state.consumeint()
        parse_state.skipws()
        parse_state.expectstr('If false: throw to monkey ')
        mf = parse_state.consumeint()
        monkeys.append(Monkey(items, Expr(op, arg0, arg1), testfactor, mt, mf))
        parse_state.skipws()
    return KeepAway(monkeys, worry_decay)