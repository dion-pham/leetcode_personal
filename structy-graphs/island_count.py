def island_count(grid):
    pass  # todo
    # island = connected components
    # need a visited set
    # problem where you need to establish movement by up,down,left,right
    # (r,c) -> r-1,c : r+1,c: r,c+1, : r,c-1

    # DFS??
    visited = set()
    count = 0
    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if explore(grid, r, c, visited) == True:
                #         do something
                count += 1
    return count


def explore(grid, r, c, visited):
    r_inbounds = 0 <= r < len(grid)
    c_inbounds = 0 <= c < len(grid[0])

    if not r_inbounds or not c_inbounds:
        return False

    if grid[r][c] == "W":
        return False

    pos = (r, c)
    if pos in visited:
        return False
    visited.add(pos)
    # if grid[r][c] in visited:
    # return False
    # visited.add(grid[r][c])

    explore(grid, r + 1, c, visited)
    explore(grid, r - 1, c, visited)
    explore(grid, r, c + 1, visited)
    explore(grid, r, c - 1, visited)
    return True


# grid = [
#   ['W', 'L', 'W', 'W', 'W'],
#   ['W', 'L', 'W', 'W', 'W'],
#   ['W', 'W', 'W', 'L', 'W'],
#   ['W', 'W', 'L', 'L', 'W'],
#   ['L', 'W', 'W', 'L', 'L'],
#   ['L', 'L', 'W', 'W', 'W'],
# ]

# island_count(grid) # -> 3
