import sys, shared
hmap = shared.parse(sys.argv[1])

# basic bfs

visited = set()
prev = {}
visited.add(hmap.start)
q = [hmap.start]
while len(q) > 0:
    cur = q.pop(0)
    if cur == hmap.end:
        # retrace path
        path = [cur]
        while cur in prev.keys():
            path.insert(0, prev[cur])
            cur = prev[cur]
        # -1 because this counts length of path, but they want number of steps,
        # which is 1 off
        print(len(path) - 1)
        sys.exit(0)
    # print('Neighbors of {}: {}'.format(cur, hmap.neighbors(cur)))
    for neighbor in hmap.neighbors(cur):
        if neighbor not in visited:
            visited.add(neighbor)
            prev[neighbor] = cur
            q.append(neighbor)

print('Path not found')
print(prev)