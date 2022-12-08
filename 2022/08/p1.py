import sys, shared
forest = shared.parse(sys.argv[1])
rowc = len(forest)
colc = len(forest[0])
visibility_map = shared.build_visibility_map(forest)
print(sum([r.count(True) for r in visibility_map]))
