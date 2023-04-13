import math


def summing_squares(n):
    return _summing_squares(n, {})


def _summing_squares(n, memo):
    pass  # todo

    if n in memo:
        return memo[n]
    # recursion involving subtracting a perfect square from n
    # 1^2, 2^2, 3^2
    # for time complexity, the branching factor of our recursion tree is the base of the exponent
    #   since branching factor is based on the square root of n, the brute force time complexity will look like Time: O(sqrt(n)^n)

    if n == 0:
        return 0

    min_squares = float("inf")
    for i in range(1, math.floor(math.sqrt(n) + 1)):
        square = i * i
        squares_count = 1 + _summing_squares(n - square, memo)
        min_squares = min(squares_count, min_squares)

    memo[n] = min_squares
    return memo[n]
    # 9 - 4 = 5
