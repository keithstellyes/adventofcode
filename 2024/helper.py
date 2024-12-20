def coordneighbors(coord: tuple[int], minc: tuple[int], maxc: tuple[int]):
    north = (coord[0], coord[1] - 1)
    east = (coord[0] + 1, coord[1])
    south = (coord[0], coord[1] + 1)
    west = (coord[0] - 1, coord[1])
    directions = (north, east, south, west)
    neighbors = []
    for d in directions:
        if d[0] < minc[0] or d[1] < minc[1]:
            continue
        if d[0] > maxc[0] or d[1] > maxc[1]:
            continue
        neighbors.append(d)
    return neighbors
