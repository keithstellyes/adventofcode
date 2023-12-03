#!/usr/bin/env python3
import re, sys

symbols = '@*/=-$&+#%'
rows = []
with open(sys.argv[1], 'r') as f:
    rows = [l.strip() for l in f.readlines()]

nummatch = re.compile('[0-9]+')
symbolmatch = re.compile(r'.*[\*' + r'@/=\-\$&\+#%]')
assert symbolmatch.match('*') is not None
x = 0
y = 0
total = 0
while y < len(rows):
    row = rows[y]
    candidates = nummatch.finditer(row)
    for candidate in candidates:
        found = False
        # clean way of handling the edge case of being on the edges
        # (pun not intended)
        xmin = max(0, candidate.start() - 1)
        xmax = min(len(row) - 1, candidate.end() + 1)
        cstr = row[candidate.start():candidate.end()]
        if y > 0:
            topmatches = symbolmatch.match(rows[y - 1][xmin:xmax])
            found = topmatches is not None
        if y < len(rows) - 1 and not found:
            botmatches = symbolmatch.match(rows[y + 1][xmin:xmax])
            found = botmatches is not None
        if not found:
            found = row[xmin] in symbols or row[xmax - 1] in symbols
        if found:
            total += int(cstr)
    y = y + 1
print(total)
