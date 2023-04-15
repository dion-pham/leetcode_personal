def can_concat(s, words):
    return _can_concat(s, words, {})


def _can_concat(s, words, memo):
    pass  # todo
    # brute force time complexity: n^s. n is the branching factor( for ex. 5 words means there would be at MOST 5 initial branches,
    # height of the tree s is the exponent
    if s in memo:
        return memo[s]

    if s == "":
        return True

    for word in words:
        if s.startswith(word):
            #     remember this
            suffix = s[len(word) :]
            if _can_concat(suffix, words, memo) == True:
                memo[s] = True
                return True

    memo[s] = False
    return False
