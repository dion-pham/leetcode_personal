def min_change(amount, coins):
    answer = _min_change(amount, coins, {})
    if answer == float("inf"):
        return -1
    return answer


def _min_change(amount, coins, memo):
    pass  # todo
    # same as the sum problem
    # in this case, once we find what indices that total up to our amount, we take the number of indices it took in

    # subtract a coin index from the amount and then run recursion to see if our amount ever gets to zero
    # from here, keep track of the memoization?
    if amount in memo:
        return memo[amount]

    if amount == 0:
        return 0

    if amount < 0:
        return float("inf")

    min_coins = float("inf")
    for coin in coins:
        num_coins = 1 + _min_change(amount - coin, coins, memo)
        if num_coins < min_coins:
            min_coins = num_coins

    memo[amount] = min_coins
    return min_coins
