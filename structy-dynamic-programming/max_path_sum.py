def max_path_sum(grid):
    return _max_path_sum(grid, 0, 0, {})


def _max_path_sum(grid, row, col, memo):
    pass  # todo
    # top left implies needing to create a helper function that takes in 0,0
    # bottom right implies coordinates of row = len(grid) -1 and col = len(grid[0]) - 1
    # only down and only right implies deltas of (1,0) and (0,1)

    pos = (row, col)
    if pos in memo:
        return memo[pos]
    #   check for inbounds
    if row == len(grid) or col == len(grid[0]):
        return float("-inf")

    # check for bottom right corner
    if row == len(grid) - 1 and col == len(grid[0]) - 1:
        return grid[row][col]

    down = _max_path_sum(grid, row + 1, col, memo)
    right = _max_path_sum(grid, row, col + 1, memo)

    #   you want to choose the max between down/right to add to "myself." "myself" in this case is grid[row][col]
    # for better understanding of myself, think of what it is in respect to a visual diagram of a tree
    memo[pos] = (row, col)

    memo[pos] = grid[row][col] + max(down, right)
    return memo[pos]
