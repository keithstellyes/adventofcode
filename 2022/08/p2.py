import sys, shared
forest = shared.parse(sys.argv[1])
rowc = len(forest)
colc = len(forest[0])
visibility_map = shared.build_visibility_map(forest)

max_score = 1
for r in range(rowc):
    for c in range(colc):
        tree = forest[r][c]
        scores = []
        for d in shared.dirs:
            _r, _c = r, c
            origin_tree = forest[_r][_c]
            _r += d[0]
            _c += d[1]
            if _r < 0 or _r >= rowc or _c < 0 or _c >= colc:
                scores.append(0)
                continue
            found = 0
            while _r >= 0 and _r < rowc and _c >= 0 and _c < colc:
                t = forest[_r][_c]
                if t >= origin_tree:
                    found += 1
                    break
                found += 1
                _r += d[0]
                _c += d[1]
            scores.append(found)
        score = 1
           
        for s in scores:
            score *= s
        #print(scores)
        if score > max_score:
            max_score = score
print(max_score)
