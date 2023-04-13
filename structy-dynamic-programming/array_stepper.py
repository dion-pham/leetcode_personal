def array_stepper(numbers):
    return _array_stepper(numbers, 0, {})


def _array_stepper(numbers, index, memo):
    pass  # todo

    if index in memo:
        return memo[index]

    if index >= len(numbers) - 1:
        return True

    max_step = numbers[index]

    for step in range(1, max_step + 1):
        if _array_stepper(numbers, index + step, memo):
            memo[index] = True
            return True

    memo[index] = False
    return False


# base case: if pointer is at last position of index, return True
# if pointer == len(numbers) -1, return True
