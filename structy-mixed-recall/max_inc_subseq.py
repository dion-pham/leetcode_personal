def max_increasing_subseq(numbers):
    return _max_increasing_subseq(numbers, 0, float("-inf"), {})


# can slice out the array
# find the longest subsequence in which the numbers are increasing in order

# dynamic programming: recursion tree branches depending on whether or not you take the first element in the list
# take or dont take the current number


def _max_increasing_subseq(numbers, index, previous, memo):
    key = (index, previous)
    if key in memo:
        return memo[key]

    if index == len(numbers):
        return 0

    current = numbers[index]
    #   create an array to determine the max between the two options (the two recursive calls )
    options = []

    dont_take_current = _max_increasing_subseq(numbers, index + 1, previous, memo)
    options.append(dont_take_current)

    if current > previous:
        take_current = 1 + _max_increasing_subseq(numbers, index + 1, current, memo)
        options.append(take_current)

    # refer to the counting logic on line 22. options would be a list comparing two numbers depending on whether or not we took the first index
    # to determine how large the subsequence would be
    memo[key] = max(options)
    return memo[key]
