from collections import deque


def knight_attack(n, kr, kc, pr, pc):
    pass  # todo
    #   given two starting positions, see if you can get from p1 to p2 with the following deltas:
    # as you move the deltas, keep track of your visited?

    # looking for shortest path from p1 to p2
    #   BFS is ideal for shortest path
    #   visit spots on the grid by means of BFS
    queue = deque([(kr, kc, 0)])
    visited = set()
    visited.add((kr, kc))

    while queue:
        r, c, distance = queue.popleft()
        if (r, c) == (pr, pc):
            return distance

        #     need a function to find the neighbors
        new_positions = move_knight(n, r, c)
        for new_position in new_positions:
            if new_position not in visited:
                new_r, new_c = new_position
                queue.append((new_r, new_c, distance + 1))
                visited.add((new_r, new_c))

    return None


def move_knight(n, kr, kc):
    positions = [
        (kr + 2, kc + 1),
        (kr + 2, kc - 1),
        (kr - 2, kc + 1),
        (kr - 2, kc - 1),
        (kr + 1, kc + 2),
        (kr + 1, kc - 2),
        (kr - 1, kc + 2),
        (kr - 1, kc - 2),
    ]

    new_positions = []
    for position in positions:
        new_r, new_c = position
        if 0 <= new_r < n and 0 <= new_c < n:
            new_positions.append((new_r, new_c))
    return new_positions


knight_attack(8, 1, 1, 2, 2)  # -> 2
