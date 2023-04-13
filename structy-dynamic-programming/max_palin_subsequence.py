def max_palin_subsequence(string):
    return _max_palin_subsequence(string, 0, len(string) - 1, {})


def _max_palin_subsequence(string, i, j, memo):
    pair = (i, j)
    if pair in memo:
        return memo[pair]

    if i == j:
        return 1
    #   lool
    if i > j:
        return 0

    if string[i] == string[j]:
        memo[pair] = 2 + _max_palin_subsequence(string, i + 1, j - 1, memo)
    else:
        memo[pair] = max(
            _max_palin_subsequence(string, i + 1, j, memo),
            _max_palin_subsequence(string, i, j - 1, memo),
        )

    return memo[pair]
