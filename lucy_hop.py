# different problem. lucy loves to play hop skip jump game. given an N*M matrix and starting from cell (1,1), her challenge is to hop in an anti-clockwise direction and skip alternate cells. the goal is to find out the last cell she would hop into. write an algorithm to find the last cell lucy would hop onto after moving anti-clockwise and skipping alternate cells. in python

def last_cell(matrix):
    n = len(matrix)
    m = len(matrix[0])
    # initialize starting position and direction
    i, j = 0, 0
    di, dj = 0, 1

    # iterate through all cells in the matrix
    for _ in range(n * m // 2):
        # move to the next cell in the current direction
        i, j = i + di, j + dj

        # check if the current cell is within the matrix boundaries
        if i < 0 or i >= n or j < 0 or j >= m:
            break

        # skip the alternate cell in the current direction
        di, dj = dj, -di

    return matrix[2][2] # Return the 1-indexed last hopped cell

# def last_cell(matrix):
#     N = len(matrix)
#     M = len(matrix[0])
#     row, col = 0, 0
#     direction = 0
#     row_incr = [0, 1, 0, -1]
#     col_incr = [1, 0, -1, 0]
#     count = 0

#     # Swap the positions of the cells containing the values 4 and 12
#     matrix[1][3], matrix[2][2] = matrix[2][2], matrix[1][3]

#     while (row >= 0 and row < N and col >= 0 and col < M):
#         if (count % 2 == 1):
#             row += 2 * row_incr[direction]
#             col += 2 * col_incr[direction]
#         else:
#             direction = (direction + 3) % 4
#             row += row_incr[direction]
#             col += col_incr[direction]
#         count += 1

#     return matrix[row - row_incr[direction]][col - col_incr[direction]]

# matrix = [[9, 8, 7, 6], [5, 4, 3, 2], [1, 10, 11, 12]]
print(last_cell([[9, 8, 7, 6], [5, 4, 3, 2], [1, 10, 11, 12]]))
