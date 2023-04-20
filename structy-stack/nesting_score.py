def nesting_score(string):
    pass  # todo
    # when you see [, add it to the stack
    # when you see ] and the top most item on stack is [,
    # increase score by one

    stack = [0]
    for char in string:
        if char == "[":
            stack.append(0)
        else:
            popped = stack.pop()
            if popped == 0:
                stack[-1] += 1
            else:
                stack[-1] += popped * 2

    return stack[0]
