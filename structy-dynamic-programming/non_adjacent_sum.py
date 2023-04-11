def non_adjacent_sum(nums):
    return _non_adjacent_sum(nums, 0, {})


def _non_adjacent_sum(nums, i, memo):
    pass  # todo
    # visualize the recursion tree
    # dyprog is indicated by duplicate subtrees - can reduce space/time complexity using memoization
    # brute force time complexity: O(2^n) - for every node, you can expect two subnodes
    # brute force space complexity: O(n) - height of the tree will be n long. deepest recursion will require a call stack with n calls
    if i in memo:
        return memo[i]
    if i >= len(nums):
        return 0
    # think of this as a binary decision process: include OR exclude element in your eventual sum
    # include = nums[0] + _non_adjacent_sum(nums[2:])
    include = nums[i] + _non_adjacent_sum(nums, i + 2, memo)
    #   slicing creates a new copy of nums list, making it inefficient.
    # exclude = _non_adjacent_sum(nums[1:])
    exclude = _non_adjacent_sum(nums, i + 1, memo)

    memo[i] = max(include, exclude)
    return memo[i]
