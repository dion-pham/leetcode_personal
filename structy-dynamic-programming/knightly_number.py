def knightly_number(n, m, kr, kc, pr, pc):
    return _knightly_number(n, m, kr, kc, pr, pc, {})


def _knightly_number(n, m, kr, kc, pr, pc, memo):
    pass  # todo
    #   starting -> target. needs EXACTLY m moves
    # cannot move out of bounds
    # recursion
    # m has to decrease with each recursive call

    #   m=1
    # SINCE THIS IS BASE CASE, WE CAN'T DO THIS BECAUSE IT MIGHT CAUSE
    # AN EARLY RETURN OF 0 WHEN WE HAVE NOT YET FINISHED MOVES
    # if m == 0 and kr == pr and kc == pc:
    #   return 1
    # else:
    #   return 0
    key = (m, kr, kc)
    if key in memo:
        return memo[key]

    if kr < 0 or kr >= n or kc < 0 or kc >= n:
        return 0

    if m == 0:
        if kr == pr and kc == pc:
            return 1
        else:
            return 0

    neighbors = [
        (kr + 2, kc + 1),
        (kr - 2, kc + 1),
        (kr + 2, kc - 1),
        (kr - 2, kc - 1),
        (kr + 1, kc + 2),
        (kr - 1, kc + 2),
        (kr + 1, kc - 2),
        (kr - 1, kc - 2),
    ]

    count = 0
    for neighbor in neighbors:

        count += _knightly_number(n, m - 1, neighbor[0], neighbor[1], pr, pc, memo)

    memo[key] = count
    return memo[key]
