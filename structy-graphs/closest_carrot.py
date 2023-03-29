from collections import deque


def closest_carrot(grid, starting_row, starting_col):
    pass  # todo
    # shortest path problem, similar to island problems
    # iterate through the grid, breadth first search
    visited = set((starting_row, starting_col))
    queue = deque([(starting_row, starting_col, 0)])

    while queue:
        row, col, distance = queue.popleft()

        if grid[row][col] == "C":
            return distance

        deltas = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for delta in deltas:
            move_row, move_col = delta

            new_row = row + move_row
            new_col = col + move_col

            new_row_inbounds = 0 <= new_row < len(grid)
            new_col_inbounds = 0 <= new_col < len(grid[0])

            pos = (new_row, new_col)

            if (
                new_col_inbounds
                and new_row_inbounds
                and grid[new_row][new_col] != "X"
                and pos not in visited
            ):
                queue.append((new_row, new_col, distance + 1))
                visited.add(pos)

    return -1
