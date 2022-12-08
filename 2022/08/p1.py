import sys, shared
forest = shared.parse(sys.argv[1])
rowc = len(forest)
colc = len(forest[0])
vmap_row = [False] * colc
visibility_map = [vmap_row.copy() for _ in range(rowc)]
print('rows:', rowc, 'colc:', colc)

rayc = ((colc - 2) * 2 + (rowc - 2) * 2)

def shoot_ray(forest, visibility_map, dir, startr, startc):
    r = startr
    c = startc
    tallest_tree = -1
    while r >= 0 and r < rowc and c >= 0 and c < colc:
        tree = forest[r][c]
        # A tree is visible if all other trees are shorter
        if tree > tallest_tree:
            tallest_tree = tree
            visibility_map[r][c] = True
        r += dir[0]
        c += dir[1]

top_g_down = (1, 0)
right_g_left = (0, -1)
bot_g_up = (-1, 0)
left_g_right = (0, 1)

for n in range(1, colc-1):
    shoot_ray(forest, visibility_map, top_g_down, 0, n)
    shoot_ray(forest, visibility_map, bot_g_up, rowc-1, n)

for n in range(1, rowc-1):
    shoot_ray(forest, visibility_map, left_g_right, n, 0)
    shoot_ray(forest, visibility_map, right_g_left, n, colc-1)

visibility_map[0][0] = True
visibility_map[0][colc-1] = True
visibility_map[rowc-1][colc-1] = True
visibility_map[rowc-1][0] = True

print(sum([r.count(True) for r in visibility_map]))
