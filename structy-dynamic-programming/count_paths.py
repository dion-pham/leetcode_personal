def count_paths(grid):
    return _count_paths(
        grid, 0, 0, {}
    )  # starting off by creating helper function to establish a (0,0) starting point. then we do memoization after


def _count_paths(grid, row, col, memo):
    pass  # todo
    pos = (row, col)
    if pos in memo:
        return memo[pos]
    if row == len(grid) or col == len(grid[0]) or grid[row][col] == "X":
        return 0

    if (
        row == len(grid) - 1 and col == len(grid[0]) - 1
    ):  # used just to get to the bottom right cell. this is used for this problem
        # if grid[row][col] == grid[len(grid)-1][len(grid[0])-1]: #used when checking for value of bottom right cell. not needed
        return 1

    down = _count_paths(grid, row + 1, col, memo)
    right = _count_paths(grid, row, col + 1, memo)
    memo[pos] = down + right
    return memo[pos]
