# really jsut a range, but named "Assignment" per the story in the problem
class Assignment:
    def __init__(self, begin, end):
        self.begin = int(begin)
        self.end = int(end)
    # overloads Python's `in` operator
    def __contains__(self, item):
        # adding int support unnecessary for this problem, but added for
        # demonstration purposes of the power of operator overloading
        if type(item) == int:
            return item >= self.begin and item <= self.end
        elif type(item) == Assignment:
            return item.begin >= self.begin and item.end <= self.end
        else:
            return False

def parse_assignment(s):
    bs, es = s.split('-')
    return Assignment(bs, es)

def parse(fname, on_assignment_pair):
    for pair in open(fname, 'r'):
        pair = pair.strip()
        if pair == '':
            continue
        a1, a2 = pair.split(',')
        on_assignment_pair((parse_assignment(a1), parse_assignment(a2)))
