def befitting_brackets(string):
    pass  # todo
    # if you come across an opener, push the closer to the stack
    # when you come across a closer, check if that closer is on top of the stack when
    stack = []
    brackets = {"[": "]", "{": "}", "(": ")"}

    for char in string:
        if char in brackets:
            stack.append(brackets[char])
        else:
            if stack and char == stack[-1]:
                stack.pop()
            else:
                return False

    return len(stack) == 0
