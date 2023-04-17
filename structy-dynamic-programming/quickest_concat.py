def quickest_concat(s, words):
    answer = _quickest_concat(s, words, {})
    if answer == float("inf"):
        return -1
    else:
        return answer


def _quickest_concat(s, words, memo):
    pass  # todo

    if s in memo:
        return memo[s]

    if s == "":
        return 0

    min_count = float("inf")
    for word in words:
        if s.startswith(word):
            remainder = s[len(word) :]
            #               = s[2:]
            attempt = 1 + _quickest_concat(remainder, words, memo)
            min_count = min(attempt, min_count)

    memo[s] = min_count
    return memo[s]


# memo[ion] = 1

quickest_concat("caution", ["ca", "ion", "caut", "ut"])  # -> 2
